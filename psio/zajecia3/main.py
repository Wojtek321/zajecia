import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import dft


# N = 32
# f = 1
# n = np.arange(start=0, stop=N)
# y = np.sin(2*np.pi*f*n/N)
# y_im = np.imag(y)
# fft = 2*np.fft.fft(y)/N
# fft_im = np.imag(fft)
# fft_abs = np.abs(fft)
# fft_ang = np.angle(fft)/np.pi
#
# plt.figure(figsize=(12, 14))
# plt.subplot(3, 2, 1)
# plt.stem(y)
# plt.title("Re(y)")
# plt.xlabel("Numer probki")
# plt.ylabel("Amplituda")
#
# plt.subplot(3, 2, 2)
# plt.stem(y_im)
# plt.title("Im(y)")
# plt.xlabel("Numer probki")
# plt.ylabel("Amplituda")
#
# plt.subplot(3, 2, 3)
# plt.stem(fft)
# plt.title("Re(fft(y))")
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Amplituda")
# plt.axis((0, 31, -1, 1))
#
# plt.subplot(3, 2, 4)
# plt.stem(fft_im)
# plt.title("Im(fft(y))")
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Amplituda")
#
# plt.subplot(3, 2, 5)
# plt.stem(fft_abs)
# plt.title("Modul(fft(y))")
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Magnituda")
#
# plt.subplot(3, 2, 6)
# plt.stem(fft_ang)
# plt.title("Phase(fft(y))")
# plt.ylabel("Faza [pi x rad]")
# plt.xlabel("Numer pasma czestotliwosciowego")
#
# plt.tight_layout()
# plt.savefig("Zadanie1.png")







# N = 16
# n = np.arange(start=0, stop=N)
# y1 = np.cos(2*np.pi*n/N + np.pi/4)
# y2 = 0.5*np.cos(4*np.pi*n/N)
# y3 = 0.25*np.cos(8*np.pi*n/N + np.pi/2)
# y4 = y1 + y2 + y3
#
# plt.plot(y1, label='y1[n] = cos(2πn/N+π/4)')
# plt.plot(y2, label='y2[n] = 0.5cos(4πn/N)')
# plt.plot(y3, label='y3[n] = 0.25cos(8πn/N+π/2)')
# plt.legend(loc='upper right')
# plt.xlabel("Numer probki")
# plt.ylabel("Amplituda")
# plt.grid(True)
# plt.savefig("Zadanie2_1")
#
# y1_fft = 2*np.fft.fft(y1)/N
# y2_fft = 2*np.fft.fft(y2)/N
# y3_fft = 2*np.fft.fft(y3)/N
# y4_fft = 2*np.fft.fft(y4)/N
#
# y1_fft_abs = np.abs(y1_fft)
# y2_fft_abs = np.abs(y2_fft)
# y3_fft_abs = np.abs(y3_fft)
# y4_fft_abs = np.abs(y4_fft)
#
# y1_fft_ang = np.angle(y1_fft)/np.pi
# y2_fft_ang = np.angle(y2_fft)/np.pi
# y3_fft_ang = np.angle(y3_fft)/np.pi
# y4_fft_ang = np.angle(y4_fft)/np.pi
#
# plt.figure(figsize=(8,7))
# plt.subplot(2, 2, 1)
# plt.stem(y1_fft_abs)
# plt.title('y1[n] = cos(2πn/N+π/4)')
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Magnituda")
# plt.axis((-0.2, 15.2, -1.1, 1.1))
#
# plt.subplot(2, 2, 2)
# plt.stem(y2_fft_abs)
# plt.title('y2[n] = 0.5cos(4πn/N)')
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Magnituda")
# plt.axis((-0.2, 15.2, -1.1, 1.1))
#
# plt.subplot(2, 2, 3)
# plt.stem(y3_fft_abs)
# plt.title('y3[n] = 0.25cos(8πn/N+π/2)')
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Magnituda")
# plt.axis((-0.2, 15.2, -1.1, 1.1))
#
# plt.subplot(2, 2, 4)
# plt.stem(y4_fft_abs)
# plt.title("y1+y2+y3")
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Magnituda")
# plt.axis((-0.2, 15.2, -1.1, 1.1))
# plt.tight_layout()
# plt.savefig("Zadanie2_2")
#
#
#
#
# plt.subplot(2, 2, 1)
# plt.stem(y1_fft_ang)
# plt.title('y1[n] = cos(2πn/N+π/4)')
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Faza [pi x rad]")
#
# plt.subplot(2, 2, 2)
# plt.stem(y2_fft_ang)
# plt.title('y2[n] = 0.5cos(4πn/N)')
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Faza [pi x rad]")
#
# plt.subplot(2, 2, 3)
# plt.stem(y3_fft_ang)
# plt.title('y3[n] = 0.25cos(8πn/N+π/2)')
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Faza [pi x rad]")
#
# plt.subplot(2, 2, 4)
# plt.stem(y4_fft_ang)
# plt.title("y1+y2+y3")
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Faza [pi x rad]")
#
# plt.tight_layout()
# plt.savefig("Zadanie2_3.png")









