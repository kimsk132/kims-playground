import sounddevice as sd
from scipy.fftpack import fft
import numpy as np
import matplotlib.pyplot as plt

def get_beat_error(freq, target_freq=6):
    num_seconds_a_day = 24*60*60
    one_clock_incment = 1/target_freq
    num_clock_seconds_a_day = freq * num_seconds_a_day * one_clock_incment
    return num_clock_seconds_a_day - num_seconds_a_day

fs = 44100
seconds = 8

samples = []
while True:
    raw_recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    watch_recording = raw_recording[int(fs):,1]
    N = len(watch_recording)
    T = 1/fs
    yf = fft(watch_recording)
    xf = np.linspace(0.0, 1.0/(2.0*T), N//2)

    lower_i = 0
    upper_i = 0
    i = 0
    while xf[i] < 6.5:
        if xf[i] < 5.5 and xf[i+1] >= 5.5:
            lower_i = i
        i += 1
    upper_i = i

    freq = xf[np.where(max((2.0/N * np.abs(yf[0:N//2]))[lower_i:upper_i]) == (2.0/N * np.abs(yf[0:N//2])))[0][0]]
    print(f"Detected freq: {freq}")
    beat_err = get_beat_error(freq)
    samples.append(beat_err)
    mean = np.mean(samples)
    print(f"Beat error: {['','+'][beat_err >= 0]}{beat_err:.2f} s/day", f"avg: {['','+'][mean >= 0]}{mean:.2f}")
