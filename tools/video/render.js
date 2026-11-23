// usage: node render.js preview [page.html] [t1,t2,...]  -> key frames only
//        node render.js full    [page.html]               -> all frames (30 fps, 15 s) into frames-<page>/
const {chromium} = require('playwright');
const path = require('path');
const fs = require('fs');
const DIR = __dirname;
const FPS = 30;
(async () => {
  const mode = process.argv[2] || 'preview';
  const page = process.argv[3] || 'elite.html';
  const name = page.replace(/\.html$/, '');
  const keys = (process.argv[4] || '1.8,6.6,10.9,14.2').split(',').map(Number);
  const b = await chromium.launch();
  const p = await b.newPage({viewport: {width: 1080, height: 1920}, deviceScaleFactor: 1});
  await p.goto('file://' + path.join(DIR, page));
  const setT = t => p.evaluate(ms => { for (const a of document.getAnimations()) { a.pause(); a.currentTime = ms; } }, t * 1000);
  // touch every scene so all font subsets are requested, then wait for fonts
  for (const t of keys) { await setT(t); await p.waitForTimeout(150); }
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(800);
  // pages that need measured layout (e.g. chat scrolling) build their animations after fonts are ready
  await p.evaluate(() => { if (window.build) window.build(); });
  const DUR = await p.evaluate(() => window.DURATION || 15);
  const ok = await p.evaluate(() => document.fonts.check('700 60px "Noto Sans SC"', document.body.innerText.replace(/\s+/g, '')));
  console.log('fonts loaded for all page text:', ok);
  if (mode === 'preview') {
    for (const t of keys) { await setT(t); await p.screenshot({path: path.join(DIR, `prev-${name}-${t}.png`)}); }
  } else {
    const out = path.join(DIR, 'frames-' + name); fs.mkdirSync(out, {recursive: true});
    for (let i = 0; i < FPS * DUR; i++) {
      await setT(i / FPS);
      await p.screenshot({path: path.join(out, String(i).padStart(4, '0') + '.png')});
    }
    console.log('frames:', FPS * DUR, 'duration:', DUR);
  }
  await b.close();
})();