# N = 32
# n = np.arange(start=0, stop=N)
# y = np.sin(2*np.pi*n/N)
# fft = 2*np.fft.fft(y)/N
# y_im = np.imag(y)
# fft_abs = np.abs(fft)
# fft_ang = np.angle(fft)/np.pi
# ifft = N*np.fft.ifft(fft)/2
# ifft_img = np.imag(ifft)
#
#
# plt.figure(figsize=(12, 14))
# plt.subplot(3, 2, 1)
# plt.stem(y)
# plt.title("Re(y)")
# plt.xlabel("Numer probki")
# plt.ylabel("Amplituda")
#
# plt.subplot(3, 2, 2)
# plt.stem(y_im)
# plt.title("Im(y)")
# plt.xlabel("Numer probki")
# plt.ylabel("Amplituda")
#
# plt.subplot(3, 2, 3)
# plt.stem(fft_abs)
# plt.title("Modul(fft(y))")
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Magnituda")
#
# plt.subplot(3, 2, 4)
# plt.stem(fft_ang)
# plt.title("Phase(fft(y))")
# plt.ylabel("Faza [pi x rad]")
# plt.xlabel("Numer pasma czestotliwosciowego")
#
# plt.subplot(3, 2, 5)
# plt.stem(ifft)
# plt.title("Re(ifft(y))")
# plt.ylabel("Amplituda")
# plt.xlabel("Numer probki")
#
# plt.subplot(3, 2, 6)
# plt.stem(ifft_img)
# plt.title("Im(ifft(y))")
# plt.ylabel("Amplituda")
# plt.xlabel("Numer probki")
# plt.axis((-0.2, 15.2, -1.1, 1.1))
#
# plt.tight_layout()
# plt.savefig("Zadanie3a.png")




# N = 32
# n = np.arange(start=0, stop=N)
# y1 = np.cos(2*np.pi*n/N + np.pi/4)
# y2 = 0.5*np.cos(4*np.pi*n/N)
# y3 = 0.25*np.cos(8*np.pi*n/N + np.pi/2)
#
# y4 = y1 + y2 + y3
# fft = 2*np.fft.fft(y4)/N
# fft_abs = np.abs(fft)
# fft_ang = np.angle(fft)/np.pi
# ifft = N*np.fft.ifft(fft)/2
#
# plt.figure(figsize=(12, 10))
# plt.subplot(2, 2, 1)
# plt.stem(y4)
# plt.title("y1+y2+y3")
# plt.xlabel("Numer Probki")
# plt.ylabel("Amplituda")
#
# plt.subplot(2, 2, 2)
# plt.stem(fft_abs)
# plt.title("Modul Widma")
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Magnituda")
#
# plt.subplot(2, 2, 3)
# plt.stem(fft_ang)
# plt.title("Faza Widma")
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Faza [pi x rad]")
#
# plt.subplot(2, 2, 4)
# plt.stem(ifft)
# plt.title("ifft(Y)")
# plt.xlabel("Numer Probki")
# plt.ylabel("Amplituda")

# plt.tight_layout()
# plt.savefig("Zadanie3b.png")







