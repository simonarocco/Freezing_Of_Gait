from Calibration import *
import statistics
from Data_to_Signal import *

def test_signal(signal, min_range, peak_diff_range):
    i = 0
    j = 0
    k = 80

    shuffle_mins = []
    shuffle_abs_peak_diffs = []
    shuffle_mins_count = 0
    shuffle_abs_peak_diffs_count = 0
    for i in range(len(signal)):
        min = 0
        max = -30000
        abs_peak_diff = 0
        while j <= k:
            if signal[j] < min:
                min = signal[j]
            if signal[j] > max:
                max = signal[j]
            abs_peak_diff = max - min
            j += 1
        if min > min_range[1]:
            shuffle_mins.append(min)
            shuffle_mins_count += 1
        elif min_range[0] < min < min_range[1]:
            shuffle_mins.append(0)
            shuffle_mins_count = 0
        if abs_peak_diff < peak_diff_range[0] or abs_peak_diff > peak_diff_range[1]:
            shuffle_abs_peak_diffs.append(abs_peak_diff)
            shuffle_abs_peak_diffs_count += 1
        elif peak_diff_range[0] < abs_peak_diff < peak_diff_range[1]:
            shuffle_abs_peak_diffs.append(0)
            shuffle_abs_peak_diffs_count = 0
        k += 80
        if shuffle_mins_count >= 4 and shuffle_abs_peak_diffs_count >= 4:
            if statistics.mean(shuffle_abs_peak_diffs[-3:]) < 300:
                print("STOP DETECTED")
                return j
            else:
                print("SHUFFLE DETECTED")
                return j
            break
        if k > len(signal):
            break


signal_to_calibrate = data_to_signal("simona_walking1.csv", Acceleration.X)

calibrated_signal = calibrate(signal_to_calibrate)
min_range = calibrated_signal[0]
abs_peak_diff_range = calibrated_signal[1]

signal_to_test = data_to_signal("simona_walking2.csv", Acceleration.X)
test_signal(signal_to_test, min_range, abs_peak_diff_range)

signal_to_test = data_to_signal("simona_shuffling1.csv", Acceleration.X)
test_signal(signal_to_test, min_range, abs_peak_diff_range)

signal_to_test = data_to_signal("simona-stop.csv", Acceleration.X)
test_signal(signal_to_test, min_range, abs_peak_diff_range)
