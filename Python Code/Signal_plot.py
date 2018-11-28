import matplotlib.pyplot as plt
from Scripts_For_Project.Peak_Tracker import *

def create_min_scatter_plot(signal):
    tracker = PeakTracker(3, 6, -20000)
    for i in range(len(signal)):
        tracker.add_sample(signal[i])
    smoothed_signal = tracker.smoothed_signal
    min_valley_indices = tracker.tot_valley_times
    min_valley_amplitudes = tracker.tot_valley_amplitudes
    return smoothed_signal, min_valley_indices, min_valley_amplitudes

def plot_signal(signal_data, accel_type, scatter_x = None, scatter_y = None):
    plt.xlabel("Time")
    plt.ylabel("Acceleration")
    plt.title(accel_type)
    plt.plot(signal_data, 'm')
    if (scatter_x and scatter_y) is not None:
        plt.scatter(scatter_x, scatter_y)
    plt.show()
