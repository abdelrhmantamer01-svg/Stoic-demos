// Renders index.html frame-by-frame into an MP4.
// usage: node render.mjs [out.mp4] [fps] [onlyTimesCommaSeparated]
import { createRequire } from 'node:module'; const { chromium } = createRequire(import.meta.url)('playwright');
import http from 'node:http'; import fs from 'node:fs'; import path from 'node:path'; import { spawn } from 'node:child_process';
const root = path.dirname(new URL(import.meta.url).pathname);
const out = process.argv[2] || 'battery-explainer.mp4', fps = +(process.argv[3] || 30), only = process.argv[4];
const types = { '.html':'text/html', '.js':'text/javascript' };
const srv = http.createServer((q, r) => { const f = path.join(root, decodeURIComponent(q.url.split('?')[0])); fs.readFile(f, (e, d) => { if (e) { r.writeHead(404); return r.end(); } r.writeHead(200, { 'content-type': types[path.extname(f)] || 'application/octet-stream' }); r.end(d); }); }).listen(0);
const port = srv.address().port;
const browser = await chromium.launch({ args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
page.on('console', m => console.log('page:', m.text())); page.on('pageerror', e => console.log('ERR', e.message));
await page.goto(`http://localhost:${port}/index.html?record`); await page.waitForFunction('window.ready === true'); await page.evaluate('document.fonts.ready');
const stage = await page.$('#stage');
if (only) { for (const t of only.split(',')) { await page.evaluate(x => window.renderAt(x), +t); await stage.screenshot({ path: `${out}-${t}.jpg`, type: 'jpeg', quality: 85 }); } }
else {
  const dur = await page.evaluate('window.DURATION'), n = Math.round(dur * fps);
  const ff = spawn('ffmpeg', ['-y', '-f', 'image2pipe', '-framerate', String(fps), '-c:v', 'mjpeg', '-i', '-', '-c:v', 'libx264', '-preset', 'slow', '-crf', '18', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', out], { stdio: ['pipe', 'ignore', 'inherit'] });
  const t0 = Date.now();
  for (let i = 0; i < n; i++) { await page.evaluate(x => window.renderAt(x), i / fps); const buf = await stage.screenshot({ type: 'jpeg', quality: 95 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if (i % 60 === 0) console.log(`frame ${i}/${n}  ${((Date.now() - t0) / 1000).toFixed(0)}s`); }
  ff.stdin.end(); await new Promise(r => ff.on('close', r));
}
await browser.close(); srv.close();
