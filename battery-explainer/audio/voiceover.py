import soundfile as sf, json, sys
from kokoro_onnx import Kokoro
k = Kokoro("kokoro-v1.0.onnx", "voices-v1.0.bin")
voice, speed = sys.argv[1], float(sys.argv[2])
L = [
 (0.4, 4.3, "What keeps your laptop alive?"),
 (4.7, 9.4, "It's the battery. Four small cells, packed with energy."),
 (9.9, 14.2, "Inside each cell: two layers. Graphite, and metal oxide."),
 (14.3, 19.2, "When you unplug, lithium ions leave the graphite, and swim across."),
 (19.3, 24.1, "Their electrons take the long way, through your laptop. That's your power."),
 (24.5, 28.5, "Then, you plug in the charger."),
 (28.9, 34.8, "It pushes the ions back into the graphite, and the energy is stored again."),
 (35.0, 39.9, "Every cycle, a few get trapped for good. That's why batteries age."),
 (40.5, 44.0, "That's how a battery works."),
]
out = []
for i,(a,b,txt) in enumerate(L):
    s, sr = k.create(txt, voice=voice, speed=speed, lang="en-us")
    f = f"{voice}_{i}.wav"; sf.write(f, s, sr); out.append((a,b,f,len(s)/sr))
    print(f"{i} window {b-a:.1f}s  speech {len(s)/sr:.2f}s  {'OVER' if len(s)/sr > b-a else ''}")
json.dump(out, open(f"{voice}.json","w"))
