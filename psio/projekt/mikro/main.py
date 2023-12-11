import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import queue
from scipy.fft import fft, fftfreq


# fs = 44100
# t = 2
# N = t*fs
# n = np.arange(0, t, 1/fs)
# f = 6
#
# sin = np.sin(2*np.pi*f*n)
# plt.plot(n,sin)
# plt.show()
#
# trans = 2*fft(sin)/N
# freq = fftfreq(N, 1/fs)
# plt.plot(freq, abs(trans))
# # plt.xlim(-10, 10)
# plt.show()

TIME = 2
ANIMATION_INTERVAL = 30
FS = 44100
DOWNSAMPLE = 1
N = TIME*FS


devices = sd.query_devices()
mic_name = devices[1]['name']

n = np.arange(0, TIME, 1/FS)

plotdata = np.zeros((N, 1))
freqs = fftfreq(N, 1/FS)
fftdata = np.zeros((N, 1))

fig, (ax1, ax2) = plt.subplots(1, 2)
line, = ax1.plot(n, plotdata)
fft_line, = ax2.plot(freqs, fftdata)

q = queue.Queue()


def plot_init():
    fig.set_size_inches(8, 4)
    ax1.set_title("Real time microphone input")
    ax1.set_xlabel("Time [s]")
    ax1.set_ylabel("Amplitude")
    ax1.set_ylim(-1.1, 1.1)

    ax2.set_title("Real time FFT")
    ax2.set_xlabel("Freq")
    ax2.set_ylabel("Amplitude")
    # ax2.set_ylim(0,2)
    # ax2.set_xlim(0,FS/2)

    line.set_ydata(plotdata)
    fft_line.set_ydata(fftdata)

    return line, fft_line

SIGNAL_THRESHOLD = 0.01
def audio_callback(indata, frames, time, status):
    data = np.sum(indata, axis=1)/2
    q.put(data[::DOWNSAMPLE])

    # signal_level = np.max(np.abs(data))
    # if signal_level > SIGNAL_THRESHOLD:
    #     fft_vals = np.abs(np.fft.fft(data))
    #     fft_vals = fft_vals[:len(fft_vals) // 2]
    #
    #     dominant_frequency_index = np.argmax(fft_vals)
    #     sample_rate = len(fft_vals) * FS // len(data)
    #     dominant_frequency = dominant_frequency_index * sample_rate / len(fft_vals)
        # print(f"Freq: {dominant_frequency:.2f} Hz")

def update_plot(frame):
    global plotdata, fftdata

    while True:
        try:
            data = q.get_nowait()
        except queue.Empty:
            break
        n_samples = len(data)
        plotdata = np.roll(plotdata, -n_samples, axis=0)
        plotdata[-n_samples:, :] = data.reshape((-1, 1))

        fftdata = np.abs(2*fft(plotdata))
        # fft_vals = np.abs(np.fft.fft(data))[:n_samples // 2]
        # fft_vals = fft_vals / np.max(fft_vals)
        # fftdata = np.roll(fftdata, -n_samples, axis=0)
        # fftdata[-n_samples // 2:, :] = fft_vals.reshape((-1, 1))

    line.set_ydata(plotdata)
    fft_line.set_ydata(fftdata)

    return line, fft_line



input = sd.InputStream(samplerate=FS, channels=2, device=1, callback=audio_callback)

ani = FuncAnimation(fig, update_plot, init_func=plot_init, interval=ANIMATION_INTERVAL, blit=True, cache_frame_data=False)


# with input:
#     fig.set_tight_layout(tight=True)
#     plt.show()