# N = 32
# k=1
# phi = np.pi/2
# n = np.arange(start=0, stop=N)
# y = np.exp(1j*((2*np.pi * k/N * n) + phi))
# y_re = np.real(y)
# y_im = np.imag(y)
# fft = 2*np.fft.fft(y)/N
# ftt_re = np.real(fft)
# fft_im = np.imag(fft)
# fft_abs = np.abs(fft)
# fft_ang = np.angle(fft)/np.pi
#
# plt.figure(figsize=(12, 14))
# plt.subplot(3, 2, 1)
# plt.stem(y_re)
# plt.title("Re(y)")
# plt.xlabel("Numer probki")
# plt.ylabel("Amplituda")
#
# plt.subplot(3, 2, 2)
# plt.stem(y_im)
# plt.title("Im(y)")
# plt.xlabel("Numer probki")
# plt.ylabel("Amplituda")
#
# plt.subplot(3, 2, 3)
# plt.stem(ftt_re)
# plt.title("Re(fft(y))")
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Amplituda")
# plt.axis((0, 31, -1, 1))
#
# plt.subplot(3, 2, 4)
# plt.stem(fft_im)
# plt.title("Im(fft(y))")
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Amplituda")
#
# plt.subplot(3, 2, 5)
# plt.stem(fft_abs)
# plt.title("Modul(fft(y))")
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Magnituda")
#
# plt.subplot(3, 2, 6)
# plt.stem(fft_ang)
# plt.title("Phase(fft(y))")
# plt.ylabel("Faza [pi x rad]")
# plt.xlabel("Numer pasma czestotliwosciowego")
#
# plt.tight_layout()
# plt.savefig("Zadanie4.png")






