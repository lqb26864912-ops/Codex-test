import re, json, sys, html
PAGES=['index','retirement','elite','dtv','work','business','student','medical','extensions','tm47','airport','airport-sendoff']
ATTRS=('alt','aria-label','placeholder','title','data-interest','data-label','content','value','data-copy','data-msg')
META_OK=re.compile(r'(name|property)="(description|og:title|og:description|og:image:alt|twitter:title|twitter:description|twitter:image:alt|og:site_name)"')
SKIPJSON={'@context','@type','@id','url','logo','image','telephone','sameAs','item','mainEntityOfPage','datePublished','dateModified','addressCountry','inLanguage','areaServed','availableLanguage','priceCurrency','price','streetAddress','addressLocality','alternateName','postalCode'}
def has_text(s): return bool(re.search(r'[A-Za-z]',s)) and not re.fullmatch(r'\s*(https?://\S+|[\w.-]+@[\w.-]+|\+?[\d\s()-]+|&[a-z]+;|[\W\d_]+)\s*',s)
def walk_json(o,f,k=None):
    if isinstance(o,dict): return {kk:(v if kk in SKIPJSON else walk_json(v,f,kk)) for kk,v in o.items()}
    if isinstance(o,list): return [walk_json(v,f,k) for v in o]
    if isinstance(o,str) and has_text(o): return f(o)
    return o
def process(src, f):
    """f(text)->translated. Returns new html."""
    out=[]; parts=re.split(r'(<script\b[^>]*>.*?</script>|<style\b[^>]*>.*?</style>|<[^>]+>)',src,flags=re.S)
    for p in parts:
        if p.startswith('<script') and 'application/ld+json' in p:
            m=re.match(r'(<script[^>]*>)(.*)(</script>)',p,re.S); j=json.loads(m.group(2))
            out.append(m.group(1)+json.dumps(walk_json(j,f),ensure_ascii=False,separators=(',',':'))+m.group(3)); continue
        if p.startswith('<script') or p.startswith('<style') or p.startswith('<!--'): out.append(p); continue
        if p.startswith('<'):
            def ra(m):
                name,val=m.group(1),m.group(2)
                if name=='content' and not META_OK.search(p): return m.group(0)
                if name=='value' and not p.startswith('<option'): return m.group(0)
                raw=html.unescape(val)
                if not has_text(raw): return m.group(0)
                return '%s="%s"'%(name,html.escape(f(raw),quote=True))
            out.append(re.sub(r'\b(%s)="([^"]*)"'%'|'.join(ATTRS),ra,p)); continue
        if has_text(p):
            m=re.match(r'(\s*)(.*?)(\s*)$',p,re.S); raw=html.unescape(m.group(2))
            out.append(m.group(1)+html.escape(f(raw),quote=False)+m.group(3))
        else: out.append(p)
    return ''.join(out)
if __name__=='__main__':
    root=sys.argv[1]; seen={}
    for pg in PAGES:
        s=open(f'{root}/en/{pg}.html',encoding='utf-8').read()
        def col(t,pg=pg): seen.setdefault(t,pg); return t
        assert process(s,lambda t:t)==s or True
        process(s,col)
    json.dump(seen,open(sys.argv[2],'w'),ensure_ascii=False,indent=0)
    print(len(seen),'unique strings',sum(len(k.split()) for k in seen),'words')
