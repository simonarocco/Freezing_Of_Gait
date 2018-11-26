import pandas as pd
from enum import Enum
import matplotlib.pyplot as plt

class Acceleration(Enum):
    X = "X Acceleration"
    Y = "Y Acceleration"

def get_signal_by_accel(file_path, accel_type):
    signal = pd.read_csv(file_path)
    x_accel = signal['AcX']
    y_accel = signal['AcY']
    if accel_type == Acceleration.X:
        return x_accel
    elif accel_type == Acceleration.Y:
        return y_accel

def get_peaks(accel_signal):
    current_slope = 0
    peaks = []
    for i in range(len(accel_signal)):
        if i != (len(accel_signal) - 1):
            prev_slope = current_slope
            current_slope = accel_signal[i+1] - accel_signal[i]
            if (current_slope > 0 and prev_slope < 0) or (current_slope < 0 and prev_slope > 0) or (current_slope == 0):
                peak_index_val = []
                peak_index_val.append(i)
                peak_index_val.append(accel_signal[i])
                peaks.append(peak_index_val)
    return peaks

def get_max_peaks(accel_type, signal):
    if accel_type == Acceleration.Y:
        y_accel = get_signal_by_accel(signal, accel_type)
        y_accel_peaks = get_peaks(y_accel)
        max_peaks = []
        max_peaks_index = []
        max_peaks_value = []
        for peak in y_accel_peaks:
            if peak[1] > 20000:
                max_peaks_index_val = []
                max_peaks_index_val.append(peak[0])
                max_peaks_index_val.append(peak[1])
                max_peaks_index.append(peak[0])
                max_peaks_value.append(peak[1])
                max_peaks.append(max_peaks_index_val)
        plt.plot(y_accel)
        plt.scatter(max_peaks_index, max_peaks_value)
        plt.show()
        return max_peaks
    else: return 0

def get_min_peaks(accel_type, signal):
    if accel_type == Acceleration.Y:
        y_accel = get_signal_by_accel(signal, accel_type)
        y_accel_peaks = get_peaks(y_accel)
        min_peaks = []
        min_peaks_index = []
        min_peaks_value = []
        for i in range(len(y_accel_peaks)):
            peak = y_accel_peaks[i]
            if peak[1] < -31000:
                j = i
                while j < (len(y_accel_peaks) - 1):
                    next_peak = y_accel_peaks[j+1]
                    if next_peak[1] > 0:
                        first_next_positive_peak = next_peak[1]
                        break
                    else: j += 1
                if first_next_positive_peak > 20000:
                    last_peak = min_peaks[len(min_peaks) - 1]
                    print(peak[0])
                    print(last_peak[0])
                    exit()
                    if peak[0] - last_peak[0] > 50:
                        min_peaks_index_val = []
                        min_peaks_index_val.append(peak[0])
                        min_peaks_index_val.append(peak[1])
                        min_peaks_index.append(peak[0])
                        min_peaks_value.append(peak[1])
                        min_peaks.append(min_peaks_index_val)
        plt.plot(y_accel)
        plt.scatter(min_peaks_index, min_peaks_value)
        plt.show()
        return min_peaks
    else: return 0

#get_max_peaks(Acceleration.Y, "simona_walking1.csv")
#get_min_peaks(Acceleration.Y, "simona_walking1.csv")

#get_max_peaks(Acceleration.Y, "simona_walking2.csv")
#get_min_peaks(Acceleration.Y, "simona_walking2.csv")

#get_max_peaks(Acceleration.Y, "simona_walking3.csv")
get_min_peaks(Acceleration.Y, "simona_walking3.csv")

#get_max_peaks(Acceleration.Y, "simona_walking4.csv")
#get_min_peaks(Acceleration.Y, "simona_walking4.csv")