# def DFT(y):
#     n = len(y)
#     dft_matrix = dft(n=n)
#     return np.dot(dft_matrix, y)
#
# def IDFT(y):
#     n = len(y)
#     dft_matrix = dft(n=n)
#     return np.dot(np.linalg.inv(dft_matrix), y)
#
#
#
# N = 32
# f = 1
# n = np.arange(start=0, stop=N)
# y = np.sin(2*np.pi*f*n/N)
# fft = 2*np.fft.fft(y)/N
# fft_abs = np.abs(fft)
# fft_ang = np.angle(fft)/np.pi
# fft_moje = 2*DFT(y)/N
# fft_moje_abs = np.abs(fft_moje)
# fft_moje_ang = np.angle(fft_moje)/np.pi
# ifft_moje = N*IDFT(fft_moje)/2
#
# plt.figure(figsize=(12, 14))
# plt.subplot(3, 2, 1)
# plt.stem(y)
# plt.title("y")
# plt.xlabel("Numer probki")
# plt.ylabel("Amplituda")
#
# plt.subplot(3, 2, 2)
# plt.stem(ifft_moje)
# plt.title("y - Funkcja Wlasna IDFT")
# plt.xlabel("Numer probki")
# plt.ylabel("Amplituda")
#
# plt.subplot(3, 2, 3)
# plt.stem(fft_abs)
# plt.title("Modul Widma FFT")
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Magnituda")
#
# plt.subplot(3, 2, 4)
# plt.stem(fft_moje_abs)
# plt.title("Modul Widma - Funkcja Wlasna")
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Magnituda")
#
# plt.subplot(3, 2, 5)
# plt.stem(fft_ang)
# plt.title("Faza Widma FFT")
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Faza [pi x rad]")
#
# plt.subplot(3, 2, 6)
# plt.stem(fft_moje_ang)
# plt.title("Faza Widma - Funkcja Wlasna")
# plt.ylabel("Faza [pi x rad]")
# plt.xlabel("Numer pasma czestotliwosciowego")
#
# plt.tight_layout()
# plt.savefig("wykres5a.png")
#
#
#
#
#
# N = 32
# n = np.arange(start=0, stop=N)
# y1 = np.cos(2*np.pi*n/N + np.pi/4)
# y1_fft = 2*np.fft.fft(y1)/N
# y1_fft_abs = np.abs(y1_fft)
# y1_fft_ang = np.angle(y1_fft)/np.pi
# y1_fft_moje = 2*DFT(y1)/N
# y1_fft_abs_moje = np.abs(y1_fft_moje)
# y1_fft_ang_moje = np.angle(y1_fft_moje)/np.pi
# y1_ifft_moje = N*IDFT(y1_fft_moje)/2
#
# plt.figure(figsize=(12, 14))
# plt.subplot(3, 2, 1)
# plt.stem(y1)
# plt.title("y1")
# plt.xlabel("Numer probki")
# plt.ylabel("Amplituda")
#
# plt.subplot(3, 2, 2)
# plt.stem(y1_ifft_moje)
# plt.title("y1 - własna funkcja IDFT")
# plt.xlabel("Numer probki")
# plt.ylabel("Amplituda")
#
# plt.subplot(3, 2, 3)
# plt.stem(y1_fft_abs)
# plt.title("Modul Widma FFT")
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Magnituda")
#
# plt.subplot(3, 2, 4)
# plt.stem(y1_fft_abs_moje)
# plt.title("Modul Widma - Funkcja Wlasna")
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Magnituda")
#
# plt.subplot(3, 2, 5)
# plt.stem(y1_fft_ang)
# plt.title("Faza Widma FFT")
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Faza [pi x rad]")
#
# plt.subplot(3, 2, 6)
# plt.stem(y1_fft_ang_moje)
# plt.title("Faza Widma - Funkcja Wlasna")
# plt.ylabel("Faza [pi x rad]")
# plt.xlabel("Numer pasma czestotliwosciowego")
#
# plt.tight_layout()
# plt.savefig("wykres5b_y1.png")
#
#
#
# y2 = 0.5*np.cos(4*np.pi*n/N)
# y2_fft = 2*np.fft.fft(y2)/N
# y2_fft_abs = np.abs(y2_fft)
# y2_fft_ang = np.angle(y2_fft)/np.pi
# y2_fft_moje = 2*DFT(y2)/N
# y2_fft_abs_moje = np.abs(y2_fft_moje)
# y2_fft_ang_moje = np.angle(y2_fft_moje)/np.pi
# y2_ifft_moje = N*IDFT(y2_fft_moje)/2
#
# plt.figure(figsize=(12, 14))
# plt.subplot(3, 2, 1)
# plt.stem(y2)
# plt.title("y2")
# plt.xlabel("Numer probki")
# plt.ylabel("Amplituda")
#
# plt.subplot(3, 2, 2)
# plt.stem(y2_ifft_moje)
# plt.title("y2 - własna funkcja IDFT")
# plt.xlabel("Numer probki")
# plt.ylabel("Amplituda")
#
# plt.subplot(3, 2, 3)
# plt.stem(y2_fft_abs)
# plt.title("Modul Widma FFT")
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Magnituda")
#
# plt.subplot(3, 2, 4)
# plt.stem(y2_fft_abs_moje)
# plt.title("Modul Widma - Funkcja Wlasna")
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Magnituda")
#
# plt.subplot(3, 2, 5)
# plt.stem(y2_fft_ang)
# plt.title("Faza Widma FFT")
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Faza [pi x rad]")
#
# plt.subplot(3, 2, 6)
# plt.stem(y2_fft_ang_moje)
# plt.title("Faza Widma - Funkcja Wlasna")
# plt.ylabel("Faza [pi x rad]")
# plt.xlabel("Numer pasma czestotliwosciowego")
#
# plt.tight_layout()
# plt.savefig("wykres5b_y2.png")
#
#
#
# y3 = 0.25*np.cos(8*np.pi*n/N + np.pi/2)
# y3_fft = 2*np.fft.fft(y3)/N
# y3_fft_abs = np.abs(y3_fft)
# y3_fft_ang = np.angle(y3_fft)/np.pi
# y3_fft_moje = 2*DFT(y3)/N
# y3_fft_abs_moje = np.abs(y3_fft_moje)
# y3_fft_ang_moje = np.angle(y3_fft_moje)/np.pi
# y3_ifft_moje = N*IDFT(y3_fft_moje)/2
#
# plt.figure(figsize=(12, 14))
# plt.subplot(3, 2, 1)
# plt.stem(y3)
# plt.title("y3")
# plt.xlabel("Numer probki")
# plt.ylabel("Amplituda")
#
# plt.subplot(3, 2, 2)
# plt.stem(y3_ifft_moje)
# plt.title("y3 - własna funkcja IDFT")
# plt.xlabel("Numer probki")
# plt.ylabel("Amplituda")
#
# plt.subplot(3, 2, 3)
# plt.stem(y3_fft_abs)
# plt.title("Modul Widma FFT")
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Magnituda")
#
# plt.subplot(3, 2, 4)
# plt.stem(y3_fft_abs_moje)
# plt.title("Modul Widma - Funkcja Wlasna")
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Magnituda")
#
# plt.subplot(3, 2, 5)
# plt.stem(y3_fft_ang)
# plt.title("Faza Widma FFT")
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Faza [pi x rad]")
#
# plt.subplot(3, 2, 6)
# plt.stem(y3_fft_ang_moje)
# plt.title("Faza Widma - Funkcja Wlasna")
# plt.ylabel("Faza [pi x rad]")
# plt.xlabel("Numer pasma czestotliwosciowego")
#
# plt.tight_layout()
# plt.savefig("wykres5b_y3.png")
#
#
#
# y4 = y1 + y2 + y3
# y4_fft = 2*np.fft.fft(y4)/N
# y4_fft_abs = np.abs(y4_fft)
# y4_fft_ang = np.angle(y4_fft)/np.pi
# y4_fft_moje = 2*DFT(y4)/N
# y4_fft_abs_moje = np.abs(y4_fft_moje)
# y4_fft_ang_moje = np.angle(y4_fft_moje)/np.pi
# y4_ifft_moje = N*IDFT(y4_fft_moje)/2
#
# plt.figure(figsize=(12, 14))
# plt.subplot(3, 2, 1)
# plt.stem(y4)
# plt.title("y4")
# plt.xlabel("Numer probki")
# plt.ylabel("Amplituda")
#
# plt.subplot(3, 2, 2)
# plt.stem(y4_ifft_moje)
# plt.title("y4 - własna funkcja IDFT")
# plt.xlabel("Numer probki")
# plt.ylabel("Amplituda")
#
# plt.subplot(3, 2, 3)
# plt.stem(y4_fft_abs)
# plt.title("Modul Widma FFT")
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Magnituda")
#
# plt.subplot(3, 2, 4)
# plt.stem(y4_fft_abs_moje)
# plt.title("Modul Widma - Funkcja Wlasna")
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Magnituda")
#
# plt.subplot(3, 2, 5)
# plt.stem(y4_fft_ang)
# plt.title("Faza Widma FFT")
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Faza [pi x rad]")
#
# plt.subplot(3, 2, 6)
# plt.stem(y4_fft_ang_moje)
# plt.title("Faza Widma - Funkcja Wlasna")
# plt.ylabel("Faza [pi x rad]")
# plt.xlabel("Numer pasma czestotliwosciowego")
#
# plt.tight_layout()
# plt.savefig("wykres5b_y4.png")










