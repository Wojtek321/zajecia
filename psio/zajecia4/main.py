import numpy as np
import matplotlib.pyplot as plt
import wave
import struct
import sounddevice as sd
from scipy.signal import square, sawtooth, periodogram, spectrogram, chirp
from librosa.feature import melspectrogram
import librosa



t = 5
f = 1000
fs = 8000
n = np.arange(0, t, 1/fs)

noise = np.random.normal(0, 1, len(n))
sin = np.sin(2*np.pi*f*n)
czesetotliwosc_zmienna = np.linspace(0, 1000, len(n))
sin_zmienny = np.sin(2 * np.pi * czesetotliwosc_zmienna * n)
with wave.open("mowa.wav", 'r') as file:
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
ax.set_ylim(0, 2)
ax = axs[1,0]; ax.plot(n, sin); ax.set_title("Sygnal sinusoidalny o stalej czestotliwosci"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Amplituda")
ax = axs[1,1]; ax.plot(n, sin_power); ax.set_title("Sygnal sinusoidalny o stalej czestotliwosci - Obwiednia mocy, alpha=0.999"); ax.set_xlabel("Czas [s]")
ax.set_ylabel("Moc"); ax.set_ylim(0, 1)
ax = axs[2,0]; ax.plot(n, sin_zmienny); ax.set_title("Sygnal o zmiennej czestotliwosci"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Amplituda")
ax = axs[2,1]; ax.plot(n, sin_zmienny_power); ax.set_title("Sygnal o zmiennej czestotliwosci - Obwiednia mocy, alpha=0.999"); ax.set_xlabel("Czas [s]")
ax.set_ylabel("Moc"); ax.set_ylim(0, 1)
ax = axs[3,0]; ax.plot(n, samples); ax.set_title("Sygnal mowy"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Amplituda")
ax = axs[3,1]; ax.plot(n, samples_power); ax.set_title("Sygnal mowy - Obwiednia mocy, alpha=0.999"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Moc")
ax.set_ylim(0, 0.1)
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
ax.set_ylim(0, 2)
ax = axs[1,0]; ax.plot(n, sin); ax.set_title("Sygnal sinusoidalny o stalej czestotliwosci"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Amplituda")
ax = axs[1,1]; ax.plot(n, sin_power); ax.set_title("Sygnal sinusoidalny o stalej czestotliwosci - Obwiednia mocy, alpha=0.99"); ax.set_xlabel("Czas [s]")
ax.set_ylabel("Moc"); ax.set_ylim(0, 1)
ax = axs[2,0]; ax.plot(n, sin_zmienny); ax.set_title("Sygnal o zmiennej czestotliwosci"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Amplituda")
ax = axs[2,1]; ax.plot(n, sin_zmienny_power); ax.set_title("Sygnal o zmiennej czestotliwosci - Obwiednia mocy, alpha=0.99"); ax.set_xlabel("Czas [s]")
ax.set_ylabel("Moc"); ax.set_ylim(0, 1)
ax = axs[3,0]; ax.plot(n, samples); ax.set_title("Sygnal mowy"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Amplituda")
ax = axs[3,1]; ax.plot(n, samples_power); ax.set_title("Sygnal mowy - Obwiednia mocy, alpha=0.99"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Moc")
ax.set_ylim(0, 0.2)
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
ax.set_ylim(0, 20)
ax = axs[1,0]; ax.plot(n, sin); ax.set_title("Sygnal sinusoidalny o stalej czestotliwosci"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Amplituda")
ax = axs[1,1]; ax.plot(n, sin_power); ax.set_title("Sygnal sinusoidalny o stalej czestotliwosci - Obwiednia mocy, alpha=0.001"); ax.set_xlabel("Czas [s]")
ax.set_ylabel("Moc"); ax.set_ylim(0, 1)
ax = axs[2,0]; ax.plot(n, sin_zmienny); ax.set_title("Sygnal o zmiennej czestotliwosci"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Amplituda")
ax = axs[2,1]; ax.plot(n, sin_zmienny_power); ax.set_title("Sygnal o zmiennej czestotliwosci - Obwiednia mocy, alpha=0.001"); ax.set_xlabel("Czas [s]")
ax.set_ylabel("Moc"); ax.set_ylim(0, 1)
ax = axs[3,0]; ax.plot(n, samples); ax.set_title("Sygnal mowy"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Amplituda")
ax = axs[3,1]; ax.plot(n, samples_power); ax.set_title("Sygnal mowy - Obwiednia mocy, alpha=0.001"); ax.set_xlabel("Czas [s]"); ax.set_ylabel("Moc")
ax.set_ylim(0, 1)
fig.set_tight_layout(tight=True)
plt.savefig("Zadanie1_3.png")















f = 1000
fs = 16000
t = 2
n = np.arange(0, t, 1/fs)
frequency = np.linspace(1000, 2000, len(n))

sin = np.sin(2*np.pi * f * n)
sq = square(2*np.pi * f * n)
traingle = sawtooth(2*np.pi * f  * n, width=0.5)
saw = sawtooth(2*np.pi * f * n)
noise = np.random.normal(0, 1, fs * t)
max_amplitude = np.max(np.abs(noise))
noise = noise / max_amplitude
sin_var = chirp(n, f0=1000, f1=2000, t1=2, method='linear')
with wave.open("mowa.wav", 'r') as file:
    n_frames = file.getnframes()
    fs_mowy = file.getframerate()
    t_mowy = n_frames/fs_mowy
    n_mowy = np.arange(0, t_mowy, 1/fs_mowy)
    data = file.readframes(n_frames)
    mowa = struct.unpack(f"{n_frames}h", data)
    max_amplitude = np.max(np.abs(mowa))
    mowa = mowa / max_amplitude
with wave.open("muzyka.wav", 'r') as file:
    liczba_kanalow = file.getnchannels()
    liczba_bitow_na_probke = file.getsampwidth()
    n_frames = file.getnframes()

    fs_muzyki = file.getframerate()
    t_muzyki = n_frames / fs_muzyki
    n_muzyki = np.arange(0, t_muzyki-(1/fs_muzyki), 1 / fs_muzyki)

    data = file.readframes(n_frames)
    muzyka = struct.unpack(f"{n_frames * liczba_kanalow}h", data)
    muzyka = np.array(muzyka).reshape((-1, liczba_kanalow))
    muzyka = np.sum(muzyka, axis=1)
    max_amplitude = np.max(np.abs(muzyka))
    muzyka = muzyka / max_amplitude


sin_f, sin_pxx = periodogram(sin, fs)
sq_f, sq_pxx = periodogram(sq, fs)
traingle_f, traingle_pxx = periodogram(traingle, fs)
saw_f, saw_pxx = periodogram(saw, fs)
noise_f, noise_pxx = periodogram(noise, fs)
sin_var_f, sin_var_pxx = periodogram(sin_var, fs)
mowa_f, mowa_pxx = periodogram(mowa, fs_mowy)
muzyka_f, muzyka_pxx = periodogram(muzyka, fs_muzyki)

fig, axs = plt.subplots(8,2)
fig.set_size_inches(20, 18)
ax = axs[0,0]; ax.plot(n, sin); ax.set_xlim(0, 0.02); ax.set_title('Sygnal sinusoidalny o stalej czestotliwosci'); ax.set_ylabel("Amplituda")
ax.set_xlabel("Czas [s]")
ax = axs[0,1]; ax.plot(sin_f, 10*np.log10(np.abs(sin_pxx))); ax.set_title('Sygnal sinusoidalny o stalej czestotliwosci - periodogram')
ax.set_ylabel("Moc [dB]"); ax.set_xlabel("Czestotliwosc [Hz]")
ax = axs[1,0]; ax.plot(n, sq); ax.set_xlim(0, 0.02); ax.set_title('Sygnal prostokatny'); ax.set_ylabel("Amplituda"); ax.set_xlabel("Czas [s]")
ax = axs[1,1]; ax.plot(sq_f, 10*np.log10(np.abs(sq_pxx))); ax.set_title('Sygnal prostokatny - periodogram'); ax.set_ylabel("Moc [dB]")
ax.set_xlabel("Czestotliwosc [Hz]")
ax = axs[2,0]; ax.plot(n, traingle); ax.set_xlim(0, 0.02); ax.set_title('Sygnal trojkatny'); ax.set_ylabel("Amplituda"); ax.set_xlabel("Czas [s]")
ax = axs[2,1]; ax.plot(traingle_f, 10*np.log10(np.abs(traingle_pxx))); ax.set_title('Sygnal trojkatny - periodogram'); ax.set_ylabel("Moc [dB]")
ax.set_xlabel("Czestotliwosc [Hz]")
ax = axs[3,0]; ax.plot(n, saw); ax.set_xlim(0, 0.02); ax.set_title('Sygnal piloksztaltny'); ax.set_ylabel("Amplituda"); ax.set_xlabel("Czas [s]")
ax = axs[3,1]; ax.plot(saw_f, 10*np.log10(np.abs(saw_pxx))); ax.set_title('Sygnal piloksztaltny - periodogram'); ax.set_ylabel("Moc [dB]")
ax.set_xlabel("Czestotliwosc [Hz]")
ax = axs[4,0]; ax.plot(n, noise); ax.set_xlim(0, 0.02); ax.set_title('Sygnal szumu'); ax.set_ylabel("Amplituda"); ax.set_xlabel("Czas [s]")
ax = axs[4,1]; ax.plot(noise_f, 10*np.log10(np.abs(noise_pxx))); ax.set_title('Sygnal szumu - periodogram'); ax.set_ylabel("Moc [dB]")
ax.set_xlabel("Czestotliwosc [Hz]")
ax = axs[5,0]; ax.plot(n, sin_var); ax.set_xlim(0, 0.02); ax.set_title('Sygnal sinusoidalny o zmiennej czestotliwosci'); ax.set_ylabel("Amplituda")
ax.set_xlabel("Czas [s]")
ax = axs[5,1]; ax.plot(sin_var_f, 10*np.log10(np.abs(sin_var_pxx))); ax.set_title('Sygnal sinusoidalny o zmiennej czestotliwosci - periodogram')
ax.set_ylabel("Moc [dB]"); ax.set_xlabel("Czestotliwosc [Hz]")
ax = axs[6,0]; ax.plot(n_mowy, mowa); ax.set_xlim(0.05, 3.7); ax.set_title('Sygnal mowy'); ax.set_ylabel("Amplituda"); ax.set_xlabel("Czas [s]")
ax = axs[6,1]; ax.plot(mowa_f, 10*np.log10(np.abs(mowa_pxx))); ax.set_title('Sygnal mowy - periodogram'); ax.set_ylabel("Moc [dB]")
ax.set_xlabel("Czestotliwosc [Hz]")
ax = axs[7,0]; ax.plot(n_muzyki, muzyka); ax.set_title('Sygnal muzyki'); ax.set_ylabel("Amplituda"); ax.set_xlabel("Czas [s]")
ax = axs[7,1]; ax.plot(muzyka_f, 10*np.log10(np.abs(muzyka_pxx))); ax.set_title('Sygnal muzyki - periodogram'); ax.set_ylabel("Moc [dB]")
ax.set_xlabel("Czestotliwosc [Hz]")
fig.set_tight_layout(tight=True)
plt.savefig("Zadanie2.png")
















sin_f, sin_t, sin_Sxx = spectrogram(sin, fs, window='hamming', nperseg=1024)
sq_f, sq_t, sq_Sxx = spectrogram(sq, fs, window='hamming', nperseg=1024)
traingle_f, traingle_t, traingle_Sxx = spectrogram(traingle, fs, window='hamming', nperseg=1024)
saw_f, saw_t, saw_Sxx = spectrogram(saw, fs, window='hamming', nperseg=1024)
noise_f, noise_t, noise_Sxx = spectrogram(noise, fs, window='hamming', nperseg=1024)
sin_var_f, sin_var_t, sin_var_Sxx = spectrogram(sin_var, fs, window='hamming', nperseg=1024)
mowa_f, mowa_t, mowa_Sxx = spectrogram(mowa, fs_mowy, window='hamming', nperseg=1024)
muzyka_f, muzyka_t, muzyka_Sxx = spectrogram(muzyka, fs_muzyki, window='hamming', nperseg=1024)

fig, axs = plt.subplots(4, 2)
fig.set_size_inches(13, 18)
ax = axs[0,0]; mesh = ax.pcolormesh(sin_t, sin_f, 10*np.log10(sin_Sxx)); cb = fig.colorbar(mesh, ax=ax); cb.set_label("Moc/ [dB]")
ax.set_title('Sygnal sinusoidalny o stalej czestotliwosci'); ax.set_ylabel("Czestotliwosc [Hz]"); ax.set_xlabel("Czas [s]")
ax = axs[0,1]; mesh = ax.pcolormesh(sq_t, sq_f, 10*np.log10(sq_Sxx)); cb = fig.colorbar(mesh, ax=ax); cb.set_label("Moc/ [dB]")
ax.set_title('Sygnal prostokatny'); ax.set_ylabel("Czestotliwosc [Hz]"); ax.set_xlabel("Czas [s]")
ax = axs[1,0]; mesh = ax.pcolormesh(traingle_t, traingle_f, 10*np.log10(traingle_Sxx)); cb = fig.colorbar(mesh, ax=ax); cb.set_label("Moc [dB]")
ax.set_title('Sygnal trojkatny'); ax.set_ylabel("Czestotliwosc [Hz]"); ax.set_xlabel("Czas [s]")
ax = axs[1,1]; mesh = ax.pcolormesh(saw_t, saw_f, 10*np.log10(saw_Sxx)); cb = fig.colorbar(mesh, ax=ax); cb.set_label("Moc [dB]")
ax.set_title('Sygnal piloksztaltny'); ax.set_ylabel("Czestotliwosc [Hz]"); ax.set_xlabel("Czas [s]")
ax = axs[2,0]; mesh = ax.pcolormesh(noise_t, noise_f, 10*np.log10(noise_Sxx)); cb = fig.colorbar(mesh, ax=ax); cb.set_label("Moc [dB]")
ax.set_title('Sygnal szumu'); ax.set_ylabel("Czestotliwosc [Hz]"); ax.set_xlabel("Czas [s]")
ax = axs[2,1]; mesh = ax.pcolormesh(sin_var_t, sin_var_f, 10*np.log10(sin_var_Sxx)); cb = fig.colorbar(mesh, ax=ax); cb.set_label("Moc [dB]")
ax.set_title('Sygnal sinusoidalny o zmiennej czestotliwosci'); ax.set_ylabel("Czestotliwosc [Hz]"); ax.set_xlabel("Czas [s]")
ax = axs[3,0]; mesh = ax.pcolormesh(mowa_t, mowa_f, 10*np.log10(mowa_Sxx)); cb = fig.colorbar(mesh, ax=ax); cb.set_label("Moc [dB/Hz]")
ax.set_title('Sygnal mowy'); ax.set_ylabel("Czestotliwosc [Hz]"); ax.set_xlabel("Czas [s]")
ax = axs[3,1]; mesh = ax.pcolormesh(muzyka_t, muzyka_f, 10*np.log10(muzyka_Sxx)); cb = fig.colorbar(mesh, ax=ax); cb.set_label("Moc [dB]")
    ax.set_title('Sygnal muzyki'); ax.set_ylabel("Czestotliwosc [Hz]"); ax.set_xlabel("Czas [s]")
fig.set_tight_layout(tight=True)
plt.savefig("Zadanie3.png")


















sin_mel = melspectrogram(y=sin, sr=fs)
sq_mel = melspectrogram(y=sq, sr=fs)
tringle_mel = melspectrogram(y=traingle, sr=fs)
saw_mel = melspectrogram(y=saw, sr=fs)
noise_mel = melspectrogram(y=noise, sr=fs)
sin_var_mel = melspectrogram(y=sin_var, sr=fs)
mowa_mel = melspectrogram(y=mowa, sr=fs_mowy)
muzyka_mel = melspectrogram(y=muzyka, sr=fs_muzyki)

fig, axs = plt.subplots(4, 2)
fig.set_size_inches(13, 18)
ax = axs[0,0]; mel = librosa.display.specshow(librosa.power_to_db(sin_mel, ref=np.max), ax=ax, y_axis='mel', x_axis='time', sr=fs); cb = fig.colorbar(mel, ax=ax)
ax.set_title('Sygnal sinusoidalny o stalej czestotliwosci'); ax.set_ylabel("Czestotliwosc Melwoa [Mel]"); ax.set_xlabel("Czas [s]")
ax = axs[0,1]; mel = librosa.display.specshow(librosa.power_to_db(sq_mel, ref=np.max), ax=ax, y_axis='mel', x_axis='time', sr=fs); cb = fig.colorbar(mel, ax=ax)
ax.set_title('Sygnal prostokatny'); ax.set_ylabel("Czestotliwosc Melwoa [Mel]"); ax.set_xlabel("Czas [s]")
ax = axs[1,0]; mel = librosa.display.specshow(librosa.power_to_db(tringle_mel, ref=np.max), ax=ax, y_axis='mel', x_axis='time', sr=fs); cb = fig.colorbar(mel, ax=ax)
ax.set_title('Sygnal trojkatny'); ax.set_ylabel("Czestotliwosc Melwoa [Mel]"); ax.set_xlabel("Czas [s]")
ax = axs[1,1]; mel = librosa.display.specshow(librosa.power_to_db(saw_mel, ref=np.max), ax=ax, y_axis='mel', x_axis='time', sr=fs); cb = fig.colorbar(mel, ax=ax)
ax.set_title('Sygnal piloksztaltny'); ax.set_ylabel("Czestotliwosc Melwoa [Mel]"); ax.set_xlabel("Czas [s]")
ax = axs[2,0]; mel = librosa.display.specshow(librosa.power_to_db(noise_mel, ref=np.max), ax=ax, y_axis='mel', x_axis='time', sr=fs); cb = fig.colorbar(mel, ax=ax)
ax.set_title('Sygnal szumu'); ax.set_ylabel("Czestotliwosc Melwoa [Mel]"); ax.set_xlabel("Czas [s]")
ax = axs[2,1]; mel = librosa.display.specshow(librosa.power_to_db(sin_var_mel, ref=np.max), ax=ax, y_axis='mel', x_axis='time', sr=fs); cb = fig.colorbar(mel, ax=ax)
ax.set_title('Sygnal sinusoidalny o zmiennej czestotliwosci'); ax.set_ylabel("Czestotliwosc Melwoa [Mel]"); ax.set_xlabel("Czas [s]")
ax = axs[3,0]; mel = librosa.display.specshow(librosa.power_to_db(mowa_mel, ref=np.max), ax=ax, y_axis='mel', x_axis='time', sr=fs); cb = fig.colorbar(mel, ax=ax)
ax.set_title('Sygnal mowy'); ax.set_ylabel("Czestotliwosc Melwoa [Mel]"); ax.set_xlabel("Czas [s]")
ax = axs[3,1]; mel = librosa.display.specshow(librosa.power_to_db(muzyka_mel, ref=np.max), ax=ax, y_axis='mel', x_axis='time', sr=fs); cb = fig.colorbar(mel, ax=ax)
ax.set_title('Sygnal muzyki'); ax.set_ylabel("Czestotliwosc Melwoa [Mel]"); ax.set_xlabel("Czas [s]")
fig.set_tight_layout(tight=True)
plt.savefig("Zadanie4.png")

