import numpy as np
import matplotlib.pyplot as plt

# N = 32
# f = 2
# n = np.arange(start=0, stop=N)
#
#
# y = np.sin(2*np.pi*n/N)
# plt.figure(figsize=(12, 14))
# plt.subplot(3, 2, 1)
# plt.stem(y)
# plt.title("Re(y)")
# plt.xlabel("Numer probki")
# plt.ylabel("Amplituda")
#
#
# y_im = np.imag(y)
# plt.subplot(3, 2, 2)
# plt.stem(y_im)
# plt.title("Im(y)")
# plt.xlabel("Numer probki")
# plt.ylabel("Amplituda")
#
#
# fft = 2*np.fft.fft(y)/N
# plt.subplot(3, 2, 3)
# plt.stem(fft)
# plt.title("Re(fft(y))")
# plt.ylabel("Amplituda")
# plt.xlabel("Numer pasma czestotliwosciowego")
# plt.axis((0, 30, -1, 1))
#
#
# fft_im = np.imag(fft)
# plt.subplot(3, 2, 4)
# plt.stem(fft_im)
# plt.title("Im(fft(y))")
# plt.ylabel("Amplituda")
# plt.xlabel("Numer pasma czestotliwosciowego")
#
#
# fft_abs = np.abs(fft)
# plt.subplot(3, 2, 5)
# plt.stem(fft_abs)
# plt.title("Modul(fft(y))")
# plt.ylabel("Magnituda")
# plt.xlabel("Numer pasma czestotliwosciowego")
#
#
# fft_ang = np.angle(fft)
# plt.subplot(3, 2, 6)
# plt.stem(fft_ang)
# plt.title("Phase(fft(y))")
# plt.ylabel("Faza [pi x rad]")
# plt.xlabel("Numer pasma czestotliwosciowego")
#
#
# plt.tight_layout()
# plt.savefig("wykres.png")
# plt.show()




N = 32
n = np.arange(start=0, stop=N)
y1 = np.cos(2*np.pi*n/N + np.pi/4)
y2 = 0.5*np.cos(4*np.pi*n/N)
y3 = 0.25*np.cos(8*np.pi*n/N + np.pi/2)

plt.plot(y1, label='y1[n] = cos(2πn/N+π/4)')
plt.plot(y2, label='y2[n] = 0.5cos(4πn/N)')
plt.plot(y3, label='y3[n] = 0.25cos(8πn/N+π/2)')
plt.legend(loc='upper right')
plt.xlabel("Numer probki")
plt.ylabel("Amplituda")
plt.show()

y4 = y1 + y2 + y3