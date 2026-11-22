# 短视频模板（15 秒 Reels）

现有：`elite.html`（精英签）、`retire.html`（养老签两条通道）。

用 HTML 动画逐帧截图，再用 ffmpeg 合成 MP4。竖版 1080×1920，30 帧，15 秒。

## 重新生成

```bash
cd tools/video
npm pack @fontsource/noto-sans-sc@5.1.1 && tar -xzf fontsource-noto-sans-sc-*.tgz && mv package fonts/ 2>/dev/null || (mkdir -p fonts && mv package fonts/)
node render.js preview elite.html          # 先看 4 个关键画面（prev-elite-*.png）
node render.js full elite.html             # 输出 450 帧到 frames-elite/
ffmpeg -y -framerate 30 -i frames-elite/%04d.png -f lavfi -i anullsrc=channel_layout=stereo:sample_rate=44100 \
  -shortest -c:v libx264 -profile:v high -pix_fmt yuv420p -crf 18 -preset slow -r 30 \
  -c:a aac -b:a 128k -movflags +faststart 精英签_Reels_15秒.mp4
```

## 改内容

文字都在 `elite.html` 里。每个元素的出现时间是 `animation-delay`，每个场景的淡出时间在 `#s1`–`#s3` 的 `out` 动画上。

## ⚠️ 需要按时更新

- "官方会员费 65 万泰铢起"：Bronze 套餐官方开放申请至 2026-12-31。过了这个日期，要按官方最新公布改价格，重新生成视频

- 养老签视频里的价格（54,000 / 60,000）、"通常 3–5 天""本人到场约 2 次""约 1 天出签""含协助开银行账户和 1 年延期"，都来自网站。价格或做法变了，要同步修改并重新生成

## 做新视频

复制一个现有的 .html，改 4 个场景（`#s1`–`#s4`）里的文字和 `animation-delay`，然后：

```bash
node render.js preview 新文件.html 2,6,10,14   # 第三个参数是要预览的时间点（秒）
node render.js full 新文件.html
```
