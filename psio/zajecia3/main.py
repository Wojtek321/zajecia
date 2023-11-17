import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import dft


# N = 32
# f = 1
# n = np.arange(start=0, stop=N)
# y = np.sin(2*np.pi*f*n/N)
# plt.figure(figsize=(12, 14))
# plt.subplot(3, 2, 1)
# plt.stem(y)
# plt.title("Re(y)")
# plt.xlabel("Numer probki")
# plt.ylabel("Amplituda")
#
# y_im = np.imag(y)
# plt.subplot(3, 2, 2)
# plt.stem(y_im)
# plt.title("Im(y)")
# plt.xlabel("Numer probki")
# plt.ylabel("Amplituda")
#
# fft = 2*np.fft.fft(y)/N
# plt.subplot(3, 2, 3)
# plt.stem(fft)
# plt.title("Re(fft(y))")
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Amplituda")
# plt.axis((0, 31, -1, 1))
#
# fft_im = np.imag(fft)
# plt.subplot(3, 2, 4)
# plt.stem(fft_im)
# plt.title("Im(fft(y))")
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Amplituda")
#
# fft_abs = np.abs(fft)
# plt.subplot(3, 2, 5)
# plt.stem(fft_abs)
# plt.title("Modul(fft(y))")
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Magnituda")
#
# fft_ang = np.angle(fft)/np.pi
# plt.subplot(3, 2, 6)
# plt.stem(fft_ang)
# plt.title("Phase(fft(y))")
# plt.ylabel("Faza [pi x rad]")
# plt.xlabel("Numer pasma czestotliwosciowego")
#
# plt.tight_layout()
# plt.savefig("wykres2.png")







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
# plt.show()
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
# plt.figure(figsize=(8,7))
#
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
# plt.show()
#
#
#
# y1_fft_ang = np.angle(y1_fft)/np.pi
# plt.subplot(2, 2, 1)
# plt.stem(y1_fft_ang)
# plt.title('y1[n] = cos(2πn/N+π/4)')
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Faza [pi x rad]")
#
# y2_fft_ang = np.angle(y2_fft)/np.pi
# plt.subplot(2, 2, 2)
# plt.stem(y2_fft_ang)
# plt.title('y2[n] = 0.5cos(4πn/N)')
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Faza [pi x rad]")
# # plt.axis((-0.2, 15.2, -1.1, 1.1))
#
# y3_fft_ang = np.angle(y3_fft)/np.pi
# plt.subplot(2, 2, 3)
# plt.stem(y3_fft_ang)
# plt.title('y3[n] = 0.25cos(8πn/N+π/2)')
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Faza [pi x rad]")
# # plt.axis((-0.2, 15.2, -1.1, 1.1))
#
# y4_fft_ang = np.angle/np.pi
# plt.subplot(2, 2, 4)
# plt.stem(y4_fft_ang)
# plt.title("y1+y2+y3")
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Faza [pi x rad]")
# # plt.axis((-0.2, 15.2, -1.1, 1.1))
#
# plt.tight_layout()
# plt.savefig("zad2.png")
# plt.show()










# N = 32
# f = 1
# n = np.arange(start=0, stop=N)
# y = np.sin(2*np.pi*f*n/N)
# fft = 2*np.fft.fft(y)/N
#
# plt.figure(figsize=(12, 14))
# plt.subplot(3, 2, 1)
# plt.stem(y)
# plt.title("Re(y)")
# plt.xlabel("Numer probki")
# plt.ylabel("Amplituda")
#
# y_im = np.imag(y)
# plt.subplot(3, 2, 2)
# plt.stem(y_im)
# plt.title("Im(y)")
# plt.xlabel("Numer probki")
# plt.ylabel("Amplituda")
#
# fft_abs = np.abs(fft)
# plt.subplot(3, 2, 3)
# plt.stem(fft_abs)
# plt.title("Modul(fft(y))")
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Magnituda")
#
# fft_ang = np.angle(fft)/np.pi
# plt.subplot(3, 2, 4)
# plt.stem(fft_ang)
# plt.title("Phase(fft(y))")
# plt.ylabel("Faza [pi x rad]")
# plt.xlabel("Numer pasma czestotliwosciowego")
#
# ifft = N*np.fft.ifft(fft)/2
# plt.subplot(3, 2, 5)
# plt.stem(ifft)
# plt.title("Re(ifft(y))")
# plt.ylabel("Amplituda")
# plt.xlabel("Numer probki")
#
# ifft_img = np.imag(ifft)
# plt.subplot(3, 2, 6)
# plt.stem(ifft_img)
# plt.title("Im(ifft(y))")
# plt.ylabel("Amplituda")
# plt.xlabel("Numer probki")
# plt.axis((-0.2, 15.2, -1.1, 1.1))
#
# plt.tight_layout()
# plt.savefig("zad3a.png")
# # plt.show()



# N = 32
# n = np.arange(start=0, stop=N)
# y1 = np.cos(2*np.pi*n/N + np.pi/4)
# y2 = 0.5*np.cos(4*np.pi*n/N)
# y3 = 0.25*np.cos(8*np.pi*n/N + np.pi/2)
# y4 = y1 + y2 + y3
#
# plt.figure(figsize=(12, 10))
# plt.subplot(2, 2, 1)
# plt.stem(y4)
# plt.title("y1+y2+y3")
# plt.xlabel("Numer Probki")
# plt.ylabel("Amplituda")
#
# fft = 2*np.fft.fft(y4)/N
# fft_abs = np.abs(fft)
# plt.subplot(2, 2, 2)
# plt.stem(fft_abs)
# plt.title("Modul Widma")
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Magnituda")
#
# fft_ang = np.angle(fft)/np.pi
# plt.subplot(2, 2, 3)
# plt.stem(fft_ang)
# plt.title("Faza Widma")
# plt.xlabel("Numer Pasma Czestotliwosciowego")
# plt.ylabel("Faza [pi x rad]")
#
# ifft = N*np.fft.ifft(fft)/2
# plt.subplot(2, 2, 4)
# plt.stem(ifft)
# plt.title("ifft(Y)")
# plt.xlabel("Numer Probki")
# plt.ylabel("Amplituda")
#
# plt.tight_layout()
# plt.savefig("zad3b.png")
# # plt.show()






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
# plt.savefig("zadanie4.png")







def DFT(y):
    n = len(y)
    dft_matrix = dft(n=n)
    return dft_matrix

def IDFT(y):
    pass






