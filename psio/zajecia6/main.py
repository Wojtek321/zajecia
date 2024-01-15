import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter, freqz, tf2zpk, periodogram, spectrogram, firwin, iirfilter, group_delay, filtfilt, iirdesign, cheby1
from scipy.fft import fft
from scipy.io.wavfile import read
import sounddevice as sd


# a = [1, 0.9, 0.1]
# b = [0.1, 0.2, 0.3]
#
# def filtr(x):
#     y = np.empty(len(x))
#
#     y[0] = b[0]*x[0]
#     y[1] = b[0]*x[1] + b[1]*x[0] - a[1]*y[0]
#
#     for i in range(2, len(x)):
#         y[i] = b[0]*x[i] + b[1]*x[i-1] + b[2]*x[i-2] - a[1]*y[i-1] - a[2]*y[i-2]
#
#     return y
#
#
# N = 16
# x = np.zeros(16)
# x[0] = 1
#
# fig, axs = plt.subplots(1, 2)
# fig.set_size_inches(14, 6)
# ax = axs[0]; ax.stem(x); ax.set_title("Impuls jednostkowy"); ax.set_xlabel("Numer próbki"); ax.set_ylabel("Amplituda")
# ax = axs[1]; ax.stem(filtr(x)); ax.set_title("Odpowiedź filtru obliczona z równania różnicowego"); ax.set_xlabel("Numer próbki"); ax.set_ylabel("Amplituda")
# fig.set_tight_layout(tight=True)
# plt.savefig("Zadanie1_a.png")
#
#
# fig, axs = plt.subplots(1, 2)
# fig.set_size_inches(14, 6)
# ax = axs[0]; ax.stem(filtr(x)); ax.set_title("Odpowiedź filtru obliczona z równania różnicowego"); ax.set_xlabel("Numer próbki"); ax.set_ylabel("Amplituda")
# ax = axs[1]; ax.stem(lfilter(b, a, x)); ax.set_title("Odpowiedź filtru obliczona funkcją lfilter"); ax.set_xlabel("Numer próbki"); ax.set_ylabel("Amplituda")
# fig.set_tight_layout(tight=True)
# plt.savefig("Zadanie1_b.png")
#
#
# w, h = freqz(b, a)
# w = w / np.pi
# h_modul = np.abs(h)
# fig, axs = plt.subplots(1, 2)
# fig.set_size_inches(14, 6)
# ax = axs[0]; ax.plot(w, 20*np.log10(h_modul)); ax.set_title("Charakterystyka amplituda filtru"); ax.set_xlabel("Czestotliwosc znormalizowana [π*rad/próbka]"); ax.set_ylabel("Magnituda [dB]")
# ax = axs[1]; ax.plot(w, np.unwrap(np.angle(h))/np.pi); ax.set_title("Charakterystyka fazowa filtru"); ax.set_xlabel("Czestotliwosc znormalizowana [π*rad/próbka]"); ax.set_ylabel("Faza [π*radian]")
# fig.set_tight_layout(tight=True)
# plt.savefig("Zadanie1_c.png")
#
#
# z, p, k = tf2zpk(b, a)
# fig, ax = plt.subplots(1)
# fig.set_size_inches(6, 6)
# ax.scatter(np.real(z), np.imag(z), color="blue")
# ax.scatter(np.real(p), np.imag(p), color="red")
# ax.set_title("Położenie zer (niebieskie) oraz biegunów (czerwone) filtru")
# ax.set_xlabel("Część rzeczywista")
# ax.set_ylabel("Część urojona")
# ax.add_artist(plt.Circle((0, 0), 1, fill=False, color="black"))
# ax.set_xlim(-1.5, 1.5)
# ax.set_ylim(-1.5, 1.5)
# ax.grid(True)
# fig.set_tight_layout(tight=True)
# plt.savefig("Zadanie1_d.png")
#
#
# N = 2048
# x = np.random.normal(0, 1, N)
# y = filtr(x)
# X = fft(x)
# Y = fft(y)
#
# fig, axs = plt.subplots(1, 2)
# fig.set_size_inches(14, 6)
# ax = axs[0]; ax.plot(np.array(2*np.abs(X)/N)[:N//2]); ax.set_title("Widmo amplitudowe sygnału szumu x"); ax.set_xlabel("Numer pasma częstotliwościowego"); ax.set_ylabel("Magnituda")
# ax = axs[1]; ax.plot(np.array(2*np.abs(Y)/N)[:N//2]); ax.set_title("Widmo amplitudowe przefiltrowanego sygnału szumu x"); ax.set_xlabel("Numer pasma częstotliwościowego"); ax.set_ylabel("Magnituda")
# fig.set_tight_layout(tight=True)
# plt.savefig("Zadanie1_e1.png")
#
#
# fig, axs = plt.subplots(1, 2)
# fig.set_size_inches(14, 6)
# ax = axs[0]; ax.plot(w, 20*np.log10(h_modul)); ax.set_title("Charakterystyka amplituda filtru"); ax.set_xlabel("Czestotliwosc znormalizowana [n*radian/próbka]"); ax.set_ylabel("Magnituda [dB]")
# ax = axs[1]; ax.plot(np.array(2*np.abs(Y)/N)[:N//2]); ax.set_title("Widmo amplitudowe przefiltrowanego sygnału szumu x"); ax.set_xlabel("Numer pasma częstotliwościowego"); ax.set_ylabel("Magnituda")
# fig.set_tight_layout(tight=True)
# plt.savefig("Zadanie1_e2.png")
















