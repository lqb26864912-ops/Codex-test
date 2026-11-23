import json, re
# spoken script, grouped by section; each string = one subtitle line
SECTIONS = [
 ('intro', ['去泰国谈生意、考察、开会', '商务签到底要准备哪些材料？', '我一次给你讲清楚']),
 ('why', ['很多人以为免签就能来谈生意', '但中国驻泰国大使馆九月份提醒过', '免签单次最多只能待 30 天', '要来工作，或者待超过 30 天', '入境前就得办好签证', '所以行程长、要经常来泰国的', '建议直接办商务签']),
 ('p1', ['材料分三部分', '第一部分，是你自己的', '护照，有效期要 6 个月以上', '还有身份证复印件和电子证件照']),
 ('p2', ['第二部分最关键，是泰国邀请公司的', '首先是邀请函', '要打印在公司的信纸上', '写清楚你是谁、来干什么', '什么时候来、什么时候走', '还要盖章、有授权人签字', '手写的不行', '另外还要这家公司的营业执照', '股东名单和税务单据']),
 ('p3', ['第三部分，是你国内公司的', '英文的在职证明', '还有营业执照复印件']),
 ('warn', ['最后提醒两点', '第一，商务签不等于工作许可', '在泰国上班，还要另外办工作许可', '第二，每个使馆的要求不完全一样', '递交前一定要按最新要求核对一遍']),
 ('outro', ['我们公司在曼谷', '平时就是帮客户办这些签证的', '材料多、怕出错的话', '可以私信我', '先帮你把材料逐项核对一遍']),
]
pauses = "1.04-1.29 3.18-3.42 6.34-6.73 8.08-8.36 9.27-9.61 15.02-15.39 17.72-18.01 18.87-19.18 19.26-19.63 23.05-23.31 25.94-26.29 27.82-28.20 29.49-29.85 30.53-30.87 32.13-32.45 35.13-35.49 38.00-38.27 41.62-41.99 43.08-43.42 45.63-45.92 49.07-49.35 50.03-50.41 51.24-51.57 52.95-53.29 54.16-54.45 56.50-56.76 58.68-59.04 61.06-61.41 62.79-63.00 64.57-64.78 65.93-66.23 66.62-66.84 68.86-69.07 72.06-72.44 76.53-76.73 78.19-78.56 79.27-79.48 81.27-81.64 82.96-83.26 85.53-85.81 87.25-87.51 88.39-88.73"
P = [tuple(map(float, p.split('-'))) for p in pauses.split()]
START, END = 0.0, 91.15
# speech intervals
segs = []; t = START
for a, b in P:
    segs.append((t, a)); t = b
segs.append((t, END))
speech = sum(b - a for a, b in segs)
def speech_to_time(x):  # x seconds of speech -> clock time
    for a, b in segs:
        if x <= b - a: return a + x
        x -= b - a
    return END
lines = [(sec, l) for sec, ls in SECTIONS for l in ls]
w = lambda s: len(re.sub(r'[，。？、：\s]', '', s)) + 0.0
total = sum(w(l) for _, l in lines)
bounds = []; acc = 0
for sec, l in lines:
    st = speech_to_time(acc / total * speech); acc += w(l); en = speech_to_time(acc / total * speech)
    bounds.append([sec, l, st, en])
# snap boundaries to nearest pause midpoint within 0.9 s
mids = [(a + b) / 2 for a, b in P]
for i in range(len(bounds) - 1):
    e = bounds[i][3]; m = min(mids, key=lambda x: abs(x - e))
    if abs(m - e) < 0.9: bounds[i][3] = m; bounds[i + 1][2] = m
print('speech %.1fs chars %d rate %.2f/s' % (speech, total, total / speech))
for b in bounds: print('%-6s %6.2f %6.2f  %s' % (b[0], b[2], b[3], b[1]))
json.dump(bounds, open('timeline.json', 'w'), ensure_ascii=False)
