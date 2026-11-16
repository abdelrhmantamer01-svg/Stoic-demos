---
name: claude-animation-base
description: Make hand-drawn style animated videos of the Clawd character (or a swapped-in character) using p5.js + p5.brush, rendered headlessly to MP4. Use when the user asks for a character animation, cartoon short, animated music video, or "Claude Animation Base" video.
---

# Claude Animation Base (John Heibel, MIT)

Starter kit, not a library. The files live in this skill's folder.

1. Read `ANIMATION_GUIDE.md` in this folder FIRST — it holds the rules, workflow and full API.
2. Copy this folder (minus SKILL.md) into a working project directory, run `npm install`.
3. Storyboard first, then write the scene in `src/scenes/`, render contact sheets to self-check,
   and finish with `node render.mjs --clip --out=out/video.mp4`.
4. Needs Node.js, Chrome/Chromium and ffmpeg. Without a GPU add `--soft-gl` and prefer to avoid
   p5.brush watercolour fills (very slow on CPU).
