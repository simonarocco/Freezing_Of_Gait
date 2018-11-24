import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#from detect_peaks import detect_peaks

df1 = pd.read_csv("dani-gs1.csv")
col_1a = df1['AcX']
col_2a = df1['AcY']
col_3a = df1['AcZ']
df2 = pd.read_csv("dani-gs2.csv")
col_1b = df2['AcX']
col_2b = df2['AcY']
col_3b = df2['AcZ']
df3 = pd.read_csv("dani-gs3.csv")
col_1c = df3['AcX']
col_2c = df3['AcY']
col_3c = df3['AcZ']
df4 = pd.read_csv("dani-gs4.csv")
col_1d = df4['AcX']
col_2d = df4['AcY']
col_3d = df4['AcZ']

spacing = np.linspace(0, 10, 333)
plt.xlabel("Time")
plt.ylabel("Acceleration")
#session 5
plt.title("Shuffling - Session 1")
plt.plot(spacing, col_1a, 'm')
plt.plot(spacing, col_2a, 'c')
plt.plot(spacing, col_3a, 'r')
plt.show()
#session 6
plt.title("Shuffling - Session 2")
plt.plot(spacing, col_1b, 'm')
plt.plot(spacing, col_2b, 'c')
plt.plot(spacing, col_3b, 'r')
plt.show()
#session 7
plt.title("Shuffling - Session 3")
plt.plot(spacing, col_1c, 'm')
plt.plot(spacing, col_2c, 'c')
plt.plot(spacing, col_3c, 'r')
plt.show()
#session 8
plt.title("Shuffling - Session 4")
plt.plot(spacing, col_1d, 'm')
plt.plot(spacing, col_2d, 'c')
plt.plot(spacing, col_3d, 'r')
plt.show()
#session 8
# peaks_session4 = detect_peaks(col_1d)
# for peak_indices in peaks_session4:
#     plt.plot(peak_indices/33, peaks_session4[peak_indices/33], marker='x', color='blue')

plt.title("Shuffling - cceleration in the X")
plt.plot(spacing, col_1b, 'm')
plt.show()
plt.title("Shuffling - Acceleration in the Y")
plt.plot(spacing, col_2b, 'c')
plt.show()
plt.title("Shuffling - Acceleration in the Z")
plt.plot(spacing, col_3b, 'r')
plt.show()