# cutoff_freq = 3000
# order = 10
# nyquist_rate = 2 * cutoff_freq
# norm = cutoff_freq / nyquist_rate
#
#
# taps = firwin(order, norm)
# w_fir, h_fir = freqz(taps)
# plt.plot(0.5 * nyquist_rate * w_fir / np.pi, 20*np.log10(np.abs(h_fir)), label=f'FIR Rząd {order}')
#
# coefficients = iirfilter(order, norm, btype='lowpass')
# b = coefficients[0]
# a = coefficients[1]
# w_iir, h_iir = freqz(b, a)
# plt.plot(0.5 * nyquist_rate * w_iir / np.pi, 20*np.log10(np.abs(h_iir)), label=f'IIR Rząd {order}')
# plt.title("Amplitudowa odpowiedź częstotliwościowa filtrów FIR oraz IIR")
# plt.xlabel("Częstotliwość [Hz]")
# plt.ylabel("Amplituda")
# plt.legend()
# plt.tight_layout()
# plt.savefig("Zadanie2_a")
# plt.clf()
#
#
#
#
# phase_response_fir = np.unwrap(np.angle(h_fir))
# phase_response_iir = np.unwrap(np.angle(h_iir))
#
# plt.plot(0.5 * nyquist_rate * w_fir / np.pi, phase_response_fir, label=f'FIR - Rząd {order}')
# plt.plot(0.5 * nyquist_rate * w_iir / np.pi, phase_response_iir, label=f'IIR - Rząd {order}')
# plt.title("Porównanie fazowych odpowiedzi częstotliwościowych filtrów FIR i IIR")
# plt.xlabel("Częstotliwość [Hz]")
# plt.ylabel("Faza [rad]")
# plt.legend()
# plt.grid()
# plt.tight_layout()
# plt.savefig("Zadanie2_b")
# plt.clf()
#
#
#
#
#
# w_fir, gd_fir = group_delay((taps, np.zeros(len(taps))))
# w_iir, gd_iir = group_delay((b, a))
# plt.title("porównanie opóźnień grupowych filtrów FIR oraz IIR")
# plt.ylabel("Opóźnienie grupowe")
# plt.xlabel("Częstotliwość")
# plt.plot(w_fir, gd_fir, label=f'FIR - Rząd {order}')
# plt.plot(w_iir, gd_iir, label=f'IIR - Rząd {order}')
# plt.xlim((0,3))
# plt.legend()
# plt.tight_layout()
# plt.savefig("Zadanie2_c")


















