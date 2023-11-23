import numpy as np
import matplotlib.pyplot as plt
import wave
import struct
import sounddevice as sd
from scipy.signal import square, sawtooth, periodogram


# t = 5
# f = 1000
# fs = 8000
# n = np.arange(0, t, 1/fs)
#
# noise = np.random.normal(0, 1, len(n))
# sin = np.sin(2*np.pi*f*n)
# czesetotliwosc_zmienna = np.linspace(0, 1000, len(n))
# sin_zmienny = np.sin(2 * np.pi * czesetotliwosc_zmienna * n)
# with wave.open("mowa.wav", 'r') as file:
#     fs = file.getframerate()
#     n_frames = file.getnframes()
#     data = file.readframes(n_frames)
#     sample_width = file.getsampwidth()
#     samples = struct.unpack(f"{n_frames}h", data)
#     max_amplitude = np.max(np.abs(samples))
#     samples = samples / max_amplitude
#
# def moc_sygnalu(alpha, signal):
#     power = []
#     power.append(0)
#
#     for i in range(1, len(signal)):
#         sample = signal[i]
#         power.append(alpha*power[i-1] + (1-alpha)*sample*sample)
#     return power
#
#
# noise_power = moc_sygnalu(0.999, noise)
# sin_power = moc_sygnalu(0.999, sin)
# sin_zmienny_power = moc_sygnalu(0.999, sin_zmienny)
# samples_power = moc_sygnalu(0.999, samples)
#
# fig, axs = plt.subplots(4, 2)
# fig.set_size_inches(18, 16)
# ax = axs[0,0]; ax.plot(n, noise); ax.set_title("Szum gaussowski"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Amplituda")
# ax = axs[0,1]; ax.plot(n, noise_power); ax.set_title("Szum gaussowski - Obwiednia mocy, alpha=0.999"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Moc")
# ax = axs[1,0]; ax.plot(n, sin); ax.set_title("Sygnal sinusoidalny o stalej czestotliwosci"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Amplituda")
# ax = axs[1,1]; ax.plot(n, sin_power); ax.set_title("Sygnal sinusoidalny o stalej czestotliwosci - Obwiednia mocy, alpha=0.999"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Moc")
# ax = axs[2,0]; ax.plot(n, sin_zmienny); ax.set_title("Sygnal o zmiennej czestotliwosci"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Amplituda")
# ax = axs[2,1]; ax.plot(n, sin_zmienny_power); ax.set_title("Sygnal o zmiennej czestotliwosci - Obwiednia mocy, alpha=0.999"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Moc")
# ax = axs[3,0]; ax.plot(n, samples); ax.set_title("Sygnal mowy"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Amplituda")
# ax = axs[3,1]; ax.plot(n, samples_power); ax.set_title("Sygnal mowy - Obwiednia mocy, alpha=0.999"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Moc")
# fig.set_tight_layout(tight=True)
# plt.savefig("Zadanie1_1.png")
#
#
# noise_power = moc_sygnalu(0.99, noise)
# sin_power = moc_sygnalu(0.99, sin)
# sin_zmienny_power = moc_sygnalu(0.99, sin_zmienny)
# samples_power = moc_sygnalu(0.99, samples)
#
# fig, axs = plt.subplots(4, 2)
# fig.set_size_inches(18, 16)
# ax = axs[0,0]; ax.plot(n, noise); ax.set_title("Szum gaussowski"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Amplituda")
# ax = axs[0,1]; ax.plot(n, noise_power); ax.set_title("Szum gaussowski - Obwiednia mocy, alpha=0.99"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Moc")
# ax = axs[1,0]; ax.plot(n, sin); ax.set_title("Sygnal sinusoidalny o stalej czestotliwosci"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Amplituda")
# ax = axs[1,1]; ax.plot(n, sin_power); ax.set_title("Sygnal sinusoidalny o stalej czestotliwosci - Obwiednia mocy, alpha=0.99"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Moc")
# ax = axs[2,0]; ax.plot(n, sin_zmienny); ax.set_title("Sygnal o zmiennej czestotliwosci"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Amplituda")
# ax = axs[2,1]; ax.plot(n, sin_zmienny_power); ax.set_title("Sygnal o zmiennej czestotliwosci - Obwiednia mocy, alpha=0.99"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Moc")
# ax = axs[3,0]; ax.plot(n, samples); ax.set_title("Sygnal mowy"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Amplituda")
# ax = axs[3,1]; ax.plot(n, samples_power); ax.set_title("Sygnal mowy - Obwiednia mocy, alpha=0.99"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Moc")
# fig.set_tight_layout(tight=True)
# plt.savefig("Zadanie1_2.png")
#
#
# noise_power = moc_sygnalu(0.001, noise)
# sin_power = moc_sygnalu(0.001, sin)
# sin_zmienny_power = moc_sygnalu(0.001, sin_zmienny)
# samples_power = moc_sygnalu(0.001, samples)
#
# fig, axs = plt.subplots(4, 2)
# fig.set_size_inches(18, 16)
# ax = axs[0,0]; ax.plot(n, noise); ax.set_title("Szum gaussowski"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Amplituda")
# ax = axs[0,1]; ax.plot(n, noise_power); ax.set_title("Szum gaussowski - Obwiednia mocy, alpha=0.001"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Moc")
# ax = axs[1,0]; ax.plot(n, sin); ax.set_title("Sygnal sinusoidalny o stalej czestotliwosci"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Amplituda")
# ax = axs[1,1]; ax.plot(n, sin_power); ax.set_title("Sygnal sinusoidalny o stalej czestotliwosci - Obwiednia mocy, alpha=0.001"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Moc")
# ax = axs[2,0]; ax.plot(n, sin_zmienny); ax.set_title("Sygnal o zmiennej czestotliwosci"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Amplituda")
# ax = axs[2,1]; ax.plot(n, sin_zmienny_power); ax.set_title("Sygnal o zmiennej czestotliwosci - Obwiednia mocy, alpha=0.001"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Moc")
# ax = axs[3,0]; ax.plot(n, samples); ax.set_title("Sygnal mowy"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Amplituda")
# ax = axs[3,1]; ax.plot(n, samples_power); ax.set_title("Sygnal mowy - Obwiednia mocy, alpha=0.001"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Moc")
# fig.set_tight_layout(tight=True)
# plt.savefig("Zadanie1_3.png")












