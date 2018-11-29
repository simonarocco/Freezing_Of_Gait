import pandas as pd
from enum import Enum
import numpy as np
import serial
from Serial_Monitor_Reading import process_string

# enum class for accelerations
class Acceleration(Enum):
    X = "X Acceleration"
    Y = "Y Acceleration"


def get_raw_signal(accel_type):
    ser = serial.Serial("/dev/cu.usbmodem1451", 9600)
    ser.reset_input_buffer()
    acz = []
    acy = []
    acx = []
    count = 0
    while count <= 240:
        raw_string = str(ser.readline())
        if "Acc z" in raw_string:
            acz.append(process_string(raw_string))
        elif "Acc y" in raw_string:
            acy.append(process_string(raw_string))
        elif "Acc x" in raw_string:
            acx.append(process_string(raw_string))
    return acx[:80] if accel_type == Acceleration.X else acy[:80]

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

def data_to_signal_real_time(accel_type):
    signal = get_raw_signal(accel_type)
    return smooth_signal(signal, 6)

def data_to_signal(file_path, accel_type):
    signal = get_signal(file_path, accel_type)
    return smooth_signal(signal, 6)
