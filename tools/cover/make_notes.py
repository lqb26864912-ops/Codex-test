"""Render Xiaohongshu image-text notes (cover + inner pages, 1080x1440) from a spec."""
import json, os, subprocess, html
HERE = os.path.dirname(os.path.abspath(__file__))
E = html.escape

CSS = '''*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1440px;overflow:hidden;font-family:"Noto Sans SC",sans-serif;background:#fbf6ef;color:#16130f}
.c{position:absolute;inset:0;padding:100px 90px 90px;display:flex;flex-direction:column}
.tag{align-self:flex-start;font-size:40px;font-weight:900;padding:12px 30px;border-radius:999px;background:#d2402f;color:#fff}
.h1{margin-top:70px;font-size:150px;font-weight:900;line-height:1.12;letter-spacing:-2px}
.h2{margin-top:30px;font-size:150px;font-weight:900;line-height:1.12;color:#d2402f}
.sub{margin-top:auto;display:flex;flex-direction:column;gap:22px}
.sub div{font-size:52px;font-weight:700;display:flex;gap:20px;align-items:center}
.sub i,.li i{font-style:normal;flex:none;width:56px;height:56px;border-radius:14px;background:#16130f;color:#fbf6ef;display:flex;align-items:center;justify-content:center;font-size:34px;font-weight:900}
.foot{margin-top:60px;display:flex;align-items:center;gap:18px;font-size:34px;font-weight:700;opacity:.75}
.foot img{width:60px;height:60px;border-radius:15px}
.pg{display:flex;justify-content:space-between;align-items:center;font-size:32px;font-weight:700;color:#8a7f73}
.pt{margin-top:40px;font-size:84px;font-weight:900;line-height:1.22}
.pt b{color:#d2402f}
.lead{margin-top:22px;font-size:40px;font-weight:700;color:#5c544b;line-height:1.5}
.list{margin-top:50px;display:flex;flex-direction:column;gap:26px}
.li{display:flex;gap:24px;align-items:flex-start;background:#fff;border:2px solid #eadfd2;border-radius:28px;padding:30px 34px}
.li i{margin-top:4px}
.li.x i{background:#d2402f}
.li .t{font-size:50px;font-weight:900;line-height:1.3}
.li .d{margin-top:8px;font-size:36px;font-weight:700;color:#5c544b;line-height:1.5}
.li .d b{color:#d2402f}
.tbl{margin-top:44px;border-radius:28px;overflow:hidden;border:2px solid #eadfd2;background:#fff}
.tr{display:grid;grid-template-columns:1.3fr 1fr 1fr;font-size:44px;font-weight:700}
.tr div{padding:22px 28px;border-top:2px solid #eadfd2}
.tr.h div{border-top:0;background:#16130f;color:#fbf6ef;font-size:36px}
.tr.hl{background:#fde8df}
.tr.hl div:first-child{color:#d2402f;font-weight:900}
.src{margin-top:auto;padding-top:30px;font-size:30px;color:#8a7f73;line-height:1.5}
.bottom{display:flex;justify-content:space-between;align-items:flex-end;gap:20px;margin-top:20px}
.brand{display:flex;align-items:center;gap:14px;font-size:30px;font-weight:700;color:#8a7f73;flex:none}
.brand img{width:48px;height:48px;border-radius:12px}
.compact .li{padding:20px 30px}.compact .list{gap:18px;margin-top:34px}.compact .cta{margin-top:30px;font-size:46px;padding:24px 34px}
.cta{margin-top:50px;font-size:56px;font-weight:900;padding:30px 40px;border-radius:28px;background:#16130f;color:#fbf6ef;line-height:1.4}
'''

def head():
    return ('<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="fonts/package/700.css">'
            '<link rel="stylesheet" href="fonts/package/900.css"><style>' + CSS + '</style></head><body>')

def cover(n):
    c = n['cover']
    subs = ''.join('<div><i>%d</i>%s</div>' % (i + 1, E(s)) for i, s in enumerate(c['points']))
    return head() + ('<div class="c"><div class="tag">%s</div><div class="h1">%s</div><div class="h2">%s</div>'
                     '<div class="sub">%s</div><div class="foot"><img src="logo.png">方诺签证 · 曼谷</div></div></body></html>'
                     ) % (E(c['tag']), c['h1'], E(c['h2']), subs)

def page(n, p, idx, total):
    body = ''
    if p.get('items'):
        body += '<div class="list">' + ''.join(
            '<div class="li%s"><i>%s</i><div><div class="t">%s</div>%s</div></div>' % (
                ' x' if it.get('x') else '', '!' if it.get('x') else (it.get('n') or str(k + 1)), E(it['t']),
                '<div class="d">%s</div>' % it['d'] if it.get('d') else '') for k, it in enumerate(p['items'])) + '</div>'
    if p.get('table'):
        rows = p['table']
        body += '<div class="tbl">' + '<div class="tr h">' + ''.join('<div>%s</div>' % E(x) for x in rows[0]) + '</div>' + ''.join(
            '<div class="tr%s">%s</div>' % (' hl' if r[0].startswith('Bronze') else '', ''.join('<div>%s</div>' % E(x) for x in r)) for r in rows[1:]) + '</div>'
    if p.get('cta'):
        body += '<div class="cta">%s</div>' % p['cta']
    src = '<div class="src">%s</div>' % E(p['src']) if p.get('src') else '<div class="src"></div>'
    return head() + ('<div class="c'+(' compact' if p.get('compact') else '')+'"><div class="pg"><span>%s</span><span>%d / %d</span></div><div class="pt">%s</div>%s%s'
                     '%s<div class="bottom"><span></span><div class="brand"><img src="logo.png">方诺签证</div></div></div></body></html>'
                     ) % (E(n['series']), idx, total, p['title'], '<div class="lead">%s</div>' % E(p['lead']) if p.get('lead') else '', body, src)

def build(notes, outdir):
    os.makedirs(outdir, exist_ok=True)
    jobs = []
    for n in notes:
        total = len(n['pages']) + 1
        docs = [cover(n)] + [page(n, p, i + 2, total) for i, p in enumerate(n['pages'])]
        for i, d in enumerate(docs):
            f = os.path.join(HERE, '_tmp_%s_%d.html' % (n['key'], i + 1))
            open(f, 'w', encoding='utf-8').write(d)
            jobs.append((f, os.path.join(outdir, '%s_%d.png' % (n['name'], i + 1))))
    js = ('const {chromium}=require("playwright");(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1440}});'
          'for(const [f,o] of %s){await p.goto("file://"+f);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);await p.screenshot({path:o});}'
          'await b.close();})()') % json.dumps(jobs)
    subprocess.run(['node', '-e', js], check=True, cwd=HERE)
    for f, _ in jobs: os.remove(f)
    return [o for _, o in jobs]