FS, signal = read("voice.wav")
signal = signal/np.max(np.abs(signal))
t = 3
n = np.arange(0, t, 1/FS)
N = 3
rp = 1
cutoff_freq = 2000
Wn = cutoff_freq/(FS/2)


coefficients = cheby1(N=N, rp=rp, Wn=Wn, btype='lowpass', analog=False)
b = coefficients[0]
a = coefficients[1]
w, h = freqz(b, a)

fig, axs = plt.subplots(1, 2)
fig.set_size_inches(14, 6)
ax = axs[0]; ax.plot((w*FS) / (2*np.pi), 20*np.log10(np.abs(h))); ax.set_title("Charakterystyka amplitudowa filtru"); ax.set_ylabel("Magnituda [dB]"); ax.set_xlabel("Czestotliwość [Hz]")
ax = axs[1]; ax.plot((w*FS) / (2*np.pi), np.angle(h)); ax.set_title("Charakterystyka fazowa filtru"); ax.set_ylabel("Faza [rad]"); ax.set_xlabel("Czestotliwość [Hz]")
fig.set_tight_layout(tight=True)
plt.savefig("Zadanie3_a.png")


fig, axs = plt.subplots(2, 1)
fig.set_size_inches(14, 10)
ax = axs[0]; ax.plot(n, signal[:t*FS]); ax.set_title("Sygnał wejściowy"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Czas [s]")
ax = axs[1]; ax.plot(n, lfilter(b, a, signal)[:t*FS]); ax.set_title("Sygnał przefiltrowany"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Czas [s]")
fig.set_tight_layout(tight=True)
plt.savefig("Zadanie3_b.png")

sd.play(signal, FS)
sd.wait()
sd.play(lfilter(b, a, signal), FS)
sd.wait()


# fs, y = periodogram(signal, FS, scaling='spectrum')
# fs, y_filtered = periodogram(lfilter(b, a, signal), FS, scaling='spectrum')
#
# fig, axs = plt.subplots(1, 2)
# fig.set_size_inches(14, 6)
# ax = axs[0]; ax.plot(fs, 20*np.log10(np.abs(y))); ax.set_title("Sygnał wejściowy - periodogram"); ax.set_ylabel("Moc [dB]"); ax.set_xlabel("Czestotliwość [Hz]")
# ax = axs[1]; ax.plot(fs, 20*np.log10(np.abs(y_filtered))); ax.set_title("Sygnał przefiltrowany - periodogram"); ax.set_ylabel("Moc [dB]"); ax.set_xlabel("Czestotliwość [Hz]")
# fig.set_tight_layout(tight=True)
# plt.savefig("Zadanie3_c.png")
#
#
# fs, t, sxx = spectrogram(signal, FS, mode='magnitude')
# fs_filtered, t_filtered, sxx_filtered = spectrogram(lfilter(b, a, signal), FS, mode='magnitude')
#
# fig, axs = plt.subplots(1, 2)
# fig.set_size_inches(14, 6)
# ax = axs[0]; mesh = ax.pcolormesh(t, fs, sxx); cb = fig.colorbar(mesh, ax=ax); cb.set_label("Moc [dB]"); ax.set_title("Sygnał wejściowy - spektogram"); ax.set_ylabel("Czestotliwość [Hz]"); ax.set_xlabel("Czas [s]")
# ax = axs[1]; mesh = ax.pcolormesh(t_filtered, fs_filtered, sxx_filtered); cb = fig.colorbar(mesh, ax=ax); cb.set_label("Moc [dB]"); ax.set_title("Sygnał przefiltrowany - spektogram"); ax.set_ylabel("Czestotliwość [Hz]"); ax.set_xlabel("Czas [s]")
# fig.set_tight_layout(tight=True)
# plt.savefig("Zadanie3_d.png")
