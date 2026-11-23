'use strict';
(function(){
  var COPY={zh:{step_status:["第 1 步，共 3 步","第 2 步，共 3 步","第 3 步，共 3 步"],validation:"地区最多 60 个字符，问题最多 350 个字符，请缩短后继续。",greeting:"你好 Kevin，我想咨询：",region_prefix:"目前所在地区：",time_prefix:"我的计划时间：",question_prefix:"想问的问题：",default_question:"想先了解适用条件、所需材料与服务范围。",closing:"请说明所需材料、官方费用和服务费用。",prepared:"草稿已生成，尚未发送。",copied:"已复制，粘贴后自行发送。",copy_fallback:"浏览器未允许自动复制。文本已选中，请长按或使用复制快捷键。"},en:{step_status:["Step 1 of 3","Step 2 of 3","Step 3 of 3"],validation:"Location can be up to 60 characters and the question up to 350. Please shorten it to continue.",greeting:"Hello Kevin, I would like to ask about: ",region_prefix:"Current location: ",time_prefix:"My planned timing: ",question_prefix:"My question: ",default_question:"I would first like to understand the eligibility, required documents and scope of service.",closing:"Please let me know the documents required, the official fees and your service fee.",prepared:"Draft ready. Nothing has been sent.",copied:"Copied. Paste it into the chat and send it yourself.",copy_fallback:"Your browser did not allow automatic copying. The text is selected; long-press or use your copy shortcut."},th:{step_status:["ขั้นตอนที่ 1 จาก 3","ขั้นตอนที่ 2 จาก 3","ขั้นตอนที่ 3 จาก 3"],validation:"พื้นที่ยาวได้ไม่เกิน 60 ตัวอักษร และคำถามไม่เกิน 350 ตัวอักษร กรุณาย่อให้สั้นลงเพื่อดำเนินการต่อ",greeting:"สวัสดีครับ Kevin ขอสอบถามเรื่อง: ",region_prefix:"พื้นที่ปัจจุบัน: ",time_prefix:"ช่วงเวลาที่วางแผน: ",question_prefix:"คำถาม: ",default_question:"อยากทราบเงื่อนไข เอกสารที่ต้องใช้ และขอบเขตบริการก่อน",closing:"รบกวนแจ้งเอกสารที่ต้องใช้ ค่าธรรมเนียมทางราชการ และค่าบริการด้วยครับ",prepared:"สร้างข้อความร่างแล้ว ยังไม่ได้ส่ง",copied:"คัดลอกแล้ว วางในแชทแล้วกดส่งเอง",copy_fallback:"เบราว์เซอร์ไม่อนุญาตให้คัดลอกอัตโนมัติ ข้อความถูกเลือกไว้แล้ว กดค้างหรือใช้คีย์ลัดเพื่อคัดลอก",lb_img:"ภาพขยาย",lb_close:"ปิด"}};
  var pageLang=(document.documentElement.lang||''), copy=pageLang.indexOf('en')===0?COPY.en:pageLang.indexOf('th')===0?COPY.th:COPY.zh;
  var $=function(id){return document.getElementById(id);};

  // Header: scrolled state + mobile menu
  var header=$('site-header'), menuToggle=document.querySelector('.menu-toggle'), mainNav=$('main-nav');
  function onScroll(){header.classList.toggle('scrolled',window.scrollY>8);}
  window.addEventListener('scroll',onScroll,{passive:true});onScroll();
  function closeMenu(){mainNav.classList.remove('is-open');menuToggle.setAttribute('aria-expanded','false');}
  menuToggle.addEventListener('click',function(){var open=menuToggle.getAttribute('aria-expanded')!=='true';menuToggle.setAttribute('aria-expanded',String(open));mainNav.classList.toggle('is-open',open);});
  mainNav.querySelectorAll('a').forEach(function(a){a.addEventListener('click',closeMenu);});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'){var wasOpen=mainNav.classList.contains('is-open');closeMenu();if(wasOpen)menuToggle.focus();}});

  // Scroll reveal
  var reveals=document.querySelectorAll('.reveal');
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(entries){entries.forEach(function(en){if(en.isIntersecting){en.target.classList.add('in');io.unobserve(en.target);}});},{rootMargin:'0px 0px -8% 0px',threshold:.08});
    reveals.forEach(function(el){io.observe(el);});
  } else reveals.forEach(function(el){el.classList.add('in');});

  // Card spotlight hover
  document.querySelectorAll('.card').forEach(function(c){c.addEventListener('pointermove',function(e){var r=c.getBoundingClientRect();c.style.setProperty('--mx',(e.clientX-r.left)+'px');c.style.setProperty('--my',(e.clientY-r.top)+'px');});});

  // Client results gallery: click-to-enlarge lightbox
  var fbLinks=document.querySelectorAll('[data-lightbox]');
  if(fbLinks.length){
    var isEn=copy===COPY.en, lb=document.createElement('div'), lbImg=document.createElement('img'), lbCap=document.createElement('p'), lbClose=document.createElement('button'), lastFocus=null;
    lb.className='fb-lightbox';lb.hidden=true;lb.setAttribute('role','dialog');lb.setAttribute('aria-modal','true');lb.setAttribute('aria-label',copy.lb_img||(isEn?'Enlarged image':'放大图片'));
    lbClose.type='button';lbClose.className='fb-close';lbClose.setAttribute('aria-label',copy.lb_close||(isEn?'Close':'关闭'));lbClose.textContent='×';
    lb.appendChild(lbClose);lb.appendChild(lbImg);lb.appendChild(lbCap);document.body.appendChild(lb);
    var closeLb=function(){lb.hidden=true;document.body.classList.remove('fb-open');lbImg.removeAttribute('src');if(lastFocus)lastFocus.focus();};
    fbLinks.forEach(function(a){a.addEventListener('click',function(e){
      e.preventDefault();lastFocus=a;var img=a.querySelector('img');
      lbImg.src=a.getAttribute('href');lbImg.alt=img?img.alt:'';lbCap.textContent=a.getAttribute('data-caption')||'';
      lb.hidden=false;document.body.classList.add('fb-open');lbClose.focus();
    });});
    lb.addEventListener('click',function(e){if(e.target!==lbImg)closeLb();});
    document.addEventListener('keydown',function(e){if(!lb.hidden&&(e.key==='Escape'||e.key==='Tab')){e.preventDefault();if(e.key==='Escape')closeLb();else lbClose.focus();}});
  }

  // Copy WeChat ID (buttons with data-copy-wechat; some are rendered later, so use delegation)
  var WX_ID='Qwe137946a', WX_MSG={zh:['已复制','请长按复制：'],en:['Copied','Copy this ID: '],th:['คัดลอกแล้ว','คัดลอก ID นี้: ']}[pageLang.slice(0,2)]||['已复制','请长按复制：'];
  document.addEventListener('click',function(e){
    var btn=e.target.closest&&e.target.closest('[data-copy-wechat]');if(!btn)return;
    var label=btn.querySelector('[data-wx-status]'), orig=label?label.getAttribute('data-orig')||label.textContent:'';
    if(label&&!label.getAttribute('data-orig'))label.setAttribute('data-orig',orig);
    function done(){if(label){label.textContent=WX_MSG[0];setTimeout(function(){label.textContent=orig;},2000);}}
    function fallback(){window.prompt(WX_MSG[1],WX_ID);}
    try{
      if(!navigator.clipboard||!navigator.clipboard.writeText)throw new Error('Clipboard unavailable');
      navigator.clipboard.writeText(WX_ID).then(done,fallback);
    }catch(err){fallback();}
  });

  // 3-step inquiry wizard (only on pages that have the form)
  if(!$('inquiry-form'))return;
  var form=$('inquiry-form'), panels=[$('inquiry-step-1'),$('inquiry-step-2'),$('inquiry-result')];
  var progress=[].slice.call(document.querySelectorAll('.wizard-progress li')), progressContainer=document.querySelector('.wizard-progress');
  var interest=$('interest'), locationField=$('location'), timing=$('timing'), question=$('purpose'), output=$('generated-text');
  var status=$('copy-status'), wizardStatus=$('wizard-status'), error=$('wizard-error'), draftLink=$('open-whatsapp-draft');
  var currentStep=1, lastFingerprint='';
  function refreshDraftLink(){draftLink.href='https://wa.me/66987390634?text='+encodeURIComponent(output.value);}
  function showStep(step,focus){
    if(focus===undefined)focus=true;
    currentStep=step;
    panels.forEach(function(p,i){p.hidden=i!==step-1;});
    progress.forEach(function(item,i){if(i===step-1)item.setAttribute('aria-current','step');else item.removeAttribute('aria-current');item.classList.toggle('is-complete',i<step-1);});
    wizardStatus.textContent=copy.step_status[step-1];
    error.textContent='';
    if(focus){[interest,locationField,output][step-1].focus({preventScroll:true});progressContainer.scrollIntoView({behavior:'auto',block:'start'});}
  }
  $('wizard-next').addEventListener('click',function(){showStep(2);});
  $('wizard-back').addEventListener('click',function(){showStep(1);});
  $('wizard-edit').addEventListener('click',function(){showStep(2);});
  document.querySelectorAll('[data-interest]').forEach(function(link){link.addEventListener('click',function(){interest.value=link.dataset.interest;showStep(1,false);});});
  output.addEventListener('input',refreshDraftLink);
  draftLink.addEventListener('click',refreshDraftLink);
  form.addEventListener('submit',function(e){
    e.preventDefault();
    if(currentStep===1){showStep(2);return;}
    var region=locationField.value.trim(), purpose=question.value.trim();
    if(region.length>60||purpose.length>350){error.textContent=copy.validation;(region.length>60?locationField:question).focus();return;}
    var fp=JSON.stringify([interest.value,region,timing.value,purpose]);
    if(fp!==lastFingerprint||!output.value.trim()){
      output.value=[copy.greeting+interest.value,region?copy.region_prefix+region:'',copy.time_prefix+timing.value,purpose?copy.question_prefix+purpose:copy.default_question,copy.closing].filter(Boolean).join('\n');
      lastFingerprint=fp;
    }
    refreshDraftLink();
    status.textContent=copy.prepared;
    showStep(3);
  });
  $('copy-inquiry').addEventListener('click',function(){
    function fallback(){output.focus();output.select();status.textContent=copy.copy_fallback;}
    try{
      if(!navigator.clipboard||!navigator.clipboard.writeText)throw new Error('Clipboard unavailable');
      navigator.clipboard.writeText(output.value).then(function(){status.textContent=copy.copied;},fallback);
    }catch(err){fallback();}
  });
  var def=interest.getAttribute('data-default');if(def){interest.value=def;}
  showStep(1,false);
  // No-JS safety: advance controls stay disabled until script runs.
  $('wizard-next').disabled=false;
  $('generate-inquiry').disabled=false;
})();
