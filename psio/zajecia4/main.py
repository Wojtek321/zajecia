import numpy as np
import matplotlib.pyplot as plt
import wave
import struct


t = 5
f = 1000
fs = 8000
n = np.arange(0, t, 1/fs)

noise = np.random.normal(0, 1, len(n))
sin = np.sin(2*np.pi*f*n)
czesetotliwosc_zmienna = np.linspace(0, 1000, len(n))
sin_zmienny = np.sin(2 * np.pi * czesetotliwosc_zmienna * n)
with wave.open("nagranie.wav", 'r') as file:
    fs = file.getframerate()
    n_frames = file.getnframes()
    data = file.readframes(n_frames)
    sample_width = file.getsampwidth()
    samples = struct.unpack(f"{n_frames}h", data)
    max_amplitude = np.max(np.abs(samples))
    samples = samples / max_amplitude

def moc_sygnalu(alpha, signal):
    power = []
    power.append(0)

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
fig.set_tight_layout(tight=True)
plt.savefig("Zadanie1_1.png")



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