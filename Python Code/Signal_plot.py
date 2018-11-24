import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_signal(signal_data, accel_type):
    sample_number = len(signal_data)
    spacing = np.linspace(0, 10, sample_number)
    plt.xlabel("Time")
    plt.ylabel("Acceleration")
    plt.title(accel_type)
    plt.plot(spacing, signal_data, 'm')
    plt.show()

def create_signal(file_path):
    df = pd.read_csv(file_path)
    x_accel = df['AcX']
    y_accel = df['AcY']
    plot_signal(x_accel, "X Acceleration")
    plot_signal(y_accel, 'Y Acceleration')

create_signal("simona_walking1.csv")
create_signal("simona_walking2.csv")
create_signal("simona_walking3.csv")
create_signal("simona_walking4.csv")
create_signal("simona_shuffling1.csv")
create_signal("simona_shuffling2.csv")
create_signal("simona_shuffling3.csv")
create_signal("simona_shuffling4.csv")
create_signal("simona_shuffling5.csv")
