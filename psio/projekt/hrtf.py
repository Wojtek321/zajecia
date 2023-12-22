import requests
from netCDF4 import Dataset
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import convolve, butter, lfilter
from scipy.io import wavfile
import sounddevice as sd
import time


# URL = "http://sofacoustics.org/data/database/mit/mit_kemar_normal_pinna.sofa"
# data = requests.get(URL).content
# open("mit.sofa", "wb").write(data)

FS = 44100
LOW_FREQ_CUTOFF = 1000
HIGH_FREQ_CUTOFF = 3000


# designing lowpass filter
normal_low_cutoff = LOW_FREQ_CUTOFF/FS/2
coefficients = butter(4, normal_low_cutoff, btype='low', analog=False)
b_low = coefficients[0]
a_low = coefficients[1]


# designing highpass filter
normal_high_cutoff = HIGH_FREQ_CUTOFF/FS/2
coefficients = butter(4, normal_low_cutoff, btype='high', analog=False)
b_high = coefficients[0]
a_high = coefficients[1]


def lowpass_filter(signal):
    return lfilter(b_low, a_low, signal)


def highpass_filter(signal):
    return lfilter(b_high, a_high, signal)


# lewe ucho index - 0
# prawe ucho index - 1

sofa_file = Dataset("mit.sofa", "r", format="NETCDF4")

ARR = sofa_file['SourcePosition'][:]

# for i in range(len(ARR)):
#     if ARR[i,1] == 0:
#         print(f"[{i}] ", ARR[i])

def measurement_number(az):
    condition1 = (ARR[:,0] == az)
    condition2 = (ARR[:,1] == 0)

    row_indices = np.where(np.all(np.logical_and(condition1[:, None], condition2[:, None]), axis=1))[0]
    return row_indices[0]





idx = measurement_number(10)

H_l = sofa_file["Data.IR"][idx,0,:]
H_r = sofa_file["Data.IR"][idx,1,:]


_, trumpet = wavfile.read("Trumpet.wav")
trumpet = trumpet/(np.max(np.abs(trumpet)))

Y_l = convolve(trumpet, H_l, mode="same")[:132300]
Y_r = convolve(trumpet, H_r, mode="same")[:132300]

plt.plot(Y_r)
Y_r = lowpass_filter(Y_r)
plt.plot(Y_r)
plt.xlim((0, 10000))
plt.show()

# Y_l = Y_l/(np.max(np.abs(Y_l)))
# Y_r = Y_r/(np.max(np.abs(Y_r)))
# plt.plot(H_l, label='left')
# plt.plot(H_r, label='right')
# plt.title("H_l and H_r")
# plt.legend()
# plt.show()
# result = np.column_stack((Y_l, Y_r))
# print(result.shape)

# plt.plot(Y_l, label='left')
# plt.plot(Y_r, label='right')
# plt.title("Y_l and Y_r")
# plt.legend()
# plt.show()

# sd.play(result, 44100)
# sd.wait()
# sd.play(Y_l, 44100)
# sd.wait()
# time.sleep(1)
# sd.play(Y_r, 44100)
# sd.wait()

