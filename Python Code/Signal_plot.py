import matplotlib.pyplot as plt
from Data_to_Signal import *

def plot_signal(signal_data, accel_type):
    plt.xlabel("Time")
    plt.ylabel("Acceleration")
    plt.title(accel_type)
    plt.plot(signal_data, 'm')
    plt.show()

signal = data_to_signal("simona_walking1.csv", Acceleration.Y)
plot_signal(signal, Acceleration.Y)

signal = data_to_signal("simona_walking2.csv", Acceleration.Y)
plot_signal(signal, Acceleration.Y)

signal = data_to_signal("simona_walking3.csv", Acceleration.Y)
plot_signal(signal, Acceleration.Y)

signal = data_to_signal("simona_walking4.csv", Acceleration.Y)
plot_signal(signal, Acceleration.Y)