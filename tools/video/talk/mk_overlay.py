import json
tl = json.load(open('timeline.json'))
T = lambda txt: next(b[2] for b in tl if b[1] == txt)
sec_start = lambda s: next(b[2] for b in tl if b[0] == s)
DUR = 91.15
top = [
 (0, sec_start('why'), '<div class="big">去泰国谈生意<br><span class="glow">商务签要准备哪些材料？</span></div>'),
 (sec_start('why'), T('但中国驻泰国大使馆九月份提醒过'), '<div class="big">免签能来<br><span class="glow">谈生意吗？</span></div>'),
 (T('但中国驻泰国大使馆九月份提醒过'), sec_start('p1'), '<div class="news"><div class="top"><span class="ntag">政策</span><span class="src">中国驻泰国大使馆</span><span class="date">2026-09-02</span></div><div class="body"><div class="hl">免签单次停留不超过 30 天</div><div class="q">工作等活动、或停留超过 30 天<br>须在入境前办妥签证</div></div></div>'),
 (sec_start('p1'), sec_start('p2'), '<div class="pill">材料分 3 部分</div><div class="big">① <span class="glow">申请人本人</span></div>'),
 (sec_start('p2'), sec_start('p3'), '<div class="pill">最关键</div><div class="big">② <span class="glow">泰国邀请公司</span></div>'),
 (sec_start('p3'), sec_start('warn'), '<div class="pill">材料分 3 部分</div><div class="big">③ <span class="glow">国内任职公司</span></div>'),
 (sec_start('warn'), sec_start('outro'), '<div class="big">最后提醒<br><span class="glow">两点</span></div>'),
 (sec_start('outro'), DUR, '<div class="big">材料多、怕出错？<br><span class="glow">先帮你逐项核对</span></div>'),
]
chips = [
 (T('护照，有效期要 6 个月以上'), sec_start('p2'), '护照（6 个月以上）', 0),
 (T('还有身份证复印件和电子证件照'), sec_start('p2'), '身份证复印件', 0),
 (T('还有身份证复印件和电子证件照') + 0.6, sec_start('p2'), '电子证件照', 0),
 (T('首先是邀请函'), sec_start('p3'), '邀请函（信纸·盖章·签字）', 0),
 (T('手写的不行'), sec_start('p3'), '手写无效', 1),
 (T('另外还要这家公司的营业执照'), sec_start('p3'), '营业执照', 0),
 (T('股东名单和税务单据'), sec_start('p3'), '股东名单', 0),
 (T('股东名单和税务单据') + 0.6, sec_start('p3'), '税务单据', 0),
 (T('英文的在职证明'), sec_start('warn'), '英文在职证明', 0),
 (T('还有营业执照复印件'), sec_start('warn'), '营业执照复印件', 0),
 (T('第一，商务签不等于工作许可'), sec_start('outro'), '商务签 ≠ 工作许可', 1),
 (T('第二，每个使馆的要求不完全一样'), sec_start('outro'), '以使馆最新要求为准', 0),
 (T('可以私信我'), DUR, '有问题，私信我们', 2),
]
data = dict(dur=DUR, subs=[[b[1], b[2], b[3]] for b in tl], top=top, chips=chips)
html = open('overlay_tpl.html', encoding='utf-8').read().replace('__DATA__', json.dumps(data, ensure_ascii=False))
open('overlay.html', 'w', encoding='utf-8').write(html)
print('ok')
