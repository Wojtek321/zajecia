import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
from scipy.signal import convolve
from scipy.fft import fft, ifft


# N = 32
# n = np.arange(0, N)
# x1 = np.sin(2*np.pi*n/N)
# x2 = np.ones((32))
#
# def Sa(x):
#     return 2 * x
#
# def Sb(x):
#     return x + 1
#
# def Sc(x):
#     wynik = []
#     for i in range(0, len(x)-1):
#         wynik.append(x[i+1] - x[i])
#     return wynik
#
#
# fig, axs = plt.subplots(2, 2)
# fig.set_size_inches(14, 10)
# ax = axs[0,0]; ax.plot(x1); ax.set_title("x1[n]"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki"); ax.set_ylim(-1, 4)
# ax = axs[0,1]; ax.plot(x2); ax.set_title("x2[n]"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki"); ax.set_ylim(0, 4)
# ax = axs[1,0]; ax.plot(Sa(x1) + Sa(x2)); ax.set_title("S{x1[n]} + S{x2[n]}"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki"); ax.set_ylim(0, 4)
# ax = axs[1,1]; ax.plot(Sa(x1 + x2)); ax.set_title("S{x1[n] + x2[n]}"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki"); ax.set_ylim(0, 4)
# fig.set_tight_layout(tight=True)
# plt.savefig("Zadanie1_a")
#
#
# fig, axs = plt.subplots(2, 2)
# fig.set_size_inches(14, 10)
# ax = axs[0,0]; ax.plot(x1); ax.set_title("x1[n]"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki"); ax.set_ylim(-1, 4)
# ax = axs[0,1]; ax.plot(x2); ax.set_title("x2[n]"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki"); ax.set_ylim(0, 4)
# ax = axs[1,0]; ax.plot(Sb(x1) + Sb(x2)); ax.set_title("S{x1[n]} + S{x2[n]}"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki"); ax.set_ylim(0, 4)
# ax = axs[1,1]; ax.plot(Sb(x1 + x2)); ax.set_title("S{x1[n] + x2[n]}"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki"); ax.set_ylim(0, 4)
# fig.set_tight_layout(tight=True)
# plt.savefig("Zadanie1_b")
#
#
# fig, axs = plt.subplots(2, 2)
# fig.set_size_inches(14, 10)
# ax = axs[0,0]; ax.plot(x1); ax.set_title("x1[n]"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki"); ax.set_ylim(-1, 4)
# ax = axs[0,1]; ax.plot(x2); ax.set_title("x2[n]"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki"); ax.set_ylim(0, 4)
# ax = axs[1,0]; ax.plot(np.add(Sc(x1), Sc(x2))); ax.set_title("S{x1[n]} + S{x2[n]}"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki"); ax.set_ylim(-0.3, 0.3)
# ax = axs[1,1]; ax.plot(Sc(x1 + x2)); ax.set_title("S{x1[n] + x2[n]}"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki"); ax.set_ylim(-0.3, 0.3)
# fig.set_tight_layout(tight=True)
# plt.savefig("Zadanie1_c")











# N=64
# n = np.arange(0,N)
# x1 = np.sin(2*np.pi*n/N)
# x2 = np.sin(4*np.pi*n/N)
#
#
# k = 0
# h = np.zeros(64)
# h[k] = 1
# fig, axs = plt.subplots(3, 2)
# fig.set_size_inches(14, 10)
# ax = axs[0,0]; ax.plot(x1); ax.set_title("x1"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki")
# ax = axs[0,1]; ax.plot(convolve(x1, h)); ax.set_title("splot liniowy x1*h"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki")
# ax = axs[1,0]; ax.plot(x2); ax.set_title("x2"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki")
# ax = axs[1,1]; ax.plot(convolve(x2, h)); ax.set_title("splot liniowy x2*h"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki")
# ax = axs[2,0]; ax.stem(h); ax.set_title("h"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki")
# ax = axs[2,1]; ax.plot(convolve(x1, x2)); ax.set_title("splot liniowy x1*x2"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki")
# fig.set_tight_layout(tight=True)
# plt.savefig("Zadanie2_a")
#
#
# k = 16
# h = np.zeros(64)
# h[k] = 1
# fig, axs = plt.subplots(3, 2)
# fig.set_size_inches(14, 10)
# ax = axs[0,0]; ax.plot(x1); ax.set_title("x1"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki")
# ax = axs[0,1]; ax.plot(convolve(x1, h)); ax.set_title("splot liniowy x1*h"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki")
# ax = axs[1,0]; ax.plot(x2); ax.set_title("x2"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki")
# ax = axs[1,1]; ax.plot(convolve(x2, h)); ax.set_title("splot liniowy x2*h"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki")
# ax = axs[2,0]; ax.stem(h); ax.set_title("h"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki")
# ax = axs[2,1]; ax.plot(convolve(x1, x2)); ax.set_title("splot liniowy x1*x2"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki")
# fig.set_tight_layout(tight=True)
# plt.savefig("Zadanie2_b")
#
#
# k = 32
# h = np.zeros(64)
# h[k] = 1
# fig, axs = plt.subplots(3, 2)
# fig.set_size_inches(14, 10)
# ax = axs[0,0]; ax.plot(x1); ax.set_title("x1"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki")
# ax = axs[0,1]; ax.plot(convolve(x1, h)); ax.set_title("splot liniowy x1*h"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki")
# ax = axs[1,0]; ax.plot(x2); ax.set_title("x2"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki")
# ax = axs[1,1]; ax.plot(convolve(x2, h)); ax.set_title("splot liniowy x2*h"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki")
# ax = axs[2,0]; ax.stem(h); ax.set_title("h"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki")
# ax = axs[2,1]; ax.plot(convolve(x1, x2)); ax.set_title("splot liniowy x1*x2"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki")
# fig.set_tight_layout(tight=True)
# plt.savefig("Zadanie2_c")
#
#
# #test przemiennosci
# fig, axs = plt.subplots(3, 3)
# fig.set_size_inches(14, 10)
# ax = axs[0,0]; ax.plot(x1); ax.set_title("x1"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki")
# ax = axs[0,1]; ax.plot(convolve(x1, h)); ax.set_title("splot liniowy x1*h"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki")
# ax = axs[0,2]; ax.plot(convolve(h, x1)); ax.set_title("splot liniowy h*x1"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki")
# ax = axs[1,0]; ax.plot(x2); ax.set_title("x2"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki")
# ax = axs[1,1]; ax.plot(convolve(x2, h)); ax.set_title("splot liniowy x2*h"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki")
# ax = axs[1,2]; ax.plot(convolve(h, x2)); ax.set_title("splot liniowy h*x2"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki")
# ax = axs[2,0]; ax.stem(h); ax.set_title("h"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki")
# ax = axs[2,1]; ax.plot(convolve(x1, x2)); ax.set_title("splot liniowy x1*x2"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki")
# ax = axs[2,2]; ax.plot(convolve(x2, x1)); ax.set_title("splot liniowy x2*x1"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki")
# fig.set_tight_layout(tight=True)
# plt.savefig("Zadanie2_d")
#
#
# #test liniowosci
# fig, axs = plt.subplots(3, 2)
# fig.set_size_inches(14, 10)
# ax = axs[0,0]; ax.plot(x1); ax.set_title("x1"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki")
# ax = axs[0,1]; ax.plot(convolve(x1+x2, h)); ax.set_title("Splot sumy (x1+x2)*h"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki")
# ax = axs[1,0]; ax.plot(x2); ax.set_title("x2"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki")
# ax = axs[1,1]; ax.plot(convolve(x1, h) + convolve(x2, h)); ax.set_title("Suma splotow x1*h + x2*h"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki")
# ax = axs[2,0]; ax.stem(h); ax.set_title("h"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki")
# ax = axs[2,1]; ax.remove() #XD
# fig.set_tight_layout(tight=True)
# plt.savefig("Zadanie2_e")















