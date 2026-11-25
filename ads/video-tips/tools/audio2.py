import numpy as np, json, wave, sys
sr=44100; T=12.0; N=int(sr*T); rng=np.random.default_rng(3)
def bp(x,lo,hi):
    X=np.fft.rfft(x); f=np.fft.rfftfreq(len(x),1/sr); X[(f<lo)|(f>hi)]=0; return np.fft.irfft(X,len(x))
def env(n,a,d): t=np.arange(n)/sr; return np.minimum(1,t/max(a,1e-4))*np.exp(-t/d)
def nz(n): return rng.standard_normal(n)
def sw(n,f0,f1,shape='sin'):
    t=np.arange(n)/sr; f=f0*(f1/f0)**(t/(n/sr)); ph=2*np.pi*np.cumsum(f)/sr
    return np.sin(ph) if shape=='sin' else 2*((ph/(2*np.pi))%1)-1
def norm(x,p=1.0): m=np.max(np.abs(x)); return x*(p/m) if m>0 else x
# ---------- drums / music 128bpm ----------
bpm=128; b=60/bpm
def kick():
    n=int(.35*sr); return norm(sw(n,160,48)*env(n,.001,.09)+0.6*bp(nz(n),2000,6000)*env(n,.0005,.004))
def clap():
    n=int(.25*sr); x=bp(nz(n),900,3500); e=env(n,.001,.07)
    for d in (0.008,0.016): k=int(d*sr); e[k:]+=0.6*env(n-k,.001,.05)
    return norm(x*e)
def hat(open_=False):
    n=int((.18 if open_ else .05)*sr); return norm(bp(nz(n),7000,15000)*env(n,.0005,.06 if open_ else .012))
def stab(freqs):
    n=int(.22*sr); x=sum(sw(n,f,f,'saw') for f in freqs); x=bp(x,200,3000); return norm(x*env(n,.003,.09))
mus=np.zeros(N); duck=np.ones(N)
chords=[[220,261.6,329.6],[174.6,220,261.6],[196,246.9,293.7],[164.8,207.7,246.9]]
def add(buf,s,t,g):
    i=int(t*sr); j=min(N,i+len(s)); 
    if i<N: buf[i:j]+=g*s[:j-i]
K,C,H,HO=kick(),clap(),hat(),hat(True)
nb=int(T/b)+1
for i in range(nb):
    t=i*b
    if t>11.4: break
    add(mus,K,t,0.9)
    m=int(t*sr); dk=int(.18*sr); duck[m:m+dk]=np.minimum(duck[m:m+dk],np.linspace(0.35,1,min(dk,N-m)))
    if i%2==1: add(mus,C,t,0.55)
    add(mus,H,t+b/2,0.35); add(mus,H,t+b/4,0.18); add(mus,H,t+3*b/4,0.18)
    ch=chords[(i//4)%4]; add(mus,stab(ch),t+b/2,0.45*duck[min(N-1,int((t+b/2)*sr))])
    if i%4==3: add(mus,HO,t+b/2,0.3)
# bass line (audible harmonics)
for i in range(nb):
    t=i*b; 
    if t>11.4: break
    f=chords[(i//4)%4][0]/2; n=int(b*0.9*sr); s=sw(n,f,f,'saw'); s=bp(s,60,900)*env(n,.005,.2); add(mus,norm(s),t+b/2,0.35)
mus*=duck**0.5
# ---------- SFX (phone-audible) ----------
def S(kind,dur=None):
    if kind=='slam':
        n=int(.3*sr); return norm(0.8*bp(nz(n),700,5000)*env(n,.0005,.05)+0.7*sw(n,260,90)*env(n,.001,.08))
    if kind=='punch':
        n=int(.9*sr); crack=bp(nz(n),500,6000)*env(n,.0005,.08); body=sw(n,300,60)*env(n,.001,.15); tail=bp(nz(n),4000,12000)*env(n,.005,.35)*0.4
        return norm(crack+body+tail)
    if kind in('whoosh','swoosh'):
        L=.45 if kind=='whoosh' else .28; n=int(L*sr); t=np.arange(n)/n; x=nz(n); y=np.zeros(n); seg=8
        for s in range(seg):
            a=int(s*n/seg); c=int((s+1)*n/seg); lo=400*(12**(s/seg)); y[a:c]=bp(x,lo,lo*4)[a:c]
        return norm(y*np.sin(np.pi*t)**1.5)
    if kind=='pop':
        n=int(.14*sr); return norm(sw(n,900,2000)*env(n,.001,.04)+0.3*bp(nz(n),2000,6000)*env(n,.0005,.006))
    if kind=='tick':
        n=int(.06*sr); return norm(bp(nz(n),2500,8000)*env(n,.0005,.01))*0.6
    if kind=='impact':
        n=int(1.1*sr); return norm(bp(nz(n),600,6000)*env(n,.0005,.09)+0.8*sw(n,320,70)*env(n,.001,.2)+0.5*bp(nz(n),5000,14000)*env(n,.01,.5))
    if kind=='ding':
        n=int(1.3*sr); t=np.arange(n)/sr; e=env(n,.001,.45)
        return norm((np.sin(2*np.pi*1568*t)+0.6*np.sin(2*np.pi*2352*t)+0.35*np.sin(2*np.pi*3136*t)+0.2*np.sin(2*np.pi*4704*t))*e)
    if kind=='click':
        n=int(.08*sr); return norm(sw(n,2600,1400)*env(n,.0005,.015))
    if kind=='typing':
        n=int(dur*sr); x=np.zeros(n); step=int(sr/12)
        for i in range(0,n-int(.03*sr),step):
            m=int(.03*sr); x[i:i+m]+=bp(nz(m),2500,7000)*env(m,.0005,.005)*(0.7+0.3*rng.random())
        return norm(x)*0.5
    return np.zeros(1)
G={'slam':0.9,'punch':1.0,'whoosh':0.8,'swoosh':0.7,'pop':0.75,'tick':0.5,'impact':1.0,'ding':0.75,'click':0.7,'typing':0.5}
ev=json.load(open(sys.argv[1]))[sys.argv[2]]
fx=np.zeros(N)
for e in ev:
    k=e[0]; s=S(k,(e[2]-e[1]) if k=='typing' else None); add(fx,s,e[1],G[k])
    if k in('slam','impact','punch'):  # duck music on hits
        m=int(e[1]*sr); dk=int(.25*sr); mus[m:m+dk]*=np.linspace(0.4,1,len(mus[m:m+dk]))
mix=0.55*norm(mus)+0.95*fx
fade=np.ones(N); fo=int(.6*sr); fade[-fo:]=np.linspace(1,0,fo); mix*=fade
mix=np.tanh(1.6*mix)/np.tanh(1.6)   # soft limiter -> loud & punchy
mix=norm(mix,0.95)
st=np.stack([mix,mix],1)
o=wave.open(sys.argv[3],'w');o.setnchannels(2);o.setsampwidth(2);o.setframerate(sr);o.writeframes((st*32767).astype('<i2').tobytes());o.close()
print('rms',float(np.sqrt((mix**2).mean())))
