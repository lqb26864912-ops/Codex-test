import subprocess, sys
def mix(video, out, events, dur):
    ins = ['-i', video]; parts = []; labels = []
    for k, (f, t, vol) in enumerate(events):
        ins += ['-i', f]
        ms = max(0, int(t * 1000))
        parts.append('[%d:a]volume=%.2f,adelay=%d|%d[e%d]' % (k + 1, vol, ms, ms, k)); labels.append('[e%d]' % k)
    parts.append('anullsrc=channel_layout=stereo:sample_rate=44100,atrim=duration=%.3f[base]' % dur)
    parts.append('[base]' + ''.join(labels) + 'amix=inputs=%d:normalize=0:duration=first,alimiter=limit=0.7[a]' % (len(labels) + 1))
    cmd = ['ffmpeg', '-loglevel', 'error', '-y'] + ins + ['-filter_complex', ';'.join(parts), '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', out]
    subprocess.run(cmd, check=True)

def events(cuts, end_start):
    ev = [('boom.wav', 0.0, 0.8)]
    for c in cuts:
        ev.append(('whoosh.wav', c - 0.4, 0.9))
        ev.append(('pop.wav', c + 0.1, 0.7))
    ev.append(('whoosh.wav', end_start - 0.4, 0.9))
    ev.append(('pop.wav', end_start + 0.05, 0.8))      # logo pops in
    ev.append(('ding.wav', end_start + 0.9, 0.8))      # CTA button
    return ev

V = '../../video/'
mix(V + '曼谷公寓探访_抖音版_32秒.mp4', V + '曼谷公寓探访_抖音版_音效.mp4', events([2.5, 6.47, 12.27, 19.27, 23.77, 26.47], 28.8), 32.3)
mix(V + '曼谷公寓探访_38秒.mp4', V + '曼谷公寓探访_小红书版_音效.mp4', events([3.0, 6.97, 12.77, 19.77, 28.27, 31.97], 34.3), 37.8)
print('ok')
