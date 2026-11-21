# SEO 修复说明（magnificentvisa.com）

`site/` 目录是线上网站的完整副本，已经包含下面的修复。上线方法：把 `site/` 里的文件覆盖到服务器网站根目录（`assets/feedback/` 不在仓库里，服务器上原有的保留不动）。

## 已修改

1. **H1 加入关键词**：如"养老签"改成"泰国养老签"，"Work Visa"改成"Thailand Work Visa"，共 22 个页面；已在手机和电脑上检查过显示效果。
2. **文章封面图补上 alt 描述**：4 篇新闻文章。
3. **BlogPosting 结构化数据补 `image` 字段**：10 篇文章。
4. **sitemap.xml 的 lastmod**：文章用真实修改日期；其他页面去掉统一填写的 2026-11-21，以后哪页有改动再填真实日期。
5. **英文标题缩短到 60 字符以内**：en/news、en/student、en/tools/visa-checker；en/student 的描述从 345 字符缩到 140 字符。
6. **中文描述扩写**：news/、tools/visa-checker、入境材料核对文章。
7. **内部链接统一**：`index.html` 改成目录地址（`./`、`news/`、`../` 等），和 canonical 保持一致。

## 需要在服务器上设置（nginx / openresty）

```nginx
# 访问 /index.html 时 301 跳转到目录地址，避免重复页面
# 注意：必须判断 $request_uri（用户实际请求的地址），不能用 location 匹配，
# 否则会和 nginx 的 index 内部跳转冲突，造成无限重定向
if ($request_uri ~ "^(.*/)index\.html(\?.*)?$") { return 301 $1$2; }

# 静态资源长缓存（改了 CSS/JS 后记得在引用处加 ?v=版本号）
location ~* \.(css|js|woff2|png|jpg|jpeg|webp|ico|svg)$ {
    expires 30d;
    add_header Cache-Control "public";
}
```

## 需要你自己提供的信息

- **统计**：网站已经装了 GoatCounter（magnificentvi.goatcounter.com），可以在它的后台看访问数据。如果还想用 Google Analytics，把衡量 ID（G-XXXX）发给我。
- **百度站长验证**：在百度搜索资源平台添加网站，把验证用的 meta 标签发给我，或者直接放到首页 `<head>` 里。
- **英文文章**：英文资讯页目前链接的都是中文文章，建议翻译 3～5 篇。

## 泰语版（/th/）

新增 12 个泰语页面：首页、养老签、精英签、DTV、工作签、商务签、学生签、医疗签、续签、90 天报到、机场服务、机场送机。

- 每个页面的中文、英文、泰语版本都互相加了 hreflang，三个语言版本的语言切换按钮都加上了「ไทย」
- 泰语 H1 用的是泰国人常搜的说法：วีซ่าเกษียณ（养老签）、วีซ่าอีลิท（精英签）、วีซ่าทำงาน（工作签）、ต่ออายุวีซ่า（续签）、รายงานตัว 90 วัน（90 天报到）等
- 询问表单和 WhatsApp 预填消息也翻译成了泰语
- 资讯、出签反馈、签证匹配工具还没有泰语版，泰语页面里的这些链接会跳到英文版
- CSS 加了泰文字体，标题行高也调高了，防止泰文的声调符号被裁掉
- sitemap 增加了 12 个泰语网址

### 顺手修好的英文页面问题

- `en/tm47.html`：「…or Elite visa」后面多出一个 DTV 链接
- `en/dtv.html`：「90-day report」后面多出一个「Medical visa enquiry」链接

### ⚠️ 上线前建议

- **请懂泰语的同事通读一遍**，尤其是价格、法律免责声明和办理条件这几部分
- 泰国客户会通过 WhatsApp 发来泰语消息，请确认有人能用泰语回复

## Meta Pixel（Facebook / Instagram 广告追踪）

代码已经装到全部 52 个页面（`site/assets/meta-pixel.js`），**像素 ID 已填：1442570674148916**（Magnificent Visa Website）。

**如需更换像素**：打开 `site/assets/meta-pixel.js`，修改第 12 行的 `PIXEL_ID`，然后重新上传这个文件。

| 事件 | 什么时候触发 | 在 Ads Manager 里怎么用 |
|---|---|---|
| PageView | 每次打开页面 | 再营销受众（看过网站的人） |
| Contact | 点击 WhatsApp / Telegram / LINE / Messenger，或复制微信号 | 广告的转化目标 |
| Lead | 填完询问表单后点击发送或复制 | 最强的购买意向信号，可以作为转化目标 |

每个事件都带三个参数：`content_name`（联系渠道）、`content_category`（服务，如 retirement、dtv）、`language`（zh / en / th）。可以用这些参数建自定义转化，比如"泰语页面的养老签咨询"。

**验证是否生效**：用 Chrome 安装 Meta Pixel Helper 插件，打开网站看事件有没有触发；或者在 Events Manager 里用「测试事件」功能。

**隐私**：泰国 PDPA 对追踪类 Cookie 有告知要求，建议在隐私说明里加上一句"本网站使用 Meta Pixel 衡量广告效果"。

### 顺手修好的问题

- **复制微信号的按钮原来点了没反应**：每个页面都有这个按钮，但线上版本没有对应的代码。现在点击后会复制 `Qwe137946a`，并提示"已复制"，中、英、泰三种语言都支持。
- **资讯文章页面原来有 JS 报错**：页面上没有询问表单，但脚本照样去初始化表单，结果出错。现在只在有表单的页面初始化。
