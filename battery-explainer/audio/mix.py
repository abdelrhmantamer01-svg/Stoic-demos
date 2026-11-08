import numpy as np, soundfile as sf, json, subprocess
SR = 48000; DUR = 44.0; N = int(SR*DUR); rng = np.random.default_rng(3)
t = np.arange(N)/SR
def env(a, b, atk=.01, rel=.3):
    e = np.zeros(N); i0, i1 = int(a*SR), min(N, int(b*SR)); x = t[i0:i1]-a; L = b-a
    e[i0:i1] = np.minimum(1, x/atk) * np.clip((L-x)/rel, 0, 1); return e
def lp(x, k):  # one-pole lowpass
    y = np.empty_like(x); acc = 0.
    for i in range(0, len(x), 4096):
        seg = x[i:i+4096]; out = np.empty_like(seg)
        for j, v in enumerate(seg): acc += k*(v-acc); out[j] = acc
        y[i:i+4096] = out
    return y
noise = rng.standard_normal(N)
# ambient pad: low fifths with slow movement, fades in/out
pad = (np.sin(2*np.pi*55*t) + .6*np.sin(2*np.pi*82.4*t + .3) + .35*np.sin(2*np.pi*110.2*t)*(.5+.5*np.sin(2*np.pi*.07*t)))
pad *= .055 * np.clip(t/3, 0, 1) * np.clip((DUR-t)/2.5, 0, 1)
air = lp(noise, .02) * .05 * np.clip(t/3,0,1) * np.clip((DUR-t)/2.5,0,1)
fx = np.zeros(N)
# riser before shatter + impact
r = env(2.6, 4.56, atk=1.9, rel=.02); fx += lp(noise, .08) * r * .35
i = int(4.55*SR); x = t[i:]-4.55
fx[i:] += (np.sin(2*np.pi*(48*np.exp(-x*1.5)+30)*x) * np.exp(-x*2.2) * .9)[:N-i]
fx[i:] += (noise[i:] * np.exp(-x*9) * .35)
for k in range(28):  # glassy shard tinkles
    s = 4.6 + rng.random()*1.6; f = 2400 + rng.random()*3500; j = int(s*SR); y = np.arange(int(.35*SR))/SR
    seg = np.sin(2*np.pi*f*y) * np.exp(-y*18) * .05; fx[j:j+len(seg)] += seg[:N-j]
# whooshes (filtered noise swell) at transitions
for a, b in [(8.9, 9.9), (23.7, 24.5), (28.1, 28.9), (39.6, 40.6)]:
    e = env(a, b, atk=(b-a)*.7, rel=(b-a)*.3); fx += lp(noise, .15) * e * .5
# plug click + charging chime
j = int(26.62*SR); y = np.arange(int(1.6*SR))/SR
click = (rng.standard_normal(len(y)) * np.exp(-y*120) * .6 + np.sin(2*np.pi*90*y)*np.exp(-y*14)*.5)
chime = (np.sin(2*np.pi*880*y) + .7*np.sin(2*np.pi*1318.5*np.maximum(y-.12,0))*(y>.12)) * np.exp(-y*3.2) * .12
fx[j:j+len(y)] += (click + chime)[:N-j]
# end swell
fx += np.sin(2*np.pi*65.4*t) * env(40.2, 44, atk=1.2, rel=2.5) * .12
# voice
vo = np.zeros(N)
for a, b, f, d in json.load(open('am_onyx.json')):
    subprocess.run(['ffmpeg','-loglevel','error','-y','-i',f,'-af','asetrate=24000*0.95,aresample=48000,atempo=1.0526,bass=g=3:f=110,acompressor=threshold=-20dB:ratio=3:attack=5:release=80','-ar','48000','-ac','1','v.wav'], check=True)
    v, _ = sf.read('v.wav'); v = v/np.max(np.abs(v))*.8; j = int(a*SR); vo[j:j+len(v)] += v[:N-j]
mix = vo + pad + air + fx*.55
mix = np.tanh(mix*1.1)*.9
sf.write('soundtrack.wav', np.stack([mix, mix], 1), SR)
print('peak', np.abs(mix).max())
