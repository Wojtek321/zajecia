import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square, sawtooth
import sounddevice as sd
import wave
import struct


# Zadanie 1
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
# # c)
# n = 200
# y = np.random.normal(loc=0, scale=0.5, size=n)
# plt.plot(y)
# plt.xlabel("Numer probki")
# plt.ylabel('Wartosc chwilowa')
# plt.title(fr'Szum Gaussowski, μ={round(float(np.mean(y)), 4)}, $σ^{2}$={round(float(np.std(y)), 4)}')
# plt.show()
#
#
# # Zadanie 2
# A = [1, 2, 5]
# F = [1000, 2000, 5000]
# phi = [0, -np.pi/2, np.pi/2]
# fs = 44100
# dur = 0.003
# t = np.arange(start=0, stop=dur, step=1/fs)
# n = np.arange(0, len(t))
#
# for i in range(0, 3):
#     y = A[i]*np.sin(2*np.pi*F[0]*n/fs + phi[0])
#     plt.subplot(3, 1, i+1)
#     plt.plot(t, y)
#     plt.xticks([0.0000, 0.0005, 0.0010, 0.0015, 0.0020, 0.0025, 0.0030],
#                ["0", "0.5", "1", "1.5", "2", "2.5", "3"])
#     plt.xlabel("Czas [s]")
#     plt.ylabel("Amplituda")
#     plt.title(f"Amplituda = {A[i]}")
#     plt.text(0.0028, -11.5, r'$x 10^{-3}$', fontsize=10)
#     plt.tight_layout()
#     plt.grid(True)
#     plt.axis((0, 0.003, -5, 5))
#     # sd.play(y, fs)
#     # sd.wait()
# plt.tight_layout()
# plt.show()
#
#
# for i in range(0, 3):
#     y = 5*np.sin(2*np.pi*F[i]*n/fs + phi[0])
#     plt.subplot(3, 1, i+1)
#     plt.plot(t, y)
#     plt.xticks([0.0000, 0.0005, 0.0010, 0.0015, 0.0020, 0.0025, 0.0030],
#                ["0", "0.5", "1", "1.5", "2", "2.5", "3"])
#     plt.xlabel("Czas [s]")
#     plt.ylabel("Amplituda")
#     plt.title(f"f = {F[i]} Hz")
#     plt.grid(True)
#     plt.axis((0, 0.003, -5, 5))
#     plt.text(0.0028, -11.5, r'$x 10^{-3}$', fontsize=10)
#     plt.tight_layout()
#     sd.play(y, fs)
#     sd.wait()
# plt.tight_layout()
# plt.show()
#
# for i in range(0, 3):
#     y = 5*np.sin(2*np.pi*F[0]*n/fs + phi[i])
#     plt.subplot(3, 1, i+1)
#     plt.plot(t, y)
#     plt.xlabel("Czas [s]")
#     plt.ylabel("Amplituda")
#     plt.xticks([0.0000, 0.0005, 0.0010, 0.0015, 0.0020, 0.0025, 0.0030],
#                ["0", "0.5", "1", "1.5", "2", "2.5", "3"])
#
#     if(i == 0):
#         plt.title("⌀ = 0 rad")
#     elif(i == 1):
#         plt.title("⌀ = -π/2 rad")
#     else:
#         plt.title("⌀ = π/2 rad")
#
#     plt.grid(True)
#     plt.axis((0, 0.003, -5, 5))
#     plt.text(0.0028, -11.5, r'$x 10^{-3}$', fontsize=10)
#     plt.tight_layout()
#     # sd.play(y, fs)
#     # sd.wait()
# plt.tight_layout()
# plt.show()
#
#
# # # # Zadanie 3
# f = 1000
# FS = [8000, 2000, 1100]
# dur = 2
#
# for i in range(0, 3):
#     t = np.arange(start=0, stop=dur + 1/FS[i], step=1/FS[i])
#     n = np.arange(start=0, stop=len(t))
#     y = 5*np.sin(2*np.pi*f*n/FS[i])
#     plt.subplot(3, 1, i+1)
#     plt.plot(t, y)
#     plt.stem(t, y)
#     plt.axis((0, 0.007, -5, 5))
#     plt.title(f"fs = {FS[i]}Hz, f = 1000Hz")
#     plt.xticks([0.000, 0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007],
#                              ["0", "1", "2", "3", "4", "5", "6", "7"])
#     plt.xlabel("Czas [s]")
#     plt.ylabel("Amplituda")
#     plt.text(0.0065, -11.5, r'$x 10^{-3}$', fontsize=10)
#     plt.grid(True)
#     plt.tight_layout()
# plt.tight_layout()
# plt.show()
#
#
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
#
# time = np.arange(0, n_frames)/fs
# plt.figure(figsize=(6, 8))
# plt.subplot(4, 1, 1)
# plt.plot(time, samples)
# plt.title("Mowa")
# plt.xlabel("Czas [s]")
# plt.ylabel("Amplituda")
# # sd.play(samples, fs)
# # sd.wait()
#
# reversed_samples = samples[::-1]
# plt.subplot(4, 1, 2)
# plt.plot(time, reversed_samples)
# plt.title("Mowa odwrocona w czasie")
# plt.xlabel("Czas [s]")
# plt.ylabel("Amplituda")
#
#
# #b)
# y = np.random.normal(loc=0, scale=1, size=n_frames)
# plt.subplot(4, 1, 3)
# plt.plot(time, y)
# plt.title(f'Szum Gaussowski, μ={round(float(np.mean(y)), 4)}, σ^2={round(float(np.std(y)), 4)}')
# plt.ylabel("Amplituda")
# plt.xlabel("Czas [s]")
#
# moc_sygnalu = np.sum(np.power(samples, 2))
# moc_szumu = np.sum(np.power(y, 2))
# x=moc_sygnalu/np.power(10, 3/10)
# z = x/moc_szumu
# z = np.sqrt(z)
# y = y*z
# moc_szumu = np.sum(np.power(y, 2))
# SNR = 10 * np.log10(moc_sygnalu / moc_szumu)
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


