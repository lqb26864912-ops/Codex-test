# 短视频模板（精英签 15 秒 Reels）

用 HTML 动画逐帧截图，再用 ffmpeg 合成 MP4。竖版 1080×1920，30 帧，15 秒。

## 重新生成

```bash
cd tools/video
npm pack @fontsource/noto-sans-sc@5.1.1 && tar -xzf fontsource-noto-sans-sc-*.tgz && mv package fonts/ 2>/dev/null || (mkdir -p fonts && mv package fonts/)
node render.js preview      # 先看 4 个关键画面（prev-*.png）
node render.js full         # 输出 450 帧到 frames/
ffmpeg -y -framerate 30 -i frames/%04d.png -f lavfi -i anullsrc=channel_layout=stereo:sample_rate=44100 \
  -shortest -c:v libx264 -profile:v high -pix_fmt yuv420p -crf 18 -preset slow -r 30 \
  -c:a aac -b:a 128k -movflags +faststart 精英签_Reels_15秒.mp4
```

## 改内容

文字都在 `elite.html` 里。每个元素的出现时间是 `animation-delay`，每个场景的淡出时间在 `#s1`–`#s3` 的 `out` 动画上。

## ⚠️ 需要按时更新

- "官方会员费 65 万泰铢起"：Bronze 套餐官方开放申请至 2026-12-31。过了这个日期，要按官方最新公布改价格，重新生成视频
