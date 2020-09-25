import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import matplotlib.pyplot as plt

# Utility functions
def count_ticks(sound, threshold):
    count = 0
    i = 0
    while i < len(sound):
        sample = sound[i]
        if sample > threshold:
            count += 1
            i += 1000
        else:
            i += 1
    return count

# Returns the index of the first peak
def find_first_peak(sound, threshold):
    peak_val = threshold
    max_i = None
    i = 0
    while i < len(sound):
        sample = sound[i]
        if sample > threshold:
            peak_val = max(sound[i:i+1000])
            return np.where(sound==peak_val)[0][0]
        else:
            i += 1
    return max_i

# Returns the index of the last peak
def find_last_peak(sound, threshold):
    i = len(sound) - 1
    max_i = None
    peak_val = threshold
    while i >= 0:
        sample = sound[i]
        if sample > threshold:
            peak_val = max(sound[i-1000:i])
            return np.where(sound==peak_val)[0][0]
        else:
            i -= 1
    return max_i

def find_threshold(sound, target_freq=6):
    # Perform binary search on threshold until we get within 5% of target freq
    upper_thresh = 1
    lower_thresh = 0
    thresh = 0.5
    last_freq = 0
    while True:
        trimmed = sound[find_first_peak(sound, thresh):find_last_peak(sound, thresh)]
        if len(trimmed)/fs <= 1:
            return 0
        freq = (count_ticks(trimmed, thresh) - 1) / (len(trimmed)/fs)
        if freq > target_freq * 1.05:
            thresh = (thresh + upper_thresh) / 2
            lower_thresh = thresh
        elif freq < target_freq * 0.95:
            thresh = (lower_thresh + thresh) / 2
            upper_thresh = thresh
        if abs(freq - target_freq) <= 0.05 * target_freq or abs(freq - last_freq) <= 0.0001:
            return thresh
        last_freq = freq


def get_beat_error(freq, target_freq):
    num_seconds_a_day = 24*60*60
    one_clock_incment = 1/target_freq
    num_clock_seconds_a_day = freq * num_seconds_a_day * one_clock_incment
    return num_clock_seconds_a_day - num_seconds_a_day


fs = 44100  # Sample rate
seconds = 3  # Duration of recording
# Channel L = index 0
# Channel R = index 1
# tick_threshold = 0.22
samples = []

while True:
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    # Take only one channel
    my_sound = myrecording[:,1]
    tick_threshold = find_threshold(my_sound)
    trimmed = my_sound[find_first_peak(my_sound, tick_threshold):find_last_peak(my_sound, tick_threshold)]
    if len(trimmed)/fs <= 1:
        print("Bad sample...")
        continue
    freq = (count_ticks(trimmed, tick_threshold) - 1) / (len(trimmed)/fs)
    beat_err = get_beat_error(freq, 6)
    if abs(beat_err) <= 300:
        samples.append(beat_err)
        mean = np.mean(samples)
        print(f"Beat error: {['','+'][beat_err >= 0]}{beat_err:.2f} s/day", f"avg: {['','+'][mean >= 0]}{mean:.2f}")
    else:
        print("Bad sample...")

