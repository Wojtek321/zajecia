import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square, sawtooth
from IPython.display import Audio
from time import sleep


# # Zadanie 1
# a)
# x = np.zeros((1, 41))
# x[0][0] = 1
# x[0][40] = 1
# plt.stem(x[0])
# plt.xlabel('Numer probki')
# plt.ylabel('Wartosc probki')
# plt.title('Impuls oraz impuls przesuniety o N=40 probek')
# plt.axis((-1, 41, -0.05, 1.05))
# plt.grid(True)
# plt.show()
#
#
# # b)
# N = 200
# x = np.linspace(0, 2*5*np.pi, N)
# y1 = np.sin(x)
# y2 = sawtooth(x)
# y3 = square(x)
#
# plt.subplot(3, 1, 1)
# plt.plot(x, y1)
# plt.xlabel('Kat [rad]')
# plt.ylabel('Amplituda')
#
# plt.subplot(3, 1, 2)
# plt.plot(x, y2)
# plt.xlabel('Kat [rad]')
# plt.ylabel('Amplituda')
#
# plt.subplot(3, 1, 3)
# plt.plot(x, y3)
# plt.xlabel('Kat [rad]')
# plt.ylabel('Amplituda')
# plt.show()
#
#
# #c)
# n = 200
# y = np.random.normal(loc=0, scale=0.5, size=n)
#
# plt.plot(y)
# plt.xlabel("Numer probki")
# plt.ylabel('Wartosc chwilowa')
# plt.title(f'Szum Gaussowski, μ={round(np.mean(y), 4)}, σ^2={round(np.std(y), 4)}')
# plt.show()


# # Zadanie 2
A = [1, 2, 5]
F = [1000, 2000, 5000]
phi = [0, -np.pi/2, np.pi/2]
fs = 44100
dur = 1
t = np.arange(start=0, stop=dur, step=1/fs)
n = np.arange(0, len(t))
#
# i=1
# for a in A:
#     y = a*np.sin(2*np.pi*F[0]*n/fs + phi[0])
#     plt.subplot(3, 1, i)
#     plt.plot(t, y)
#     plt.xlabel("Czas [ms]")
#     plt.ylabel("Amplituda")
#     plt.title(f"Amplituda = {a}")
#     plt.grid(True)
#     plt.axis((0, 0.003, -5, 5))
#     i += 1
#     # Audio(y, rate=44100)
#     # sleep(2)
# plt.tight_layout()
# plt.show()
#
# i=1
# for f in F:
#     y = A[0]*np.sin(2*np.pi*f*n/fs + phi[0])
#     plt.subplot(3, 1, i)
#     plt.plot(t, y)
#     plt.xlabel("Czas [ms]")
#     plt.ylabel("Amplituda")
#     plt.title(f"f = {f}")
#     plt.grid(True)
#     plt.axis((0, 0.003, -1, 1))
#     i += 1
# plt.tight_layout()
# plt.show()
#
# i=1
# for p in phi:
#     y = A[0]*np.sin(2*np.pi*F[0]*n/fs + p)
#     plt.subplot(3, 1, i)
#     plt.plot(t, y)
#     plt.xlabel("Czas [ms]")
#     plt.ylabel("Amplituda")
#
#     if(i == 1):
#         plt.title("⌀ = 0 rad")
#     elif(i == 2):
#         plt.title("⌀ = -π/2 rad")
#     else:
#         plt.title("⌀ = π/2 rad")
#
#     plt.grid(True)
#     plt.axis((0, 0.003, -1, 1))
#     i += 1
# plt.tight_layout()
# plt.show()


# Zadanie 3
# f = 1000
# FS = [8000, 2000, 1100]
# dur = 0.007
#
# i=1
# for fs in FS:
#     t = np.arange(start=0, stop=dur + 1/fs, step=1/fs)
#     n = np.arange(start=0, stop=len(t))
#     y = np.sin(2*np.pi*f*n/fs)
#     plt.subplot(3, 1, i)
#     plt.plot(t, y)
#     plt.stem(t, y)
#     plt.axis((0, 0.007, -1, 1))
#     plt.title(f"fs = {fs}Hz, f = 1000Hz")
#     plt.xlabel("Czas [ms]")
#     plt.ylabel("Amplituda")
#     plt.grid(True)
#     i += 1
# plt.tight_layout()
# plt.show()

