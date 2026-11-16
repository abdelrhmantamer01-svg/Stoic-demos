# Review

Creative calls: one red dot carries the whole film; the voice orders it around. Light flat graphic look, Bebas + Stoic red kept. Storylines B and C (STORYLINES.md) not built.
Client round 2 applied: scenes run 1.15-1.2x faster, VO at Kokoro speed 1.1 with three filler lines so no gap exceeds ~0.9 s, 28.0 s total, price beat added, music slot left commented in index.html.

Measured: `check --json` ok:true (0 errors). Render 1080x1920, 30 fps, 28.0 s. Audio -15.0 LUFS integrated, true peak -1.0 dBTP, no clipping. Sound was measured, not heard.
Looked at: 4 rounds of contact sheets (about 85 frames) plus a 1 fps strip of the final MP4.
Round 1 fixes: empty lower half on bone scenes (added the ink floor from scene 1), pupil escaping the eyelid (clip path), LOUD overshooting into the caption, CTA header overflowing its card, period colliding with the N.
Round 2 fixes: dot hop touching "A DOT.", stray slot ring at the price exit.

Kept warnings: 18 `outside_safe_zone` (the linter's zones are stricter than the brief's 168-1330 band; all text is inside the brief's band and left of x=960 except the cafe poster's own lower copy and timer baseline near 1310); `line_unread` on YOUR BRAND in the price scene (it is the same card carried over from the previous scene, read there for 0.9 s); overlap/contrast at 7.78 s are mid-flip frames.

Weakest shot: the app scene (2.35 s) - the UI is placeholder bars, and it is the least surprising world. With more time: a real client app screen, and hand-drawn motion blur on the whip and flip.
Not checked by anyone: how the voice actually sounds (pronunciation, tone), and sync by ear.
