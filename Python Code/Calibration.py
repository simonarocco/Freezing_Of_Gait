import statistics

def calibrate_mins(mins):
    mean = statistics.mean(mins)

    lower_bound = mean - 2000
    upper_bound = mean + 3000
    return [lower_bound, upper_bound]

def calibrate_abs_peak_diff(maxs, mins):
    peak_diffs = []
    for i in range(len(maxs)):
        peak_diffs.append(maxs[i] - mins[i])

    mean = statistics.mean(peak_diffs)
    lower_bound = mean - 5000
    upper_bound = mean + 2000
    return [lower_bound, upper_bound]

def calibrate(signal):

    minimums = []
    maximums = []

    i = 1
    j = 0
    k = 80
    while i <= 9:
        min = 0
        max = -30000
        while j <= k:
            if signal[j] < min:
                min = signal[j]
            if signal[j] > max:
                max = signal[j]
            j += 1
        if i > 4:
            minimums.append(min)
            maximums.append(max)
        i += 1
        k += 80

    return calibrate_mins(minimums), calibrate_abs_peak_diff(maximums, minimums)
