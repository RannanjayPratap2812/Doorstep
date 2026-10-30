"""Generates the alarm ringtones (10 s WAVs) used by the Android/iPhone builds. Run: python3 tools/make_ringtones.py"""
import wave,struct,math,os
T={'chime':(0,[(784,0,.5),(988,.3,.5),(1175,.6,.9)]),'bell':(0,[(660,0,1.2),(1320,0,.8)]),'beep':(1,[(1000,0,.15),(1000,.25,.15),(1000,.5,.15)]),'rise':(0,[(523,0,.25),(659,.25,.25),(784,.5,.25),(1047,.75,.6)]),'pulse':(1,[(880,0,.2),(660,.25,.2),(880,.5,.2),(660,.75,.2)])}
R,L=16000,10
os.makedirs('ringtones',exist_ok=True)
for name,(sq,seq) in T.items():
    buf=[0.0]*(R*L)
    for rep in range(0,L,2):
        for f,st,du in seq:
            for i in range(int(du*R)):
                j=int((rep+st)*R)+i
                if j>=len(buf):break
                t=i/R;env=min(1,t/.01)*math.exp(-4*t/du);v=math.sin(2*math.pi*f*t)
                if sq:v=.5*(1 if v>=0 else -1)
                buf[j]+=v*env*.5
    w=wave.open(f'ringtones/{name}.wav','wb');w.setnchannels(1);w.setsampwidth(2);w.setframerate(R)
    w.writeframes(b''.join(struct.pack('<h',int(max(-1,min(1,x))*32000)) for x in buf));w.close()
