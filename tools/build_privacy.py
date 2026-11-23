"""Build privacy.html (zh), en/privacy.html, th/privacy.html and add a footer notice on every page.
Run from the site root:  python3 ../tools/build_privacy.py .
Safe to re-run: pages are regenerated, footer notice is only added once.
"""
import os, re, sys, glob

root = sys.argv[1] if len(sys.argv) > 1 else '.'
os.chdir(root)
BASE = 'https://magnificentvisa.com/'

L = {
'zh': dict(
  html_lang='zh-CN', shell='index.html', out='privacy.html', home='首页', badge='隐私说明',
  title='隐私说明｜方诺签证', h1='隐私说明',
  desc='方诺签证网站的隐私说明：咨询表单、WhatsApp 等联系方式、访问统计，以及 Meta Pixel 广告衡量如何处理你的信息。',
  updated='最近更新：2026 年 11 月 21 日',
  footer='本网站使用 Meta Pixel 和访问统计，用于衡量广告效果、改进网站。详见<a href="{href}" class="text-link">隐私说明</a>。',
  body='''
<p>本说明介绍 magnificentvisa.com 如何处理你的信息。我们尽量少收集：咨询表单不会把你填写的内容发送到我们的服务器。</p>

<h2>1. 我们是谁</h2>
<p>The magnificent world VISA co.Ltd（泰文登记名称：<span lang="th">บริษัท เดอะ แม็กนิฟิเซนต์ เวิลด์ วีซ่า จำกัด</span>），公司登记号 0105568067189。办公地址：Room 1916, 19th Floor, Pier111 Building, 111 Ratchadamri Road, Bangkok。</p>
<p>与隐私有关的问题，可以通过 WhatsApp +66 98 739 0634 联系我们（也可以用 Telegram @Taiguo911、LINE north137946 或微信 Qwe137946a）。</p>

<h2>2. 本网站会处理哪些信息</h2>
<ul>
<li><strong>咨询表单：</strong>你填写的内容只在你自己的浏览器里生成一份草稿，不会发送到我们的服务器，刷新页面后即清空。只有当你点击「在 WhatsApp 中打开」之类的按钮，草稿才会交给对应的通讯软件，并由你自己决定是否发送。</li>
<li><strong>你主动发给我们的信息：</strong>你通过 WhatsApp、Telegram、LINE、Messenger 或微信发来的内容，我们会收到，用于回复咨询、报价和办理业务。首次咨询请不要发送证件号码、银行资料，也不要上传证件。</li>
<li><strong>访问统计：</strong>我们使用 GoatCounter 统计页面浏览量等汇总数据。据该服务说明，它不使用 Cookie 跟踪访客。</li>
<li><strong>广告衡量：</strong>我们使用 Meta Pixel，详见下一节。</li>
<li><strong>服务器日志：</strong>与大多数网站一样，服务器可能记录访问时间、IP 地址和请求的页面等基础日志，用于网站安全和故障排查。</li>
</ul>

<h2>3. Meta Pixel（Facebook / Instagram 广告）</h2>
<p>本网站安装了 Meta Platforms 提供的 Meta Pixel。它会在你的浏览器中设置 Cookie，并向 Meta 发送：你访问了哪些页面、浏览器和设备信息、IP 地址，以及你点击联系按钮（WhatsApp、Telegram、LINE、Messenger、复制微信号）或使用咨询表单时的事件。事件信息只包含联系渠道、所在的服务页面和页面语言；我们没有设置发送你在表单中填写的文字内容。</p>
<p>这些数据用于衡量广告效果，以及向访问过本网站的人展示相关广告。Meta 按其自己的隐私政策处理这些数据。</p>
<p><strong>如何拒绝：</strong>可以在 Facebook 或 Instagram 的广告设置中，关闭基于网站活动的广告；也可以在浏览器中屏蔽第三方 Cookie，或使用广告拦截插件。</p>

<h2>4. 信息会提供给谁</h2>
<p>除上述通讯软件、Meta 和 GoatCounter 外，我们的网站由托管服务器提供。办理具体业务时，经你同意，我们会把办理所需的材料提交给相关政府机构。我们不会出售你的信息。</p>

<h2>5. 保存多久</h2>
<p>咨询聊天记录和办理材料，仅在处理你的咨询、提供服务以及满足法律要求所需的期间内保存。</p>

<h2>6. 你的权利</h2>
<p>根据适用的数据保护法律（例如泰国《个人数据保护法》，PDPA），你可能有权查阅、更正、删除我们保存的你的个人数据，或撤回你的同意。请通过上面的联系方式告诉我们。</p>

<h2>7. 本说明的更新</h2>
<p>如果网站使用的工具或处理方式有变化，我们会更新本页，并修改页首的日期。</p>
'''),
'en': dict(
  html_lang='en', shell='en/index.html', out='en/privacy.html', home='Home', badge='Privacy',
  title='Privacy Notice | Magnificent Visa', h1='Privacy Notice',
  desc='Privacy notice for magnificentvisa.com: how the enquiry form, WhatsApp and other contact channels, page-view analytics and the Meta Pixel handle your information.',
  updated='Last updated: 21 November 2026',
  footer='This site uses the Meta Pixel and page-view analytics to measure ads and improve the site. See our <a href="{href}" class="text-link">Privacy Notice</a>.',
  body='''
<p>This notice explains how magnificentvisa.com handles your information. We keep collection to a minimum: our enquiry form does not send what you type to our servers.</p>

<h2>1. Who we are</h2>
<p>The magnificent world VISA co.Ltd (registered Thai name: <span lang="th">บริษัท เดอะ แม็กนิฟิเซนต์ เวิลด์ วีซ่า จำกัด</span>), company registration no. 0105568067189. Office: Room 1916, 19th Floor, Pier111 Building, 111 Ratchadamri Road, Bangkok.</p>
<p>For privacy questions, contact us on WhatsApp at +66 98 739 0634 (or Telegram @Taiguo911, LINE north137946, or WeChat Qwe137946a).</p>

<h2>2. What this website processes</h2>
<ul>
<li><strong>Enquiry form:</strong> what you type is used only to build a draft message in your own browser. It is not sent to our servers and is cleared when you refresh the page. The draft is handed to a messaging app only when you click a button such as “Open in WhatsApp”, and you decide whether to send it.</li>
<li><strong>Information you send us:</strong> messages you send through WhatsApp, Telegram, LINE, Messenger or WeChat reach us, and we use them to answer your enquiry, give a quote and carry out the work. For a first enquiry, please do not send passport numbers or bank details, and do not upload ID documents.</li>
<li><strong>Page-view statistics:</strong> we use GoatCounter to count page views and similar summary figures. According to the service, it does not use cookies to track visitors.</li>
<li><strong>Ad measurement:</strong> we use the Meta Pixel, described in the next section.</li>
<li><strong>Server logs:</strong> like most websites, our server may keep basic logs such as access time, IP address and the page requested, for security and troubleshooting.</li>
</ul>

<h2>3. Meta Pixel (Facebook / Instagram ads)</h2>
<p>This website uses the Meta Pixel provided by Meta Platforms. It sets cookies in your browser and sends Meta the pages you visit, browser and device information, your IP address, and events when you click a contact button (WhatsApp, Telegram, LINE, Messenger, copy WeChat ID) or use the enquiry form. These events contain only the contact channel, the service page you were on and the page language; we have not set the Pixel to send the text you type into the form.</p>
<p>This data is used to measure how our ads perform and to show relevant ads to people who have visited this website. Meta handles the data under its own privacy policy.</p>
<p><strong>How to opt out:</strong> in your Facebook or Instagram ad settings you can turn off ads based on website activity. You can also block third-party cookies in your browser or use an ad blocker.</p>

<h2>4. Who receives information</h2>
<p>Besides the messaging apps, Meta and GoatCounter mentioned above, the website is served from a hosting server. When we carry out a specific application, we submit the documents it needs to the relevant government authority with your agreement. We do not sell your information.</p>

<h2>5. How long we keep it</h2>
<p>We keep chat records and application documents only for as long as needed to handle your enquiry, provide the service and meet legal requirements.</p>

<h2>6. Your rights</h2>
<p>Under applicable data protection law (for example Thailand’s Personal Data Protection Act, PDPA), you may have the right to access, correct or delete personal data we hold about you, or to withdraw your consent. Please tell us using the contact details above.</p>

<h2>7. Changes to this notice</h2>
<p>If the tools we use or the way we handle information changes, we will update this page and the date at the top.</p>
'''),
'th': dict(
  html_lang='th', shell='th/index.html', out='th/privacy.html', home='หน้าแรก', badge='ความเป็นส่วนตัว',
  title='นโยบายความเป็นส่วนตัว | Magnificent Visa', h1='นโยบายความเป็นส่วนตัว',
  desc='นโยบายความเป็นส่วนตัวของ magnificentvisa.com: แบบฟอร์มสอบถาม ช่องทางติดต่ออย่าง WhatsApp สถิติการเข้าชม และ Meta Pixel จัดการข้อมูลของคุณอย่างไร',
  updated='อัปเดตล่าสุด: 21 พฤศจิกายน 2026',
  footer='เว็บไซต์นี้ใช้ Meta Pixel และสถิติการเข้าชม เพื่อวัดผลโฆษณาและปรับปรุงเว็บไซต์ ดู <a href="{href}" class="text-link">นโยบายความเป็นส่วนตัว</a>',
  body='''
<p>นโยบายนี้อธิบายวิธีที่ magnificentvisa.com จัดการข้อมูลของคุณ เราพยายามเก็บข้อมูลให้น้อยที่สุด แบบฟอร์มสอบถามของเราไม่ส่งสิ่งที่คุณพิมพ์ไปยังเซิร์ฟเวอร์ของเรา</p>

<h2>1. เราคือใคร</h2>
<p>The magnificent world VISA co.Ltd (ชื่อจดทะเบียนภาษาไทย: <span lang="th">บริษัท เดอะ แม็กนิฟิเซนต์ เวิลด์ วีซ่า จำกัด</span>) เลขทะเบียนนิติบุคคล 0105568067189 สำนักงาน: ห้อง 1916 ชั้น 19 อาคาร Pier111 เลขที่ 111 ถนนราชดำริ กรุงเทพฯ</p>
<p>หากมีคำถามเรื่องความเป็นส่วนตัว ติดต่อเราได้ทาง WhatsApp +66 98 739 0634 (หรือ Telegram @Taiguo911, LINE north137946 หรือ WeChat Qwe137946a)</p>

<h2>2. เว็บไซต์นี้ประมวลผลข้อมูลอะไรบ้าง</h2>
<ul>
<li><strong>แบบฟอร์มสอบถาม:</strong> สิ่งที่คุณพิมพ์ใช้สร้างข้อความร่างในเบราว์เซอร์ของคุณเองเท่านั้น ไม่ถูกส่งไปยังเซิร์ฟเวอร์ของเรา และจะถูกล้างเมื่อรีเฟรชหน้า ข้อความร่างจะถูกส่งต่อให้แอปแชทก็ต่อเมื่อคุณกดปุ่ม เช่น “เปิดใน WhatsApp” และคุณเป็นผู้ตัดสินใจว่าจะส่งหรือไม่</li>
<li><strong>ข้อมูลที่คุณส่งให้เรา:</strong> ข้อความที่คุณส่งผ่าน WhatsApp, Telegram, LINE, Messenger หรือ WeChat จะมาถึงเรา และเราใช้เพื่อตอบคำถาม เสนอราคา และดำเนินการ การสอบถามครั้งแรกกรุณาอย่าส่งเลขหนังสือเดินทางหรือข้อมูลบัญชีธนาคาร และอย่าอัปโหลดเอกสารประจำตัว</li>
<li><strong>สถิติการเข้าชม:</strong> เราใช้ GoatCounter นับจำนวนการเข้าชมหน้าและตัวเลขสรุปทำนองเดียวกัน ตามที่ผู้ให้บริการระบุ บริการนี้ไม่ใช้คุกกี้ติดตามผู้เข้าชม</li>
<li><strong>การวัดผลโฆษณา:</strong> เราใช้ Meta Pixel ตามที่อธิบายในหัวข้อถัดไป</li>
<li><strong>บันทึกของเซิร์ฟเวอร์:</strong> เช่นเดียวกับเว็บไซต์ส่วนใหญ่ เซิร์ฟเวอร์ของเราอาจเก็บบันทึกพื้นฐาน เช่น เวลาเข้าชม ที่อยู่ IP และหน้าที่ขอ เพื่อความปลอดภัยและแก้ไขปัญหา</li>
</ul>

<h2>3. Meta Pixel (โฆษณา Facebook / Instagram)</h2>
<p>เว็บไซต์นี้ใช้ Meta Pixel ของ Meta Platforms ซึ่งจะตั้งคุกกี้ในเบราว์เซอร์ของคุณ และส่งให้ Meta ว่าคุณเข้าชมหน้าใด ข้อมูลเบราว์เซอร์และอุปกรณ์ ที่อยู่ IP รวมถึงเหตุการณ์เมื่อคุณกดปุ่มติดต่อ (WhatsApp, Telegram, LINE, Messenger, คัดลอก WeChat ID) หรือใช้แบบฟอร์มสอบถาม เหตุการณ์เหล่านี้มีเพียงช่องทางติดต่อ หน้าบริการที่คุณอยู่ และภาษาของหน้า เราไม่ได้ตั้งค่าให้ส่งข้อความที่คุณพิมพ์ในแบบฟอร์ม</p>
<p>ข้อมูลนี้ใช้วัดผลโฆษณาของเรา และแสดงโฆษณาที่เกี่ยวข้องให้ผู้ที่เคยเข้าชมเว็บไซต์นี้ Meta จัดการข้อมูลตามนโยบายความเป็นส่วนตัวของ Meta เอง</p>
<p><strong>วิธีปฏิเสธ:</strong> ในการตั้งค่าโฆษณาของ Facebook หรือ Instagram คุณสามารถปิดโฆษณาที่อิงกิจกรรมบนเว็บไซต์ได้ หรือบล็อกคุกกี้ของบุคคลที่สามในเบราว์เซอร์ หรือใช้ตัวบล็อกโฆษณา</p>

<h2>4. ใครได้รับข้อมูลบ้าง</h2>
<p>นอกจากแอปแชท Meta และ GoatCounter ข้างต้น เว็บไซต์ของเราให้บริการจากเซิร์ฟเวอร์โฮสติ้ง เมื่อดำเนินการเรื่องใดเรื่องหนึ่งให้คุณ เราจะยื่นเอกสารที่จำเป็นต่อหน่วยงานราชการที่เกี่ยวข้องโดยได้รับความยินยอมจากคุณ เราไม่ขายข้อมูลของคุณ</p>

<h2>5. เก็บไว้นานเท่าไร</h2>
<p>เราเก็บบันทึกการสนทนาและเอกสารที่ใช้ดำเนินการ เท่าที่จำเป็นต่อการตอบคำถามของคุณ การให้บริการ และการปฏิบัติตามกฎหมายเท่านั้น</p>

<h2>6. สิทธิของคุณ</h2>
<p>ตามกฎหมายคุ้มครองข้อมูลส่วนบุคคลที่เกี่ยวข้อง (เช่น พ.ร.บ.คุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562 หรือ PDPA) คุณอาจมีสิทธิขอเข้าถึง แก้ไข หรือลบข้อมูลส่วนบุคคลของคุณที่เราเก็บไว้ หรือถอนความยินยอม กรุณาแจ้งเราผ่านช่องทางติดต่อข้างต้น</p>

<h2>7. การเปลี่ยนแปลงนโยบายนี้</h2>
<p>หากเครื่องมือที่เราใช้หรือวิธีจัดการข้อมูลเปลี่ยนไป เราจะอัปเดตหน้านี้และวันที่ด้านบน</p>
'''),
}