# Zadanie 5

CZESTOTLIWOSC = {
    'C': 261.626,
    'D': 293.665,
    'E': 329.628,
    'F': 349.228,
    'G': 391.995,
    'A': 440,
    'H': 493.883,
}

MELODIA = [
    ('G', 1), ('E', 1), ('E', 1), ('F', 1), ('D', 1), ('D', 1),
    ('C', 0.5), ('E', 0.5), ('G', 2),
    ('G', 1), ('E', 1), ('E', 1), ('F', 1), ('D', 1), ('D', 1),
    ('C', 0.5), ('E', 0.5), ('C', 2),
    ('C', 1), ('E', 1), ('E', 1), ('F', 1), ('D', 1), ('D', 1),
    ('C', 0.5), ('E', 0.5), ('G', 2),
    ('G', 1), ('E', 1), ('E', 1), ('F', 1), ('D', 1), ('D', 1),
    ('C', 0.5), ('E', 0.5), ('C', 2),
]

FS = 44100
TIME = 0.5
SOUNDS = []

def generate_sound(czestotliwosc, czas):
    t = np.arange(start=0, stop=czas, step=1 / FS)
    n = np.arange(start=0, stop=len(t))
    sound = 0.3 * np.sin(2 * np.pi * czestotliwosc * n / FS)

    fade_in = np.linspace(0, 1, int(0.05 * FS))
    fade_out = np.linspace(1, 0, int(0.05 * FS))

    sound[0:len(fade_in)] *= fade_in
    sound[-len(fade_out):] *= fade_out

    return sound


for nuta in MELODIA:
    sound = generate_sound(CZESTOTLIWOSC[nuta[0]], TIME*float(nuta[1]))
    SOUNDS.extend(sound)

sd.play(SOUNDS, FS)
sd.wait()
