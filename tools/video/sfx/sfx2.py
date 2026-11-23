"""More natural sound effects: swept-filter whoosh with stereo pan, soft UI tap, marimba-like chime, light reverb."""
import numpy as np
from scipy.signal import fftconvolve
from scipy.io import wavfile
SR = 44100
rng = np.random.default_rng(7)

def pink(n):
    w = rng.standard_normal(n); f = np.fft.rfft(w); k = np.arange(len(f)); k[0] = 1
    return np.fft.irfft(f / np.sqrt(k), n)

def svf_bandpass(x, fc, q=1.2):
    """State-variable filter with a per-sample centre frequency (array)."""
    lp = bp = 0.0; out = np.empty_like(x); d = 1.0 / q
    for i in range(len(x)):
        f = 2 * np.sin(np.pi * min(fc[i], SR / 6) / SR)
        hp = x[i] - lp - d * bp; bp += f * hp; lp += f * bp; out[i] = bp
    return out

def reverb(st, t=0.45, mix=0.18):
    n = int(SR * t); ir = rng.standard_normal(n) * np.exp(-np.linspace(0, 7, n)); ir /= np.abs(ir).sum() ** 0.5 * 8
    wet = np.stack([fftconvolve(st[:, c], ir)[:len(st)] for c in range(2)], 1)
    return st * (1 - mix) + wet * mix * 4

def norm(st, peak):
    return st / (np.abs(st).max() + 1e-9) * peak

def save(name, st, pad=0.5):
    st = np.vstack([st, np.zeros((int(SR * pad), 2))])
    wavfile.write(name, SR, (np.clip(st, -1, 1) * 32767).astype(np.int16))

def whoosh(dur=0.75, f0=350, f1=3200, peak=0.32):
    n = int(SR * dur); t = np.linspace(0, 1, n)
    x = pink(n)
    fc = f0 + (f1 - f0) * np.sin(np.pi * t) ** 1.5                 # sweep up then back down
    y = svf_bandpass(x, fc, q=1.4)
    env = np.sin(np.pi * np.clip(t / 0.95, 0, 1)) ** 2.2            # smooth swell
    y = y * env
    pan = np.clip(t * 1.4 - 0.2, 0, 1)                               # left to right
    st = np.stack([y * np.cos(pan * np.pi / 2), y * np.sin(pan * np.pi / 2)], 1)
    return norm(reverb(st, 0.35, 0.15), peak)

def tap(peak=0.22):
    n = int(SR * 0.12); t = np.arange(n) / SR
    click = svf_bandpass(rng.standard_normal(n), np.full(n, 3500.0), q=3) * np.exp(-t * 180)
    body = np.sin(2 * np.pi * 1150 * t) * np.exp(-t * 45) * 0.6
    y = click * 0.5 + body
    return norm(reverb(np.stack([y, y], 1), 0.25, 0.12), peak)

def note(freq, dur, amp):
    n = int(SR * dur); t = np.arange(n) / SR
    y = (np.sin(2 * np.pi * freq * t) * np.exp(-t * 4.5) + 0.35 * np.sin(2 * np.pi * freq * 4 * t) * np.exp(-t * 14)
         + 0.12 * np.sin(2 * np.pi * freq * 10 * t) * np.exp(-t * 30))
    y *= np.minimum(1, t / 0.004) * amp
    return y

def chime(peak=0.30):
    n = int(SR * 1.4); y = np.zeros(n)
    a = note(1046.5, 1.2, 1.0); y[:len(a)] += a                       # C6
    b = note(1568.0, 1.0, 0.8); s = int(SR * 0.12); y[s:s + len(b)] += b[:n - s]   # G6
    return norm(reverb(np.stack([y * 0.95, y], 1), 0.6, 0.22), peak)

def swell(dur=1.3, peak=0.22):
    n = int(SR * dur); t = np.linspace(0, 1, n)
    y = svf_bandpass(pink(n), 200 + 2500 * t ** 2, q=0.9) * (t ** 1.5) * np.exp(-((t - 0.85) ** 2) * 0) 
    y *= np.where(t > 0.85, np.cos((t - 0.85) / 0.15 * np.pi / 2), 1)
    return norm(reverb(np.stack([y, y], 1), 0.5, 0.2), peak)

save('whoosh2.wav', whoosh()); save('tap2.wav', tap()); save('chime2.wav', chime()); save('swell2.wav', swell())
print('ok')