f = 1000
fs = 16000
t = 2
n = np.arange(0, t, 1/fs)
frequency = np.linspace(1000, 2000, len(n))

sin = np.sin(2*np.pi * f * t * n)
sq = square(2*np.pi * f * t * n)
traingle = sawtooth(2*np.pi * f * t * n, width=0.5)
saw = sawtooth(2*np.pi * f * t * n)
noise = np.random.normal(0, 1, fs*t)
max_amplitude = np.max(np.abs(noise))
noise = noise / max_amplitude
sin_var = np.sin(2*np.pi * frequency * t * n)
with wave.open("mowa.wav", 'r') as file:
    n_frames = file.getnframes()
    fs_mowy = file.getframerate()
    t_mowy = n_frames/fs_mowy
    n_mowy = np.arange(0, t_mowy, 1/fs_mowy)
    data = file.readframes(n_frames)
    mowa = struct.unpack(f"{n_frames}h", data)
    max_amplitude = np.max(np.abs(mowa))
    mowa = mowa / max_amplitude
with wave.open("muzyka.wav", 'r') as file:
    liczba_kanalow = file.getnchannels()
    liczba_bitow_na_probke = file.getsampwidth()
    n_frames = file.getnframes()

    fs_muzyki = file.getframerate()
    t_muzyki = n_frames / fs_muzyki
    n_muzyki = np.arange(0, t_muzyki-(1/fs_muzyki), 1 / fs_muzyki)

<<<<<<< HEAD
    for i in range(1, len(signal)):
        sample = signal[i]
        power.append(alpha*power[i-1] + (1-alpha)*sample*sample)
    return power



