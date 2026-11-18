---
name: lenis
description: Smooth, inertial scrolling for websites with Lenis (darkroomengineering, MIT). Use when building or fixing a website's scroll feel, syncing scroll with GSAP ScrollTrigger, anchor links, scroll-snap, or Lenis in React/Next.js/Vue/Nuxt.
---

# Lenis smooth scroll

Read `references/README.md` first (install, options, methods, events, GSAP ScrollTrigger sync, troubleshooting). Then by stack: `references/react.md`, `references/vue.md`; for snapping `references/snap.md`; all options and types in `references/types.ts`. Always include `references/lenis.css` (or `lenis/dist/lenis.css`).

Rules that matter most:
- Never combine Lenis with CSS `scroll-behavior: smooth`.
- With GSAP ScrollTrigger: `lenis.on('scroll', ScrollTrigger.update)` and drive Lenis from `gsap.ticker` (`gsap.ticker.add((t) => lenis.raf(t * 1000)); gsap.ticker.lagSmoothing(0);`), with `autoRaf: false`.
- Nested scrollable areas (modals, code blocks) need `data-lenis-prevent`.
- Respect `prefers-reduced-motion`: don't start Lenis (or set `lerp: 1`) when the user asks for reduced motion.
- Not for HyperFrames video renders (those are seeked frame by frame, not scrolled); use it in real websites.
