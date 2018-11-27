from Data_to_Signal import *

def get_peaks(accel_signal):
    current_slope = 0
    peaks = []
    for i in range(len(accel_signal)):
        if i != (len(accel_signal) - 1):
            prev_slope = current_slope
            current_slope = accel_signal[i+1] - accel_signal[i]
            if (current_slope > 0 and prev_slope < 0) or (current_slope == 0):
                peak_index_val = []
                peak_index_val.append(i)
                peak_index_val.append(accel_signal[i])
                peaks.append(peak_index_val)
    return peaks

# will likely only use min peaks
"""
def get_max_peaks(signal):
    peaks = get_peaks(signal)
    max_peaks = []
    for peak in peaks:
        if peak[1] > 10000:
            max_peaks_index_val = []
            max_peaks_index_val.append(peak[0])
            max_peaks_index_val.append(peak[1])
            max_peaks.append(max_peaks_index_val)
    if not max_peaks:
        return 0
    else: return max_peaks
"""

def get_min_peaks(signal):
    peaks = get_peaks(signal)
    min_peaks = []
    for peak in peaks:
        if peak[1] < -25000:
            min_peaks_index_val = []
            min_peaks_index_val.append(peak[0])
            min_peaks_index_val.append(peak[1])
            min_peaks.append(min_peaks_index_val)
    if not min_peaks:
        return 0
    else: return min_peaks


