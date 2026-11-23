const {chromium}=require('playwright');const path=require('path');const fs=require('fs');
(async()=>{const mode=process.argv[2]||'preview';const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+path.join(__dirname,'overlay.html'));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(800);
const setT=t=>p.evaluate(ms=>{for(const a of document.getAnimations()){a.pause();a.currentTime=ms;}},t*1000);
const DUR=await p.evaluate(()=>window.DURATION);
if(mode==='preview'){for(const t of process.argv[3].split(',').map(Number)){await setT(t);await p.screenshot({path:path.join(__dirname,`ov-${t}.png`),omitBackground:true});}}
else{const out=path.join(__dirname,'ov');fs.mkdirSync(out,{recursive:true});const N=Math.round(DUR*30);
for(let i=0;i<N;i++){await setT(i/30);await p.screenshot({path:path.join(out,String(i).padStart(4,'0')+'.png'),omitBackground:true});}console.log('frames',N);}
await b.close();})();
