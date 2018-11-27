import numpy as np

def detect_valley(self, current_smoothed_sample, current_change):
    if (current_smoothed_sample < self.valley_max) and ((self.last_change <= 0 and current_change > 0) or current_change == 0):
        self.valley_amplitudes[:-1] = self.valley_amplitudes[1:]
        self.valley_amplitudes[-1] = self.last_smoothed_sample
        self.tot_valley_amplitudes.append(self.last_smoothed_sample)

        self.valley_times[:-1] = self.valley_times[1:]
        self.valley_times[-1] = self.sample_number-1
        self.tot_valley_times.append(self.sample_number-1)

class PeakTracker:
    """
    Detects valleys in a signal online (as new samples are received), and reports
    average amplitude and inter-valley intervals of the most recent valleys.
    """

    def __init__(self, n_valleys, n_smooth, valley_max):
        """
        :param n_valleys: number of recent valleys over which to report average
          amplitude and interval
        :param n_smooth: number of signal samples to average, to create a
          smoothed signal prior to peak detection (this helps to
          avoid detecting valleys that are just noise)
        :param valley_max: maximum amplitude of valleys (larger valleys are
          ignored)
        """

        self.sample_number = 0
        self.valley_max = valley_max

        self.smoothed_signal = []
        self.tot_valley_amplitudes = []
        self.tot_valley_times = []

        self.window = np.array([np.nan] * n_smooth)
        self.valley_amplitudes = np.array([np.nan] * n_valleys)
        self.valley_times = np.array([np.nan] * n_valleys)

        self.last_smoothed_sample = 0
        self.last_change = -1

    def add_sample(self, sample):
        # update rolling window
        self.window[:-1] = self.window[1:]
        self.window[-1] = sample

        smoothed_sample = np.nanmean(self.window)
        self.smoothed_signal.append(smoothed_sample)
        change = smoothed_sample - self.last_smoothed_sample

        detect_valley(self, smoothed_sample, change)

        self.last_smoothed_sample = smoothed_sample
        self.last_change = change
        self.sample_number += 1

    def get_mean_amplitude(self):
        return np.nanmean(self.valley_amplitudes)

    def get_mean_interval(self):
        return np.nanmean(np.diff(self.valley_times))