# N=64
# n = np.arange(0,N)
#
# x = np.sin(2*np.pi*n/N)
# h = np.exp(-n/10)
# X = fft(x)
# H = fft(h)
# g = np.real(ifft(X*H))
# splot = convolve(x, h)
#
#
# fig, axs = plt.subplots(3, 2)
# fig.set_size_inches(14, 10)
# ax = axs[0,0]; ax.plot(x);  ax.set_title("x"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki")
# ax = axs[0,1]; ax.plot(h);  ax.set_title("h"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki")
# ax = axs[1,0]; ax.stem(np.abs(2*X/N));  ax.set_title("DFT(x)"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer pasma czestotliwosciowego")
# ax = axs[1,1]; ax.stem(np.abs(2*H/N));  ax.set_title("DFT(h)"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer pasma czestotliwosciowego")
# ax = axs[2,0]; ax.plot(g);  ax.set_title("IDFT(DFT(x) * DFT(h))"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki")
# ax = axs[2,1]; ax.plot(splot);  ax.set_title("Splot liniowy x*h"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki")
# fig.set_tight_layout(tight=True)
# plt.savefig("Zadanie3")










# file_path = "NaumburgBandshell.wav"
# _, bezechowe = wavfile.read(file_path)
# bezechowe = np.array(bezechowe)
# bezechowe = np.sum(bezechowe, axis=1)/2
# max_amplitude = np.max(np.abs(bezechowe))
# bezechowe = bezechowe/ max_amplitude
#
#
# file_path = "Space4ArtGallery.wav"
# _, sala = wavfile.read(file_path)
# sala = np.array(sala)
# sala = np.sum(sala, axis=1)/2
# max_amplitude = np.max(np.abs(sala))
# sala = sala / max_amplitude
#
#
# file_path = "SteinmanHall.wav"
# _, pokoj = wavfile.read(file_path)
# pokoj = np.array(pokoj)
# pokoj = np.sum(pokoj, axis=1)/2
# max_amplitude = np.max(np.abs(pokoj))
# pokoj = pokoj / max_amplitude
#
#
# splot1 = convolve(bezechowe, sala)
# splot2 = convolve(bezechowe, pokoj)
#
# fig, axs = plt.subplots(2, 3)
# fig.set_size_inches(14, 8)
# ax = axs[0,0]; ax.plot(bezechowe);  ax.set_title("Dzwiek nagrany w komorze bezechowej"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki")
# ax = axs[0,1]; ax.plot(sala);  ax.set_title("Dzwiek nagrany w sali"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki")
# ax = axs[0,2]; ax.plot(pokoj);  ax.set_title("Dzwiek nagrany w pokoju"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki")
# ax = axs[1,0]; ax.plot(splot1);  ax.set_title("Splot dzwieku z komory bezechowej oraz sali"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer pprobki")
# ax = axs[1,1]; ax.plot(splot2);  ax.set_title("Splot dzwieku z komory bezechowej oraz pokoju"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki")
# ax = axs[1,2]; ax.remove()
# fig.set_tight_layout(tight=True)
# plt.savefig("Zadanie4")

