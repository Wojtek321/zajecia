import requests
from netCDF4 import Dataset
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import convolve
from scipy.io import wavfile
import sounddevice as sd
import time
from filters import lowpass_filter, highpass_filter
from gcc_phat import gcc_phat
from scipy.signal import correlate



# URL = "http://sofacoustics.org/data/database/mit/mit_kemar_normal_pinna.sofa"
# data = requests.get(URL).content
# open("mit.sofa", "wb").write(data)
TIME = 4

# lewe ucho index - 0
# prawe ucho index - 1


sofa_file = Dataset("mit.sofa", "r", format="NETCDF4")
# print(sofa_file)
# print(sofa_file["Data.IR"])

ARR = sofa_file['SourcePosition'][:]

# for i in range(len(ARR)):
#     if ARR[i,1] == 0:
#         print(f"[{i}] ", ARR[i])

def measurement_number(az):
    condition1 = (ARR[:,0] == az)
    condition2 = (ARR[:,1] == 0)

    row_indices = np.where(np.all(np.logical_and(condition1[:, None], condition2[:, None]), axis=1))[0]
    return row_indices[0]





idx = measurement_number(90)

H_l = sofa_file["Data.IR"][idx,0,:]
H_r = sofa_file["Data.IR"][idx,1,:]


_, trumpet = wavfile.read("Trumpet.wav")
trumpet = trumpet/(np.max(np.abs(trumpet)))
trumpet = trumpet[:TIME*44100]


Y_l = convolve(trumpet, H_l, mode="same")
Y_r = convolve(trumpet, H_r, mode="same")


def ITD(Y_l, Y_r, fs=44100):
    Y_l = lowpass_filter(Y_l)
    Y_r = lowpass_filter(Y_r)

    i = np.argmax(Y_l)
    j = np.argmax(Y_r)

    return np.abs(i-j) / fs

    # itd, _ = gcc_phat(Y_r, Y_l)
    # return itd
    # cc = correlate(Y_r, Y_l, mode='full')
    # idx_lag = np.argmax(np.abs(cc))
    # toa_diff = idx_lag - 512
    #
    #
    # toa_diff = toa_diff / fs
    # return toa_diff


def ILD(Y_l, Y_r):
    l = sum(Y_l)
    r = sum(Y_r)

    return 20*np.log10(r/l)




print(ITD(Y_l, Y_r))
# print(ILD(Y_l, Y_r))


# def azimuth(ITD):
#     return np.degrees(np.arctan2(itd * 343, 0.18))

# fig, axs = plt.subplots(1, 2)
# fig.set_size_inches(14, 6)
# ax = axs[0]; ax.plot(fft(Y_l)); ax.set_xlim((0, 20000))
# ax = axs[1]; ax.plot(fft(lowpass_filter(Y_l))); ax.set_xlim((0, 20000))
# fig.set_tight_layout(tight=True)
# plt.savefig("fft1.png")
#
# fig, axs = plt.subplots(1, 2)
# fig.set_size_inches(14, 6)
# ax = axs[0]; ax.plot(fft(Y_l)); ax.set_xlim((0, 20000))
# ax = axs[1]; ax.plot(fft(highpass_filter(Y_l))); ax.set_xlim((0, 20000))
# fig.set_tight_layout(tight=True)
# plt.savefig("fft2.png")















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

