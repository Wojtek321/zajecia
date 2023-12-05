import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import queue


downsample = 1
window = 1000
interval = 30
fs = 44100
q = queue.Queue()
length = int(window*fs/(1000*downsample))
plotdata = np.zeros((length, 1))

t = 5
n = np.arange(0, t, 1/fs)
data = np.zeros(t*fs)
n_frames = t*fs

devices = sd.query_devices()
mic_name = devices[1]['name']

fig, ax = plt.subplots()
plt.title("Real time microphone input")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
lines = plt.plot(plotdata)

def audio_callback(indata, frames, time, status):
    indata = np.sum(indata, axis=1)
    max_amplitude = max(abs(indata))
    indata /= max_amplitude

    q.put(indata[::downsample])


def update_plot(frame):
    global plotdata

    while True:
        try:
            data = q.get_nowait()
        except queue.Empty:
            break
        shift = len(data)
        plotdata = np.roll(plotdata, -shift, axis=0)
        plotdata[-shift:,:] = data
    for column, line in enumerate(lines):
        line.set_ydata(plotdata[:,0])
    return lines



input = sd.InputStream(samplerate=fs, channels=2, device=mic_name, callback=audio_callback)

ani = FuncAnimation(fig, update_plot, interval=interval, blit=True)

with input:
    plt.show()


