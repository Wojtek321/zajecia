import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter, freqz, tf2zpk
from scipy.fft import fft


a = [1, 0.9, 0.1]
b = [0.1, 0.2, 0.3]

def filtr(x):
    y = np.empty(len(x))

    y[0] = b[0]*x[0]
    y[1] = b[0]*x[1] + b[1]*x[0] - a[1]*y[0]

    for i in range(2, len(x)):
        y[i] = b[0]*x[i] + b[1]*x[i-1] + b[2]*x[i-2] - a[1]*y[i-1] - a[2]*y[i-2]

    return y


N = 16
x = np.zeros(16)
x[0] = 1

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


w, h = freqz(b, a)
w = w / np.pi
h_modul = np.abs(h)
fig, axs = plt.subplots(1, 2)
fig.set_size_inches(14, 6)
ax = axs[0]; ax.plot(w, 20*np.log10(h_modul)); ax.set_title("Charakterystyka amplituda filtru"); ax.set_xlabel("Czestotliwosc znormalizowana [n*radian/próbka]"); ax.set_ylabel("Magnituda [dB]")
ax = axs[1]; ax.plot(w, np.unwrap(np.angle(h))/np.pi); ax.set_title("Charakterystyka fazowa filtru"); ax.set_xlabel("Czestotliwosc znormalizowana [n*radian/próbka]"); ax.set_ylabel("Faza [pi*radian]")
fig.set_tight_layout(tight=True)
plt.savefig("Zadanie1_c.png")


z, p, k = tf2zpk(b, a)
fig, ax = plt.subplots(1)
fig.set_size_inches(6, 6)
ax.scatter(np.real(z), np.imag(z), color="blue", label="Zero")
ax.scatter(np.real(p), np.imag(p), color="red", label="Pole")
ax.set_title("Położenie zer oraz biegunów filtru")
ax.set_xlabel("Część rzeczywista")
ax.set_ylabel("Część urojona")
ax.add_artist(plt.Circle((0, 0), 1, fill=False, color="black"))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.grid(True)
ax.legend()
fig.set_tight_layout(tight=True)
plt.savefig("Zadanie1_d.png")


N = 2048
n = np.arange(0, N//2, 1)/(N//2)
x = np.random.normal(0, 1, N)
y = filtr(x)
X = fft(x)
Y = fft(y)

fig, axs = plt.subplots(1, 2)
fig.set_size_inches(14, 6)
ax = axs[0]; ax.plot(np.array(2*np.abs(X)/N)[:N//2]); ax.set_title("Widmo amplitudowe sygnału szumu x"); ax.set_xlabel("Numer pasma częstotliwościowego"); ax.set_ylabel("Magnituda")
ax = axs[1]; ax.plot(np.array(2*np.abs(Y)/N)[:N//2]); ax.set_title("Widmo amplitudowe przefiltrowanego sygnału szumu x"); ax.set_xlabel("Numer pasma częstotliwościowego"); ax.set_ylabel("Magnituda")
fig.set_tight_layout(tight=True)
plt.savefig("Zadanie1_e1.png")


fig, axs = plt.subplots(1, 2)
fig.set_size_inches(14, 6)
ax = axs[0]; ax.plot(w, 20*np.log10(h_modul)); ax.set_title("Charakterystyka amplituda filtru"); ax.set_xlabel("Czestotliwosc znormalizowana [n*radian/próbka]"); ax.set_ylabel("Magnituda [dB]")
ax = axs[1]; ax.plot(n, np.array(20*np.log10(2*np.abs(Y)/N))[:N//2]); ax.set_title("Widmo amplitudowe przefiltrowanego sygnału szumu x"); ax.set_xlabel("Czestotliwosc znormalizowana [n*radian/próbka]"); ax.set_ylabel("Magnituda [dB]")
fig.set_tight_layout(tight=True)
plt.savefig("Zadanie1_e2.png")