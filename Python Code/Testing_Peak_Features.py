from Signal_plot import *
from Peak_Tracker import *
from Data_to_Signal import *

mean_valley_interval = []
mean_valley_amplitude = []

def create_tracker(signal):
    tracker = PeakTracker(3, 4, -20000)
    for i in range(len(signal)):
        tracker.add_sample(signal[i])
    return tracker

signal = data_to_signal("simona_walking1.csv", Acceleration.Y)
smoothed_signal, min_valley_indices, min_valley_amplitudes = create_min_scatter_plot(signal)
tracker = create_tracker(smoothed_signal)
mean_valley_interval.append(tracker.get_mean_interval())
mean_valley_amplitude.append(tracker.get_mean_amplitude())
#plot_signal(smoothed_signal, Acceleration.Y, min_valley_indices, min_valley_amplitudes)

signal = data_to_signal("simona_walking2.csv", Acceleration.Y)
smoothed_signal, min_valley_indices, min_valley_amplitudes = create_min_scatter_plot(signal)
tracker = create_tracker(smoothed_signal)
mean_valley_interval.append(tracker.get_mean_interval())
mean_valley_amplitude.append(tracker.get_mean_amplitude())
#plot_signal(smoothed_signal, Acceleration.Y, min_valley_indices, min_valley_amplitudes)

signal = data_to_signal("simona_walking3.csv", Acceleration.Y)
smoothed_signal, min_valley_indices, min_valley_amplitudes = create_min_scatter_plot(signal)
tracker = create_tracker(smoothed_signal)
mean_valley_interval.append(tracker.get_mean_interval())
mean_valley_amplitude.append(tracker.get_mean_amplitude())
#plot_signal(smoothed_signal, Acceleration.Y, min_valley_indices, min_valley_amplitudes)

signal = data_to_signal("simona_walking4.csv", Acceleration.Y)
smoothed_signal, min_valley_indices, min_valley_amplitudes = create_min_scatter_plot(signal)
tracker = create_tracker(smoothed_signal)
mean_valley_interval.append(tracker.get_mean_interval())
mean_valley_amplitude.append(tracker.get_mean_amplitude())
#plot_signal(smoothed_signal, Acceleration.Y, min_valley_indices, min_valley_amplitudes)

print(mean_valley_amplitude)
print(mean_valley_interval)