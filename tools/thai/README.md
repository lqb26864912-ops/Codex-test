# 泰语版生成工具

泰语页面（`site/th/`）是用英文页面（`site/en/`）加上翻译表自动生成的。

- `strings.json`：从 12 个英文页面提取的全部文字（共 791 条）
- `t1.py` / `t2.py` / `t3.py`：对应的泰语翻译，按编号对应
- `i18n.py`：提取和替换文字的工具
- `build_th.py`：生成 `site/th/*.html`，同时给中文和英文页面加上泰语切换按钮、hreflang，并更新 sitemap
- `wa_th.py`：把泰语页面里 WhatsApp 预填的英文消息换成泰语

## 英文页面改了内容之后，怎么更新泰语版

```bash
cd site
python3 ../tools/thai/i18n.py . ../tools/thai/strings.json   # 重新提取，新增的文字会出现在 strings.json 末尾
# 在 t3.py 里给新编号补上泰语翻译
python3 ../tools/thai/build_th.py . ../tools/thai/strings.json ../tools/thai/t1.py ../tools/thai/t2.py ../tools/thai/t3.py
python3 ../tools/thai/wa_th.py .
```

注意：重新提取时如果英文页面删改了旧文字，编号会变，需要核对翻译表。

## ⚠️ 重新生成前请注意

线上的 `th/index.html`、`th/retirement.html`、`th/extensions.html` 以及对应的英文、中文页面，已经被人工修改过措辞（例如把"全包"改成"费用含代办服务"）。这些改动**不在** `strings.json` 和 `t1/t2/t3.py` 里。直接重新运行 `build_th.py` 会用旧译文把这些页面的改动覆盖掉。

要重新生成之前，先把这些改动同步进英文页面和翻译表，或者只对没有被人工修改过的页面运行。

`th/elite.html` 和 `en/elite.html` 也已经手工改写过（新增了适合谁、对比表等板块），同样不在翻译表里，重新生成会被覆盖。
