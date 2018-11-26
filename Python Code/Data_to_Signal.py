import pandas as pd
from enum import Enum
import numpy as np

class Acceleration(Enum):
    X = "X Acceleration"
    Y = "Y Acceleration"

def get_signal(file_path, accel_type):
    df = pd.read_csv(file_path)
    x_accel = df['AcX']
    y_accel = df['AcY']
    if accel_type == Acceleration.X:
        return x_accel
    elif accel_type == Acceleration.Y:
        return y_accel

def smooth_signal(signal, window_size):
    window = np.array([np.nan] * window_size)
    smoothed_signal = []
    for i in range(len(signal)):
        window[:-1] = window[1:]
        window[-1] = signal[i]
        smoothed_signal.append(np.nanmean(window))
    return smoothed_signal

def data_to_signal(file_path, accel_type):
    signal = get_signal(file_path, accel_type)
    return smooth_signal(signal, 3)