def swap(pattern, repl, s, flags=0):
    s2, n = re.subn(pattern, lambda m: repl, s, count=1, flags=flags)
    assert n == 1, pattern
    return s2

def esc(t):
    return t.replace('&', '&amp;').replace('"', '&quot;')

SWITCH = [('zh-CN', '中文', 'privacy.html', ''), ('en', 'EN', 'en/privacy.html', 'en/'), ('th', 'ไทย', 'th/privacy.html', 'th/')]

for code, c in L.items():
    s = open(c['shell'], encoding='utf-8').read()
    prefix = '' if code == 'zh' else '../'
    head_end = s.index('</head>')
    head, rest = s[:head_end], s[head_end:]
    # head: title, description, canonical, hreflang, og/twitter, no structured data from the home page
    head = swap(r'<title>.*?</title>', '<title>%s</title>' % esc(c['title']), head, re.S)
    for key in ('name="description"', 'property="og:title"', 'property="og:description"', 'name="twitter:title"', 'name="twitter:description"'):
        val = c['desc'] if 'description' in key else c['title']
        head = swap(r'<meta %s content="[^"]*">' % re.escape(key), '<meta %s content="%s">' % (key, esc(val)), head)
    url = BASE + c['out']
    head = swap(r'<link rel="canonical" href="[^"]*">', '<link rel="canonical" href="%s">' % url, head)
    head = swap(r'<meta property="og:url" content="[^"]*">', '<meta property="og:url" content="%s">' % url, head)
    hl = ('<link rel="alternate" hreflang="zh-Hans" href="%sprivacy.html">\n<link rel="alternate" hreflang="en" href="%sen/privacy.html">\n'
          '<link rel="alternate" hreflang="th" href="%sth/privacy.html">\n<link rel="alternate" hreflang="x-default" href="%sprivacy.html">') % ((BASE,) * 4)
    head = swap(r'(<link rel="alternate" hreflang="[^"]+" href="[^"]*">\n?)+', hl + '\n', head)
    head = re.sub(r'<script type="application/ld\+json">.*?</script>\n?', '', head, flags=re.S)
    # header: no "current page" on Home, language switch points to the three privacy pages
    h_start = rest.index('<header'); h_end = rest.index('</header>') + len('</header>')
    header = rest[h_start:h_end].replace(' aria-current="page"', '')
    parts = []
    for lc, label, _, d in SWITCH:
        cur = (lc == 'zh-CN' and code == 'zh') or lc == code
        href = 'privacy.html' if cur else prefix + d + 'privacy.html'
        parts.append('<a href="%s" lang="%s"%s>%s</a>' % (href, lc, ' aria-current="page"' if cur else '', label))
    sw = ''.join(parts)
    header = re.sub(r'(<div class="language-switch" aria-label="[^"]*">).*?(</div>)', lambda m: m.group(1) + sw + m.group(2), header, count=1, flags=re.S)
    footer = rest[rest.index('<footer'):]
    main = ('\n<main id="main">\n<section id="top" class="hero page-hero">\n<div class="hero-grid-bg" aria-hidden="true"></div>\n<div class="container">\n'
            '<nav class="breadcrumbs reveal" aria-label="breadcrumb"><a href="./">%s</a><span> / %s</span></nav>\n'
            '<p class="badge reveal"><span class="dot" aria-hidden="true"></span>%s</p>\n<h1 class="reveal" style="--d:.12s">%s</h1>\n</div>\n</section>\n'
            '<article class="container article-wrap">\n<div class="article-meta"><span>%s</span></div>\n<div class="article-body">%s</div>\n</article>\n</main>\n') % (
            c['home'], c['badge'], c['badge'], c['h1'], c['updated'], c['body'])
    open(c['out'], 'w', encoding='utf-8').write(head + '\n' + rest[:h_start].replace('</head>', '</head>\n', 1) + header + main + footer)

# footer notice on every page (once)
done = 0
for f in glob.glob('**/*.html', recursive=True):
    s = open(f, encoding='utf-8').read()
    if 'class="footer-bottom"' not in s or 'privacy.html' in s.split('<footer', 1)[1]:
        continue
    code = 'en' if f.startswith('en/') else 'th' if f.startswith('th/') else 'zh'
    inner = f.split('/', 1)[1] if code != 'zh' else f
    href = '../' * inner.count('/') + 'privacy.html'
    note = '<p>' + L[code]['footer'].format(href=href) + '</p>'
    i = s.index('class="footer-bottom"'); j = s.index('</div>', i)
    s = s[:j] + note + ' ' + s[j:]
    open(f, 'w', encoding='utf-8').write(s); done += 1
print('footer notice added to', done, 'pages')

# sitemap
sm = open('sitemap.xml', encoding='utf-8').read()
add = ''.join('  <url>\n    <loc>%s%s</loc>\n  </url>\n' % (BASE, c['out']) for c in L.values() if BASE + c['out'] + '<' not in sm)
open('sitemap.xml', 'w', encoding='utf-8').write(sm.replace('</urlset>', add + '</urlset>'))
print('built', [c['out'] for c in L.values()])