N = 32
n = np.arange(0, N)
y = np.sin(2*np.pi * 2.5 * n/N)

bartlett = np.bartlett(N)
hamming = np.hamming(N)
hann = np.hanning(N)
kaiser = np.kaiser(N, 2)
prostokatne = np.ones(N)

fft_abs = np.abs(2*np.fft.fft(y)/N)
fft_bartlett = np.abs(2*np.fft.fft(y * bartlett)/N)
fft_hamming = np.abs(2*np.fft.fft(y * hamming)/N)
fft_hann = np.abs(2*np.fft.fft(y * hann)/N)
fft_kaiser = np.abs(2*np.fft.fft(y * kaiser)/N)
fft_prostokatne = np.abs(2*np.fft.fft(y * prostokatne)/N)

fig, axs = plt.subplots(3, 3)
fig.set_size_inches(18, 16)
ax = axs[0,0]
ax.stem(y)
ax.set_title("y")
ax.set_xlabel("Numer Probki")
ax.set_ylabel("Amplituda")

ax = axs[0,1]
ax.set_xlabel("Numer Probki")
ax.set_ylabel("Waga")
ax.plot(n, bartlett, label='Bartlett')
ax.plot(n, hamming, label='Hamming')
ax.plot(n, hann, label='Hann')
ax.plot(n, kaiser, label='Kaiser')
ax.plot(n, prostokatne, label='Okno Prostokatne')
ax.legend()

ax = axs[1,0]
ax.stem(fft_abs)
ax.set_title("Modul FFT - Brak Okna")
ax.set_xlabel("Numer Pasma Czestotliwosciowego")
ax.set_ylabel("Magnituda")

ax = axs[1,1]
ax.stem(fft_bartlett)
ax.set_title("Modul FFT - Bartlett")
ax.set_xlabel("Numer Pasma Czestotliwosciowego")
ax.set_ylabel("Magnituda")

ax = axs[1,2]
ax.stem(fft_hamming)
ax.set_title("Modul FFT - Hamming")
ax.set_xlabel("Numer Pasma Czestotliwosciowego")
ax.set_ylabel("Magnituda")

ax = axs[2,0]
ax.stem(fft_hann)
ax.set_title("Modul FFT - Hann")
ax.set_xlabel("Numer Pasma Czestotliwosciowego")
ax.set_ylabel("Magnituda")

ax = axs[2,1]; ax.stem(fft_kaiser); ax.set_title("Modul FFT - Kaiser"); ax.set_xlabel("Numer Pasma Czestotliwosciowego"); ax.set_ylabel("Magnituda")

ax = axs[2,2]; ax.stem(fft_prostokatne); ax.set_title("Modul FFT - Okno Prostokatne"); ax.set_xlabel("Numer Pasma Czestotliwosciowego"); ax .set_ylabel("Magnituda")


fig.set_tight_layout(tight=True)
plt.savefig("Zadanie6.png")