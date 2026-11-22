// usage: node render.js preview   -> key frames only
//        node render.js full      -> all frames (30 fps, 15 s)
const {chromium} = require('playwright');
const path = require('path');
const fs = require('fs');
const DIR = __dirname;
const FPS = 30, DUR = 15;
(async () => {
  const mode = process.argv[2] || 'preview';
  const b = await chromium.launch();
  const p = await b.newPage({viewport: {width: 1080, height: 1920}, deviceScaleFactor: 1});
  await p.goto('file://' + path.join(DIR, 'elite.html'));
  const setT = t => p.evaluate(ms => { for (const a of document.getAnimations()) { a.pause(); a.currentTime = ms; } }, t * 1000);
  // touch every scene so all font subsets are requested, then wait for fonts
  for (const t of [1.8, 6.6, 10.9, 14.2]) { await setT(t); await p.waitForTimeout(150); }
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(800);
  const ok = await p.evaluate(() => ['想在泰国长期生活', '精英签会员费', '五种套餐怎么选', '曼谷注册中文咨询'].map(s => document.fonts.check('900 60px "Noto Sans SC"', s)));
  console.log('fonts loaded:', ok.join(','));
  if (mode === 'preview') {
    for (const t of [1.8, 6.6, 10.9, 14.2]) { await setT(t); await p.screenshot({path: path.join(DIR, `prev-${t}.png`)}); }
  } else {
    const out = path.join(DIR, 'frames'); fs.mkdirSync(out, {recursive: true});
    for (let i = 0; i < FPS * DUR; i++) {
      await setT(i / FPS);
      await p.screenshot({path: path.join(out, String(i).padStart(4, '0') + '.png')});
    }
    console.log('frames:', FPS * DUR);
  }
  await b.close();
})();
