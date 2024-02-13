from netCDF4 import Dataset
import numpy as np
from scipy.signal import convolve, correlate
from scipy.io import wavfile
import sounddevice as sd
from librosa import resample
from ITD_ILD import ITD, ILD
import matplotlib.pyplot as plt
import requests


# URL = "https://sofacoustics.org/data/database/mit/mit_kemar_normal_pinna.sofa"
# URL = "https://sofacoustics.org/data/database/sadie/H3_48K_24bit_256tap_FIR_SOFA.sofa"
# data = requests.get(URL).content
# open("sofa_files/sadie.sofa", "wb").write(data)


TIME = 3

# lewe ucho index - 0
# prawe ucho index - 1


sofa_file = Dataset("sofa_files/mit.sofa", "r", format="NETCDF4")
sofa_fs =  sofa_file['Data.SamplingRate'][:][0]
ears_distance = sofa_file['ReceiverPosition'][1, 1] - sofa_file['ReceiverPosition'][0, 1]
print(f"fs: {sofa_fs}")
print(f"distance: {ears_distance}")

ARR = sofa_file['SourcePosition'][:]



def measurement_number(az):
    condition1 = (ARR[:,0] == az)
    condition2 = (ARR[:,1] == 0)

    row_indices = np.where(np.all(np.logical_and(condition1[:, None], condition2[:, None]), axis=1))[0]
    return row_indices[0]





fs, signal = wavfile.read("signals/voice.wav")
signal = signal/(np.max(np.abs(signal)))
signal = signal[:TIME*fs]
signal = resample(signal, orig_sr=fs, target_sr=sofa_fs)

# for i in range(710):
#     if ARR[i, 1]==0:
#         print(ARR[i])



angles = []
itds = []
ilds = []

for angle in range(0, 360, 5):
    angles.append(angle)

    idx = measurement_number(angle)

    H_l = sofa_file["Data.IR"][idx,0,:]
    H_r = sofa_file["Data.IR"][idx,1,:]

    Y_l = convolve(signal, H_l)
    Y_r = convolve(signal, H_r)

    itd = ITD(Y_l, Y_r)
    itds.append(itd)
    ild = ILD(Y_l, Y_r)
    ilds.append(ild)

x = np.column_stack((itds, ilds))
print(x)

# fig, axs = plt.subplots(1, 2)
# fig.set_size_inches(18, 9)
# ax = axs[0]; ax.stem(angles, itds); ax.set_title("mit.sofa ITD - same IRs"); ax.set_xlabel("angle [°]"); ax.set_ylabel("time [s]")
# ax = axs[1]; ax.stem(angles, ilds); ax.set_title("mit.sofa ILD - same IRs"); ax.set_xlabel("angle [°]"); ax.set_ylabel("amplitude [dB]")
# fig.set_tight_layout(tight=True)
# plt.savefig("mit_itd_ild.png")




# angle = 90
#
# idx = measurement_number(angle)
# H_l = sofa_file["Data.IR"][idx,1,:]
# H_r = sofa_file["Data.IR"][idx,0,:]
#
#
#
#
# Y_l = convolve(signal, H_l)
# Y_r = convolve(signal, H_r)
#
# plt.plot(Y_l)
# plt.plot(Y_r)
# plt.show()
# itd = ITD(Y_l, Y_r, fs=sofa_fs)
# ild = ILD(Y_l, Y_r)
#
#
#
# print(ITD(Y_l, Y_r, fs=sofa_fs))
# print(ILD(Y_l, Y_r))
#
#
# sd.play(np.column_stack((Y_l, Y_r)), 44100)
# sd.wait()


