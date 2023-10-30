import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square, sawtooth
from time import sleep
import sounddevice as sd
import wave
import struct


# # Zadanie 1
# # a)
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
# Y = [np.sin(x), sawtooth(x), square(x)]
#
# for i in range(0, 3):
#     plt.subplot(3, 1, i+1)
#     plt.plot(x, Y[i])
#     plt.xlabel('Kat [rad]')
#     plt.ylabel('Amplituda')
# plt.tight_layout()
# plt.show()
#
#
# #c)
# n = 200
# y = np.random.normal(loc=0, scale=0.5, size=n)
# plt.plot(y)
# plt.xlabel("Numer probki")
# plt.ylabel('Wartosc chwilowa')
# plt.title(f'Szum Gaussowski, μ={round(np.mean(y), 4)}, σ^2={round(np.std(y), 4)}')
# plt.show()


# # Zadanie 2
# A = [1, 2, 5]
# F = [1000, 2000, 5000]
# phi = [0, -np.pi/2, np.pi/2]
# fs = 44100
# dur = 2
# t = np.arange(start=0, stop=dur, step=1/fs)
# n = np.arange(0, len(t))
# #
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
#     # sd.play(y, fs)
#     # sd.wait()
# plt.tight_layout()
# plt.show()
# #
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
#     # sd.play(y, fs)
#     # sd.wait()
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
#     # sd.play(y, fs)
#     # sd.wait()
# plt.tight_layout()
# plt.show()


# # Zadanie 3
# f = 1000
# FS = [8000, 2000, 1100]
# dur = 0.2
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
#     sd.play(y, fs)
#     sd.wait()
# plt.tight_layout()
# plt.show()


# # Zadanie 4
# # a)
# with wave.open("odliczanie.wav", 'r') as file:
#     fs = file.getframerate()
#     n_frames = file.getnframes()
#     data = file.readframes(n_frames)
#     sample_width = file.getsampwidth()
#     samples = struct.unpack(f"{n_frames}h", data)
#
# max_amplitude = np.max(np.abs(samples))
# samples = samples / max_amplitude
# reversed_samples = samples[::-1]
#
# #
# time = np.arange(0, n_frames)/fs
# plt.figure(figsize=(6, 8))
# plt.subplot(4, 1, 1)
# plt.plot(time, samples)
# plt.title("Mowa")
# plt.xlabel("Czas [s]")
# plt.ylabel("Amplituda")
#
# plt.subplot(4, 1, 2)
# plt.plot(time, reversed_samples)
# plt.title("Mowa odwrocona w czasie")
# plt.xlabel("Czas [s]")
# plt.ylabel("Amplituda")
#
# # sd.play(reversed_samples, fs)
# # sd.wait()
#
#
# #b)
# y = np.random.normal(loc=0, scale=1, size=n_frames)
# plt.subplot(4, 1, 3)
# plt.plot(time, y)
# plt.title(f'Szum Gaussowski, μ={round(np.mean(y), 4)}, σ^2={round(np.std(y), 4)}')
# plt.ylabel("Amplituda")
# plt.xlabel("Czas [s]")
#
#
# moc_sygnalu = np.sum(np.power(samples, 2))
# moc_szumu = np.sum(np.power(y, 2))
#
#
# x=moc_sygnalu/np.power(10, 3/10)
# z = x/moc_szumu
# z = np.sqrt(z)
# y = y*z
# moc_szumu = np.sum(np.power(y, 2))
# SNR = 10 * np.log10(moc_sygnalu / moc_szumu)
# print(SNR)
#
#
# superpozycja = samples + y
# plt.subplot(4, 1, 4)
# plt.plot(time, superpozycja)
# plt.title(f"Mowa i Szum, SNR={round(SNR, 3)}")
# plt.ylabel("Amplituda")
# plt.xlabel("Czas [s]")
# # sd.play(superpozycja, fs)
# # sd.wait()
#
# plt.tight_layout()
# plt.show()


# # Zadanie 5