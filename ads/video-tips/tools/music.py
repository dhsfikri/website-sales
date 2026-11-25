import numpy as np, wave, sys
sr=44100;T=15.0;n=int(sr*T);t=np.arange(n)/sr
bpm=96;beat=60/bpm
def note(m):return 440*2**((m-69)/12)
chords=[[57,60,64],[53,57,60],[48,55,64],[55,59,62]]  # Am F C G
out=np.zeros(n)
bar=beat*4
for i in range(int(T/bar)+1):
    c=chords[i%4];st=i*bar
    idx=(t>=st)&(t<st+bar+0.6)
    tt=t[idx]-st
    env=np.minimum(1,tt/0.4)*np.exp(-tt*0.35)
    for m in c:
        f=note(m);out[idx]+=0.12*env*(np.sin(2*np.pi*f*tt)+0.3*np.sin(2*np.pi*2*f*tt)+0.15*np.sin(2*np.pi*f*1.003*tt))
    # bass
    f=note(c[0]-12);out[idx]+=0.18*env*np.sin(2*np.pi*f*tt)
# soft pluck arpeggio on 8ths
for k in range(int(T/(beat/2))):
    st=k*beat/2;c=chords[int(st/bar)%4];m=c[k%3]+12
    idx=(t>=st)&(t<st+0.5);tt=t[idx]-st
    out[idx]+=0.06*np.exp(-tt*9)*np.sin(2*np.pi*note(m)*tt)
# soft kick on beats
for k in range(int(T/beat)):
    st=k*beat;idx=(t>=st)&(t<st+0.25);tt=t[idx]-st
    out[idx]+=0.25*np.exp(-tt*18)*np.sin(2*np.pi*(55+90*np.exp(-tt*30))*tt)
fade=np.ones(n);fi=int(0.3*sr);fo=int(1.2*sr);fade[:fi]=np.linspace(0,1,fi);fade[-fo:]=np.linspace(1,0,fo)
out*=fade
rms=np.sqrt(np.mean(out**2));out*=0.12/rms;out=np.clip(out,-0.95,0.95)
st=np.stack([out,out],1);w=wave.open(sys.argv[1],'w');w.setnchannels(2);w.setsampwidth(2);w.setframerate(sr);w.writeframes((st*32767).astype('<i2').tobytes());w.close()
