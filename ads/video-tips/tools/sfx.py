import numpy as np, json, wave, sys
sr=44100; T=12.0; N=int(sr*T)
rng=np.random.default_rng(7)
def env(n,a,d): t=np.arange(n)/sr; return np.minimum(1,t/max(a,1e-4))*np.exp(-t/d)
def noise(n): return rng.standard_normal(n)
def lp(x,k): # simple moving average lowpass
    k=max(1,int(k)); return np.convolve(x,np.ones(k)/k,'same')
def sweep(n,f0,f1):
    t=np.arange(n)/sr; f=f0*(f1/f0)**(t/(n/sr)); return np.sin(2*np.pi*np.cumsum(f)/sr)
def snd(kind,dur=None):
    if kind=='slam':
        n=int(.25*sr); x=0.9*sweep(n,120,45)*env(n,.002,.07)+0.35*lp(noise(n),3)*env(n,.001,.03); return x
    if kind=='punch':
        n=int(.6*sr); return 1.0*sweep(n,90,35)*env(n,.003,.18)+0.25*lp(noise(n),6)*env(n,.001,.05)
    if kind in('whoosh','swoosh'):
        L=.4 if kind=='whoosh' else .25; n=int(L*sr); t=np.arange(n)/n
        x=noise(n); w=np.sin(np.pi*t)**2
        lo=lp(x,40); hi=x-lp(x,6); x=(lo*(1-t)+hi*t*0.6)*w; return 0.7*x/np.max(np.abs(x))
    if kind=='pop':
        n=int(.12*sr); return 0.55*sweep(n,700,1500)*env(n,.002,.03)
    if kind=='tick':
        n=int(.05*sr); return 0.3*lp(noise(n),2)*env(n,.0005,.008)
    if kind=='impact':
        n=int(.9*sr); return 1.0*sweep(n,110,38)*env(n,.002,.25)+0.4*lp(noise(n),4)*env(n,.001,.06)+0.25*np.sin(2*np.pi*55*np.arange(n)/sr)*env(n,.01,.4)
    if kind=='ding':
        n=int(1.2*sr); t=np.arange(n)/sr; e=env(n,.002,.35)
        return 0.35*(np.sin(2*np.pi*1568*t)+0.5*np.sin(2*np.pi*2352*t)+0.25*np.sin(2*np.pi*3136*t))*e
    if kind=='click':
        n=int(.06*sr); return 0.5*sweep(n,2000,1200)*env(n,.0005,.012)
    if kind=='typing':
        n=int(dur*sr); x=np.zeros(n); step=int(sr/11)
        for i in range(0,n-int(.03*sr),step):
            m=int(.03*sr); x[i:i+m]+=0.18*lp(noise(m),2)*env(m,.0005,.006)
        return x
    return np.zeros(1)
ev=json.load(open(sys.argv[1]))[sys.argv[2]]
out=np.zeros(N)
for e in ev:
    k=e[0]; t0=e[1]; s=snd(k, (e[2]-e[1]) if k=='typing' else None)
    i=int(t0*sr); j=min(N,i+len(s)); out[i:j]+=s[:j-i]
# music
w=wave.open(sys.argv[3]); m=np.frombuffer(w.readframes(w.getnframes()),dtype='<i2').reshape(-1,2)[:,0]/32767.0
m=m[:N]; m=np.pad(m,(0,N-len(m)))
fade=np.ones(N); fo=int(.8*sr); fade[-fo:]=np.linspace(1,0,fo)
mix=0.7*m+0.55*out
mix*=fade
mix/=max(1.0,np.max(np.abs(mix))/0.95)
st=np.stack([mix,mix],1)
o=wave.open(sys.argv[4],'w');o.setnchannels(2);o.setsampwidth(2);o.setframerate(sr);o.writeframes((st*32767).astype('<i2').tobytes());o.close()
