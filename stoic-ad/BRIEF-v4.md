# Round 4 — NEW CONCEPT for BOTH ads (overrides every earlier brief)

The client changed the idea. Reference he sent (screen recording of a TikTok launch film): dark ground,
glowing type that blurs in ("Machine Speed" → "Introducing" → logo), glass cards linked by glowing lines,
"Built for the people who build", a tilted 3D CTA card. Its sound is pure SOUND DESIGN — no narrator:
whooshes, risers, UI clicks, glassy hits, bass impacts on every move. Contact sheet:
/tmp/claude-0/-home-user-Stoic-demos/41feed11-e3a8-5582-9ab2-b65b34088184/scratchpad/ref3/sheet.jpg
Use it for the FEEL (premium, smooth, sound-led), not to copy its look. Your visual language stays your own.

## Hard rules (client feedback)
- NO VOICEOVER. No narrator at all. Sound design only (sfx on every move, rotate takes, layered hits).
  Do NOT use the Kokoro TTS. The previous voice "didn't follow the rhythm of the video" — rhythm is everything now:
  cut and land every move on a steady pulse (pick a BPM, e.g. 120 → 15 frames per beat; place every hit on the grid).
- FULL FRAME. No black half / empty bottom band. Every frame uses the whole 1080×1920 canvas (the TikTok UI will
  overlay the bottom; put decoration there, keep words inside y 168–1330).
- Smooth, blurred transitions between beats (blur-swap, whip with motion blur, push-through). Nothing jumpy.
- Length 18–24 s, 9:16 1080×1920, 30 fps.
- Music: the client adds it in-app. Leave headroom: mix the sfx to about -16 LUFS integrated, true peak ≤ -1 dBTP.

## Structure (client's own words, same for both ads)
1. WHAT WE DO, at its finest — e.g. "Motion design. At its finest." / "Web design. At its finest."
2. THE ADVANTAGES — 4 words/phrases, each blurring smoothly into the next. Use stronger, more seductive words
   than the client's draft:
     - motion: smooth / simple / premium / animated  → e.g. "Buttery smooth." "Effortlessly simple." "Unmistakably premium." "Alive in every frame."
     - websites: 3D / own domain / animated / smooth / premium / professional → e.g. "Built in 3D." "Your own .com." "Silky motion." "Boardroom-grade."
   (Write your own — better than these.)
3. "WE DON'T DO WHAT OTHERS DO" — 4 examples of how others are weak, POPPED UP AS TABS (browser tabs / windows /
   notification cards stacking up fast, each with its weakness: e.g. websites: "Loads in 9 s", "Same template as 1,000 others",
   "Breaks on mobile", "yourname.freebuilder.site"; motion: "Choppy", "Clip-art", "Copy-paste templates", "Flat & lifeless").
   Make them look deliberately cheap/ugly next to our style, then dismiss them all in one satisfying move.
4. THEN WE DO OUR PART — our version, premium, the showpiece of the film:
   - websites: the real demo sites in 3D on laptop + phone together (assets in /home/user/Stoic-demos/stoic-ad/site-shots/:
     cafe, clinic, realestate, garage, nursery — <name>-laptop.png, -laptop-full.jpg, -phone.png, -phone-full.jpg).
   - motion: a dazzling 3–5 s piece of pure motion craft (logo build, kinetic type, 3D object, morphs).
5. CTA — "Want to work with us? DM us." + "Don't miss the November deal." with the deal on the card:
   - websites: "$500 website — was $1,200 · November only"   · Stoic Agency · WhatsApp +971 54 557 2646
   - motion: "$300 per animated ad · first 5 clients · November" · Abdelrahman — Motion Designer · WhatsApp +971 54 557 2646

## Sound
Bundled sfx: /root/.npm/_npx/702923228c2ce1e6/node_modules/hyperframes/dist/skills/media-use/audio/assets/sfx/
(whoosh, whoosh-short, whoosh-cinematic, click, click-soft, key-press, typing, pop, sparkle, riser, impact-bass-1/2,
glitch-1..3, chime, ping, notification, error). "error"/"notification"/"glitch" suit the cheap tabs popping up.
You may build layered hits by combining files (ffmpeg: pitch/speed variants via asetrate/atempo, reverse for
reverse-swells, short reverb tails via aecho) — keep every sound caused by something on screen.
