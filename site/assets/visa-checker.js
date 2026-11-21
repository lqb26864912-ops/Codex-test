(function(){
  var lang = document.documentElement.lang.indexOf("zh") === 0 ? "zh" : "en";
  var T = lang === "zh" ? {
    q1: "您的年龄？", h1: "养老签通常要求年满 50 岁，选最接近的一项即可。",
    a1: "未满 50 岁", a2: "已满 50 岁",
    q2: "来泰国的主要目的？", h2: "按眼下最主要的目的选一项。",
    p1: "旅游、探亲或短期停留", p2: "长期居住或养老", p3: "远程办公或数字游民（DTV）",
    p4: "在泰国工作（受雇于泰国公司）", p5: "商务考察、开会或短期商务", p6: "读书或语言学校",
    q3: "打算停留多久？", h3: "按目前的计划选，以后有变化可以再问。",
    d1: "60 天以内", d2: "几个月", d3: "一年以上或长期",
    q4: "会在泰国本地工作吗？", h4: "指受雇于泰国公司、在泰国境内工作。远程为海外雇主做事，通常不算本地工作。",
    w1: "不会在泰国本地工作", w2: "会，已有或准备找泰国雇主", w3: "只做远程，雇主不在泰国",
    step: function(i,n){return "第 "+i+" 题，共 "+n+" 题";},
    next: "下一步", see: "查看建议", back: "上一步",
    resultTitle: "根据你的选择，可以先了解这些方向",
    resultHelp: "这是根据 4 个问题给出的初步方向，帮助你选择下一步要了解的签证类型。具体条件和材料再一对一核对。",
    primary: "初步建议", also: "也可以了解",
    comply: "网上声称能保证结果或「交钱疏通」的，都不要相信。",
    waBtn: "用结果咨询 WhatsApp", tgBtn: "打开 Telegram", reset: "重新选择",
    waMsg: function(s){return "你好 Kevin，我刚用了网站上的「我该办哪种泰国签证」工具，初步建议是："+s+"。想咨询适用条件和需要准备的材料。";},
    recs: {
      tourist: { name: "免签停留或旅游签", page: "../extensions.html#visa-exempt", pageLabel: "免签延期", text: "短期旅游或探亲，多数旅客先走免签停留或旅游签。入境时要说得清行程，建议随身准备回程或离境机票、酒店或住处、大致行程和足够旅费，被问话时如实回答。网上说交钱就能过关的，不要相信。" },
      extend: { name: "续签或延期协助", page: "../extensions.html", pageLabel: "续签协助", text: "如果已经在泰国，且停留期快到，可以先核对签证类型和到期日，再看是否适合办理续签或延期。材料要求和是否需要本人到场，按移民局规定一对一确认。" },
      retirement: { name: "养老签", page: "../retirement.html", pageLabel: "了解养老签", text: "年满 50 岁、打算长期在泰国生活且不在本地工作的，可以优先了解养老签。首次办理和续签都要核对财务或收入证明、住址登记等材料。符合条件时，续签也可以咨询本人不到场的办理方式。" },
      dtv: { name: "DTV（Destination Thailand Visa）", page: "../dtv.html", pageLabel: "了解 DTV", text: "远程办公、数字游民，或雇主不在泰国、本人要较长时间居留的，可以了解 DTV。适用条件和材料会调整，需要按你的工作和停留计划一对一核对，不要自行假设一定符合。" },
      elite: { name: "精英签（Thailand Privilege）", page: "../elite.html", pageLabel: "了解精英签", text: "希望较长年限、配套服务更完整的长期停留，可以了解精英签。这是会员项目，官方套餐和会员费以官方公布为准。我们协助咨询与办理，但不代表官方机构。" },
      workv: { name: "工作签", page: "../work.html", pageLabel: "了解工作签", text: "要在泰国本地受雇工作，通常需要工作签及相应工作许可。须为真实雇佣关系。已有雇主或还在了解合规雇佣安排的，都可以先咨询；我们会说明材料和限制，审批由主管部门决定。" },
      business: { name: "商务签", page: "../business.html", pageLabel: "了解商务签", text: "短期商务考察、开会或商务访问，可以了解商务签。商务签不等于工作许可，不能用来在泰国本地上班。具体条件和停留期限按个案说明。" },
      student: { name: "学生签", page: "../student.html", pageLabel: "了解学生签", text: "计划在泰国读语言学校或其他课程，可以了解学生签。课程安排、到校要求和材料因学校而异，需要按你的行程一对一确认。" }
    }
  } : {
    q1: "Your age?", h1: "A retirement visa is generally for people aged 50 or over.",
    a1: "Under 50", a2: "50 or over",
    q2: "Main purpose of your stay?", h2: "Choose the option that fits best right now.",
    p1: "Tourism, visiting family, or a short stay", p2: "Long-term living or retirement",
    p3: "Remote work or digital nomad (DTV)", p4: "Working in Thailand for a Thai employer",
    p5: "Business visit or meetings", p6: "Study or language school",
    q3: "How long do you plan to stay?", h3: "Use your current plan; you can ask again if it changes.",
    d1: "Up to 60 days", d2: "A few months", d3: "A year or longer",
    q4: "Will you work locally in Thailand?", h4: "This means employment with a Thai employer in Thailand. Remote work for an overseas employer is usually not local work.",
    w1: "No local work in Thailand", w2: "Yes — I have or will look for a Thai employer", w3: "Remote only, employer is outside Thailand",
    step: function(i,n){return "Question "+i+" of "+n;},
    next: "Next", see: "See suggestions", back: "Back",
    resultTitle: "Based on your answers, start with these options",
    resultHelp: "This is a first-pass suggestion from four questions, so you know which visa type to read about next. We will then check conditions and documents with you.",
    primary: "First suggestion", also: "Also consider",
    comply: "Do not trust anyone who promises approval or claims they can pay to get you through immigration.",
    waBtn: "WhatsApp this result", tgBtn: "Open Telegram", reset: "Start over",
    waMsg: function(s){return "Hello Kevin, I used the visa matcher on your website. The initial suggestion was: "+s+". I would like to ask about eligibility and the documents required.";},
    recs: {
      tourist: { name: "Visa exemption or tourist visa", page: "../extensions.html#visa-exempt", pageLabel: "Visa-exempt extension", text: "For short tourism or family visits, most travellers use visa exemption or a tourist visa. Be ready to explain your plans, and keep return tickets, accommodation, a basic itinerary and sufficient funds with you. Do not pay anyone who claims they can get you through immigration." },
      extend: { name: "Extension assistance", page: "../extensions.html", pageLabel: "Extensions", text: "If you are already in Thailand and your permitted stay is ending, we can review your visa type and expiry date and explain whether an extension may apply. Document requirements and whether you must attend in person depend on immigration rules." },
      retirement: { name: "Retirement visa", page: "../retirement.html", pageLabel: "Retirement visa", text: "If you are 50 or over, plan to live in Thailand long term and will not work locally, a retirement visa is usually the first option to review. First-time applications and renewals require financial or income evidence and address registration. Where the case qualifies, renewal without attending in person can also be discussed." },
      dtv: { name: "DTV (Destination Thailand Visa)", page: "../dtv.html", pageLabel: "DTV page", text: "Remote work, digital-nomad stays, or a longer stay while employed outside Thailand may point to DTV. Conditions and documents change, so we check your work and travel plans with you. Please do not assume you automatically qualify." },
      elite: { name: "Elite visa (Thailand Privilege)", page: "../elite.html", pageLabel: "Elite visa", text: "If you want a longer membership period and the Privilege package benefits, consider the Elite visa. Official packages and membership fees are set by the programme. We help with enquiries and applications; we are not a government body." },
      workv: { name: "Work visa", page: "../work.html", pageLabel: "Work visa", text: "Local employment in Thailand generally requires a work visa and a work permit, and the job must be a genuine employment relationship. We can explain documents and limits if you already have an employer or are exploring a compliant arrangement. Approval is decided by the competent authorities." },
      business: { name: "Business visa", page: "../business.html", pageLabel: "Business visa", text: "For short business visits or meetings, a business visa may be appropriate. It is not a work permit and does not allow local employment. Conditions and length of stay are confirmed case by case." },
      student: { name: "Student visa", page: "../student.html", pageLabel: "Student visa", text: "If you plan to attend a language school or other course in Thailand, a student visa may apply. Attendance and document requirements vary by school and should be confirmed against your plans." }
    }
  };

  var state = { step: 0, age: "", purpose: "", duration: "", work: "" };
  var questions = [
    { key: "age", title: T.q1, help: T.h1, options: [{v:"under50",t:T.a1},{v:"age50",t:T.a2}] },
    { key: "purpose", title: T.q2, help: T.h2, options: [{v:"travel",t:T.p1},{v:"retire",t:T.p2},{v:"remote",t:T.p3},{v:"work",t:T.p4},{v:"business",t:T.p5},{v:"study",t:T.p6}] },
    { key: "duration", title: T.q3, help: T.h3, options: [{v:"short",t:T.d1},{v:"months",t:T.d2},{v:"long",t:T.d3}] },
    { key: "work", title: T.q4, help: T.h4, options: [{v:"no",t:T.w1},{v:"local",t:T.w2},{v:"remote",t:T.w3}] }
  ];

  function pick() {
    var age = state.age, purpose = state.purpose, duration = state.duration, work = state.work;
    var list = [];
    function add(key){ if (list.indexOf(key) === -1) list.push(key); }
    if (work === "local" || purpose === "work") add("workv");
    if (purpose === "study") add("student");
    if (purpose === "business") add("business");
    if (purpose === "remote" || work === "remote") add("dtv");
    if (age === "age50" && work !== "local" && purpose !== "work" && purpose !== "study" && (purpose === "retire" || duration !== "short")) add("retirement");
    if (work !== "local" && purpose !== "work" && purpose !== "study" && (purpose === "retire" || duration === "long")) add("elite");
    if ((purpose === "retire" || duration === "long") && age === "under50" && work !== "local" && purpose !== "study") add("dtv");
    if (purpose === "travel" && duration === "short" && work !== "local") add("tourist");
    if (purpose === "travel" && (duration === "months" || duration === "long") && work !== "local") { add("tourist"); add("extend"); }
    if (age === "age50" && purpose === "travel" && duration === "short") add("retirement");
    if (!list.length) add("tourist");
    if (list[0] === "tourist" && (purpose === "work" || work === "local")) {
      list = list.filter(function(k){ return k !== "tourist"; });
      add("workv");
    }
    return list.slice(0, 3);
  }

  var root = document.getElementById("checker");
  if (!root) return;

  function render() {
    if (state.step >= questions.length) return renderResult();
    var q = questions[state.step];
    var chosen = state[q.key];
    var dots = questions.map(function(_, i){
      var cls = i < state.step ? "is-done" : (i === state.step ? "is-current" : "");
      return '<span class="'+cls+'"></span>';
    }).join("");
    var opts = q.options.map(function(o){
      return '<button type="button" aria-pressed="'+(chosen===o.v?"true":"false")+'" data-v="'+o.v+'">'+o.t+"</button>";
    }).join("");
    var back = state.step > 0 ? '<button type="button" class="btn btn-ghost" id="chk-back">'+T.back+"</button>" : "";
    var nextLabel = state.step === questions.length - 1 ? T.see : T.next;
    root.innerHTML = '<div class="checker-card" id="contact-step"><div class="checker-progress" aria-hidden="true">'+dots+"</div>"+
      '<p class="wizard-status" role="status">'+T.step(state.step+1, questions.length)+"</p>"+
      "<h2>"+q.title+'</h2><p class="q-help">'+q.help+"</p>"+
      '<div class="q-options" role="group" aria-label="'+q.title+'">'+opts+"</div>"+
      '<div class="checker-nav">'+back+'<button type="button" class="btn btn-primary" id="chk-next"'+(chosen?"":" disabled")+">"+nextLabel+' <span aria-hidden="true">→</span></button></div></div>';
    root.querySelectorAll(".q-options button").forEach(function(btn){
      btn.addEventListener("click", function(){
        state[q.key] = btn.getAttribute("data-v");
        render();
      });
    });
    var nb = document.getElementById("chk-next");
    if (nb) nb.addEventListener("click", function(){ if (state[q.key]) { state.step += 1; render(); }});
    var bb = document.getElementById("chk-back");
    if (bb) bb.addEventListener("click", function(){ state.step -= 1; render(); });
  }

  function renderResult(){
    var keys = pick();
    var cards = keys.map(function(k, i){
      var r = T.recs[k];
      var cls = i === 0 ? "result-card primary" : "result-card";
      var label = i === 0 ? T.primary : T.also;
      return '<div class="'+cls+'"><span class="result-label">'+label+"</span><h3>"+r.name+"</h3><p>"+r.text+'</p><a class="text-link" href="'+r.page+'">'+r.pageLabel+' <span aria-hidden="true">→</span></a></div>';
    }).join("");
    var summary = keys.map(function(k){ return T.recs[k].name; }).join(lang === "zh" ? "、" : ", ");
    var wa = "https://wa.me/66987390634?text="+encodeURIComponent(T.waMsg(summary));
    root.innerHTML = '<div class="checker-card" id="contact-step"><h2>'+T.resultTitle+"</h2><p class=\"q-help\">"+T.resultHelp+'</p><div class="result-block">'+cards+"</div>"+
      '<div class="compliance" style="margin-top:22px">'+T.comply+"</div>"+
      '<div class="hero-actions" style="justify-content:flex-start;margin-top:22px">'+
      '<a class="btn btn-wa" href="'+wa+'" target="_blank" rel="noopener noreferrer">'+T.waBtn+' <span aria-hidden="true">↗</span></a>'+
      '<button type="button" class="btn btn-wx" data-copy-wechat aria-label="'+(lang==="zh"?"复制微信号 Qwe137946a":"Copy WeChat ID Qwe137946a")+'">'+(lang==="zh"?"微信：Qwe137946a":"WeChat: Qwe137946a")+' <small data-wx-status>'+(lang==="zh"?"点击复制":"Tap to copy")+"</small></button>"+
      '<a class="btn btn-tg" href="https://t.me/Taiguo911" target="_blank" rel="noopener noreferrer">'+T.tgBtn+' <span aria-hidden="true">↗</span></a>'+
      '<button type="button" class="btn btn-ghost" id="chk-reset">'+T.reset+"</button></div></div>";
    document.getElementById("chk-reset").addEventListener("click", function(){
      state = { step: 0, age: "", purpose: "", duration: "", work: "" };
      render();
    });
  }
  render();
})();
