import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import queue


TIME = 3
ANIMATION_INTERVAL = 30
FS = 44100
RMS_THRESHOLD = 0.05

devices = sd.query_devices()
# print(devices)
mic_name = devices[1]['name']

n = np.arange(0, TIME, 1/FS)
plotdata = np.zeros((TIME*FS, 1))

q = queue.Queue()

fig, ax = plt.subplots()
line, = plt.plot(n, plotdata)


def plot_init():
    plt.title("Real time microphone input")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    ax.set_ylim(-1.1, 1.1)
    line.set_ydata(plotdata)
    return line,


def audio_callback(indata, frames, time, status):
    indata = np.sum(indata, axis=1)

    q.put(indata)


def RMS(indata):
    return np.sqrt(np.mean([pow(x, 2) for x in indata]))


def update_plot(frame):
    global plotdata

    while True:
        try:
            data = q.get_nowait()
        except queue.Empty:
            break

        shift = len(data)
        plotdata = np.roll(plotdata, -shift, axis=0)

        print(RMS(data))
        if(RMS(data) < RMS_THRESHOLD):
            data = np.zeros(len(data))

        plotdata[-shift:,:] = np.reshape(data, (-1, 1))


    line.set_ydata(plotdata)
    # ax.set_ylim(min(plotdata), max(plotdata))
    return line,



input = sd.InputStream(samplerate=FS, channels=2, device=1, callback=audio_callback)

ani = FuncAnimation(fig, update_plot, init_func=plot_init, interval=ANIMATION_INTERVAL, blit=True, cache_frame_data=False)

with input:
    plt.show()
