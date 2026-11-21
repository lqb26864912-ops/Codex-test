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
location ~ ^(.*/)index\.html$ { return 301 $1; }

# 静态资源长缓存（改了 CSS/JS 后记得在引用处加 ?v=版本号）
location ~* \.(css|js|woff2|png|jpg|jpeg|webp|ico|svg)$ {
    expires 30d;
    add_header Cache-Control "public";
}
```

## 需要你自己提供的信息

- **统计代码**：Google Analytics 的衡量 ID（G-XXXX）或百度统计代码，提供后我可以加到所有页面。
- **百度站长验证**：在百度搜索资源平台添加网站，把验证用的 meta 标签发给我，或者直接放到首页 `<head>` 里。
- **英文文章**：英文资讯页目前链接的都是中文文章，建议翻译 3～5 篇。
