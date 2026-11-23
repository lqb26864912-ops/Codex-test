# 音效

音效全部用 ffmpeg 合成，没有使用任何第三方音效素材，不存在版权问题。

生成命令：

```bash
ffmpeg -f lavfi -i "anoisesrc=d=0.7:c=pink:a=0.9" -af "highpass=f=300,lowpass=f=5000,afade=t=in:d=0.4:curve=exp,afade=t=out:st=0.4:d=0.3,volume=0.55,aformat=channel_layouts=stereo" whoosh.wav
ffmpeg -f lavfi -i "aevalsrc='0.5*sin(2*PI*(500+1800*exp(-t*35))*t)*exp(-t*22)':d=0.25:s=44100" -af "aformat=channel_layouts=stereo" pop.wav
ffmpeg -f lavfi -i "aevalsrc='0.28*(sin(2*PI*1318.5*t)+0.6*sin(2*PI*1975.5*t)+0.3*sin(2*PI*2637*t))*exp(-t*3.2)':d=1.4:s=44100" -af "aformat=channel_layouts=stereo" ding.wav
ffmpeg -f lavfi -i "aevalsrc='0.9*sin(2*PI*(55+40*exp(-t*8))*t)*exp(-t*3.5)':d=1.2:s=44100" -f lavfi -i "anoisesrc=d=0.3:c=brown:a=0.6" -filter_complex "[1:a]afade=t=out:d=0.3,lowpass=f=900[n];[0:a][n]amix=inputs=2:normalize=0,aformat=channel_layouts=stereo" boom.wav
```

- boom：开头的低音冲击
- whoosh：每次切镜头前 0.4 秒的"嗖"声
- pop：段落标签出现时的轻"啵"声
- ding：结尾按钮出现时的提示音

`mix.py` 按切点时间把音效混进视频。