noise_power = moc_sygnalu(0.999, noise)
sin_power = moc_sygnalu(0.999, sin)
sin_zmienny_power = moc_sygnalu(0.999, sin_zmienny)
samples_power = moc_sygnalu(0.999, samples)

fig, axs = plt.subplots(4, 2)
fig.set_size_inches(18, 16)
ax = axs[0,0]; ax.plot(n, noise); ax.set_title("Szum gaussowski"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Amplituda")
ax = axs[0,1]; ax.plot(n, noise_power); ax.set_title("Szum gaussowski - Obwiednia mocy, alpha=0.999"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Moc")
ax = axs[1,0]; ax.plot(n, sin); ax.set_title("Sygnal sinusoidalny o stalej czestotliwosci"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Amplituda")
ax = axs[1,1]; ax.plot(n, sin_power); ax.set_title("Sygnal sinusoidalny o stalej czestotliwosci - Obwiednia mocy, alpha=0.999"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Moc")
ax = axs[2,0]; ax.plot(n, sin_zmienny); ax.set_title("Sygnal o zmiennej czestotliwosci"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Amplituda")
ax = axs[2,1]; ax.plot(n, sin_zmienny_power); ax.set_title("Sygnal o zmiennej czestotliwosci - Obwiednia mocy, alpha=0.999"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Moc")
ax = axs[3,0]; ax.plot(n, samples); ax.set_title("Sygnal mowy"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Amplituda")
ax = axs[3,1]; ax.plot(n, samples_power); ax.set_title("Sygnal mowy - Obwiednia mocy, alpha=0.999"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Moc")
=======
    data = file.readframes(n_frames)
    muzyka = struct.unpack(f"{n_frames * liczba_kanalow}h", data)
    muzyka = np.array(muzyka).reshape((-1, liczba_kanalow))
    muzyka = np.sum(muzyka, axis=1)
    max_amplitude = np.max(np.abs(muzyka))
    muzyka = muzyka / max_amplitude



fig, axs = plt.subplots(8,2)
fig.set_size_inches(18, 16)
ax = axs[0,0]; ax.plot(n, sin); ax.set_xlim(0, 0.001)
ax = axs[1,0]; ax.plot(n, sq); ax.set_xlim(0, 0.001)
ax = axs[2,0]; ax.plot(n, traingle); ax.set_xlim(0, 0.001)
ax = axs[3,0]; ax.plot(n, saw); ax.set_xlim(0, 0.001)
ax = axs[4,0]; ax.plot(n, noise); ax.set_xlim(0, 0.001)
ax = axs[5,0]; ax.plot(n, sin_var); ax.set_xlim(0, 0.001)
ax = axs[6,0]; ax.plot(n_mowy, mowa)
ax = axs[7,0]; ax.plot(n_muzyki, muzyka)
>>>>>>> 8e861ea3f420eff0a26226297d4aefe631f0b052
fig.set_tight_layout(tight=True)
plt.savefig("Zadanie2_1.png")


<<<<<<< HEAD

noise_power = moc_sygnalu(0.99, noise)
sin_power = moc_sygnalu(0.99, sin)
sin_zmienny_power = moc_sygnalu(0.99, sin_zmienny)
samples_power = moc_sygnalu(0.99, samples)

fig, axs = plt.subplots(4, 2)
fig.set_size_inches(18, 16)
ax = axs[0,0]; ax.plot(n, noise); ax.set_title("Szum gaussowski"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Amplituda")
ax = axs[0,1]; ax.plot(n, noise_power); ax.set_title("Szum gaussowski - Obwiednia mocy, alpha=0.99"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Moc")
ax = axs[1,0]; ax.plot(n, sin); ax.set_title("Sygnal sinusoidalny o stalej czestotliwosci"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Amplituda")
ax = axs[1,1]; ax.plot(n, sin_power); ax.set_title("Sygnal sinusoidalny o stalej czestotliwosci - Obwiednia mocy, alpha=0.99"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Moc")
ax = axs[2,0]; ax.plot(n, sin_zmienny); ax.set_title("Sygnal o zmiennej czestotliwosci"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Amplituda")
ax = axs[2,1]; ax.plot(n, sin_zmienny_power); ax.set_title("Sygnal o zmiennej czestotliwosci - Obwiednia mocy, alpha=0.99"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Moc")
ax = axs[3,0]; ax.plot(n, samples); ax.set_title("Sygnal mowy"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Amplituda")
ax = axs[3,1]; ax.plot(n, samples_power); ax.set_title("Sygnal mowy - Obwiednia mocy, alpha=0.99"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Moc")
fig.set_tight_layout(tight=True)
plt.savefig("Zadanie1_2.png")



noise_power = moc_sygnalu(0.001, noise)
sin_power = moc_sygnalu(0.001, sin)
sin_zmienny_power = moc_sygnalu(0.001, sin_zmienny)
samples_power = moc_sygnalu(0.001, samples)

fig, axs = plt.subplots(4, 2)
fig.set_size_inches(18, 16)
ax = axs[0,0]; ax.plot(n, noise); ax.set_title("Szum gaussowski"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Amplituda")
ax = axs[0,1]; ax.plot(n, noise_power); ax.set_title("Szum gaussowski - Obwiednia mocy, alpha=0.001"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Moc")
ax = axs[1,0]; ax.plot(n, sin); ax.set_title("Sygnal sinusoidalny o stalej czestotliwosci"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Amplituda")
ax = axs[1,1]; ax.plot(n, sin_power); ax.set_title("Sygnal sinusoidalny o stalej czestotliwosci - Obwiednia mocy, alpha=0.001"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Moc")
ax = axs[2,0]; ax.plot(n, sin_zmienny); ax.set_title("Sygnal o zmiennej czestotliwosci"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Amplituda")
ax = axs[2,1]; ax.plot(n, sin_zmienny_power); ax.set_title("Sygnal o zmiennej czestotliwosci - Obwiednia mocy, alpha=0.001"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Moc")
ax = axs[3,0]; ax.plot(n, samples); ax.set_title("Sygnal mowy"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Amplituda")
ax = axs[3,1]; ax.plot(n, samples_power); ax.set_title("Sygnal mowy - Obwiednia mocy, alpha=0.001"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Moc")
fig.set_tight_layout(tight=True)
plt.savefig("Zadanie1_3.png")
=======



# w_f, w_pxx = periodogram(w, fs, scaling='density')
# s_f, s_pxx = periodogram(s, fs, scaling='density')
# y_f, y_pxx = periodogram(y, fs, scaling='density')
#
#
#
# fig, axs = plt.subplots(3, 2)
# fig.set_size_inches(18, 16)
# ax = axs[0,0]; ax.plot(N*w_f/np.pi, 10*np.log10(w_pxx)); ax.set_ylim(-70, 0)
# ax = axs[1,0]; ax.plot(N*s_f/np.pi, 10*np.log10(s_pxx)); ax.set_ylim(-90, 0)
# ax = axs[2,0]; ax.plot(N*y_f/np.pi, 10*np.log10(y_pxx)); ax.set_ylim(-100, 0)
#
# w_f, w_pxx = periodogram(w, fs, scaling='density', window='hann')
# s_f, s_pxx = periodogram(s, fs, scaling='density')
# y_f, y_pxx = periodogram(y, fs, scaling='density')
#
# ax = axs[0,1]; ax.plot(N*w_f/np.pi, 10*np.log10(w_pxx)); ax.set_ylim(-70, 0)
# ax = axs[1,1]; ax.plot(N*s_f/np.pi, 10*np.log10(s_pxx)); ax.set_ylim(-90, 0)
# ax = axs[2,1]; ax.plot(N*y_f/np.pi, 10*np.log10(y_pxx)); ax.set_ylim(-100, 0)
# fig.set_tight_layout(tight=True)
# plt.savefig("Zadanie2_1.png")
>>>>>>> 8e861ea3f420eff0a26226297d4aefe631f0b052
