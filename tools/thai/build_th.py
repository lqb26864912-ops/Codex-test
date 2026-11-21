"""Build /th/ pages from /en/ pages using the Thai string table.
Usage: python3 build_th.py <site_root> <strings.json> <t1.py> <t2.py> <t3.py>
"""
import sys, os, re, json, runpy
sys.path.insert(0, os.path.dirname(__file__))
import i18n

root, strings_path, *tfiles = sys.argv[1:]
keys = list(json.load(open(strings_path, encoding='utf-8')).keys())
T = {}
for f in tfiles:
    T.update(runpy.run_path(f)['T'])
missing = [i for i in range(len(keys)) if i not in T]
assert not missing, f'missing translations: {missing[:20]}'
TH = {keys[i]: T[i] for i in range(len(keys))}

PAGES = i18n.PAGES
FILE = {p: ('' if p == 'index' else p + '.html') for p in PAGES}   # path relative to a language root
BASE = 'https://magnificentvisa.com/'
H1 = {
 'index': '<span class="glow">วีซ่าไทย</span>',
 'retirement': '<span class="glow">วีซ่าเกษียณ</span>',
 'elite': '<span class="glow">วีซ่าอีลิท</span>',
 'business': '<span class="glow">วีซ่าธุรกิจ</span>',
 'work': '<span class="glow">วีซ่าทำงาน</span>',
 'student': '<span class="glow">วีซ่านักเรียน</span>',
 'airport': '<span class="glow">บริการสนามบิน</span>',
 'extensions': '<span class="glow">ต่ออายุวีซ่า</span>',
 'airport-sendoff': '<span class="glow"><span style="white-space:nowrap">บริการส่ง</span><span style="white-space:nowrap">ที่สนามบิน</span></span>',
 'dtv': 'วีซ่า DTV',
 'medical': 'สอบถามวีซ่ารักษาพยาบาล',
 'tm47': 'รายงานตัว <span style="white-space:nowrap">90 วัน</span>',
}
translated_files = {p + '.html' for p in PAGES} | {'./', 'index.html'}

def tr(t):
    if t not in TH:
        raise KeyError(t)
    return TH[t]

def hreflang_block(p):
    f = FILE[p]
    return ('<link rel="alternate" hreflang="zh-Hans" href="%s%s">\n'
            '<link rel="alternate" hreflang="en" href="%sen/%s">\n'
            '<link rel="alternate" hreflang="th" href="%sth/%s">\n'
            '<link rel="alternate" hreflang="x-default" href="%s%s">') % (BASE, f, BASE, f, BASE, f, BASE, f)

def set_hreflang(s, p):
    s2, n = re.subn(r'(<link rel="alternate" hreflang="[^"]+" href="[^"]*">\n?)+', hreflang_block(p) + '\n', s, count=1)
    assert n == 1, p
    return s2

def lang_switch(p, current, prefix):
    """prefix: path from the current page to the site root ('' or '../')."""
    f = FILE[p]
    dirs = {'zh-CN': '', 'en': 'en/', 'th': 'th/'}
    out = []
    for lang, label in (('zh-CN', '中文'), ('en', 'EN'), ('th', 'ไทย')):
        href = (f or './') if lang == current else prefix + dirs[lang] + f
        out.append('<a href="%s" lang="%s"%s>%s</a>' % (href, lang, ' aria-current="page"' if lang == current else '', label))
    return ''.join(out)

def set_switch(s, p, current, prefix):
    s2, n = re.subn(r'(<div class="language-switch" aria-label="[^"]*">).*?(</div>)',
                    lambda m: m.group(1) + lang_switch(p, current, prefix) + m.group(2), s, flags=re.S)
    assert n >= 1, (p, current)
    return s2

def fix_links(s):
    # links to pages that have no Thai version yet go to the English page
    def rep(m):
        href = m.group(1)
        path = href.split('#')[0]
        if href.startswith(('http', '#', 'mailto:', 'tel:', '../', 'data:')) or path in translated_files or path == '':
            return m.group(0)
        if path.endswith(('.css', '.js', '.png', '.jpg', '.webp', '.ico', '.woff2')):
            return m.group(0)
        return 'href="../en/%s"' % href
    return re.sub(r'href="([^"]*)"', rep, s)

os.makedirs(os.path.join(root, 'th'), exist_ok=True)
for p in PAGES:
    src = open(os.path.join(root, 'en', p + '.html'), encoding='utf-8').read()
    s = i18n.process(src, tr)
    s = s.replace('<html lang="en">', '<html lang="th">', 1)
    s = s.replace('content="en_US"', 'content="th_TH"')
    s = s.replace('"inLanguage":"en"', '"inLanguage":"th"')
    # self URLs: canonical, og:url, JSON-LD items for translated pages
    for q in PAGES:
        s = s.replace('"%sen/%s"' % (BASE, FILE[q]), '"%sth/%s"' % (BASE, FILE[q]))
    s = set_hreflang(s, p)
    s = set_switch(s, p, 'th', '../')
    s = re.sub(r'(<h1[^>]*>).*?(</h1>)', lambda m: m.group(1) + H1[p] + m.group(2), s, count=1, flags=re.S)
    s = fix_links(s)
    open(os.path.join(root, 'th', p + '.html'), 'w', encoding='utf-8').write(s)

# add Thai to the switch + hreflang of matching zh / en pages
for p in PAGES:
    for lang, path, prefix in (('zh-CN', p + '.html', ''), ('en', 'en/' + p + '.html', '../')):
        fp = os.path.join(root, path)
        s = open(fp, encoding='utf-8').read()
        s = set_hreflang(s, p)
        s = set_switch(s, p, lang, prefix)
        open(fp, 'w', encoding='utf-8').write(s)

# sitemap
sp = os.path.join(root, 'sitemap.xml')
sm = open(sp, encoding='utf-8').read()
add = ''.join('  <url>\n    <loc>%sth/%s</loc>\n  </url>\n' % (BASE, FILE[p]) for p in PAGES if '%sth/%s<' % (BASE, FILE[p]) not in sm)
sm = sm.replace('</urlset>', add + '</urlset>')
open(sp, 'w', encoding='utf-8').write(sm)
print('built', len(PAGES), 'Thai pages')
