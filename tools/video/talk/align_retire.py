import json, re
SECTIONS = [
 ('intro', ['想在泰国养老', '养老签有三条路', '我一分钟给你讲清楚']),
 ('cond', ['先说条件：年满五十岁就可以申请']),
 ('r1', ['第一条路，存款', '在泰国银行账户里，存够八十万泰铢']),
 ('r2', ['第二条路，收入', '每个月有六万五千泰铢以上的收入', '要能开出收入证明']),
 ('r3', ['第三条路，存款加收入', '两样加起来', '一年合计达到八十万泰铢']),
 ('rule', ['养老签一次办一年', '之后每年在泰国续签', '住满九十天，还要做九十天报到']),
 ('nowork', ['提醒一句，养老签不能在泰国工作']),
 ('fund', ['还有，资金证明一定要是真实的', '有人说可以帮你借钱存进去、开证明', '被查出来，签证可能被拒，甚至取消', '以后再办也会受影响']),
 ('outro', ['你更适合哪一条路？', '不确定的话，可以私信我', '我们公司在曼谷，帮你一对一看看']),
]
pauses = "3.73-4.02 4.34-4.55 6.13-6.32 7.41-7.62 10.21-10.53 16.17-16.44 21.50-21.87 22.97-23.19 28.69-28.98 30.53-30.75 31.79-31.98 33.30-33.51 38.28-38.47 39.00-39.39 42.96-43.24"
P = [tuple(map(float, p.split('-'))) for p in pauses.split()]
START, END = 0.0, 46.4
segs = []; t = START
for a, b in P: segs.append((t, a)); t = b
segs.append((t, END))
speech = sum(b - a for a, b in segs)
def s2t(x):
    for a, b in segs:
        if x <= b - a: return a + x
        x -= b - a
    return END
lines = [(s, l) for s, ls in SECTIONS for l in ls]
w = lambda s: len(re.sub(r'[，。：？、\s]', '', s))
total = sum(w(l) for _, l in lines)
out = []; acc = 0
for s, l in lines:
    st = s2t(acc / total * speech); acc += w(l); out.append([s, l, st, s2t(acc / total * speech)])
mids = [(a + b) / 2 for a, b in P]
for i in range(len(out) - 1):
    e = out[i][3]; m = min(mids, key=lambda x: abs(x - e))
    if abs(m - e) < 0.8: out[i][3] = m; out[i + 1][2] = m
print('rate %.2f chars/s' % (total / speech))
for o in out: print('%-6s %5.2f %5.2f %s' % (o[0], o[2], o[3], o[1]))
json.dump(out, open('timeline.json', 'w'), ensure_ascii=False)
