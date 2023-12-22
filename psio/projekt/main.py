import timeit
import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import queue
from scipy.fft import fft, fftfreq
from scipy.io import wavfile
import time
import timeit
from pprint import pprint
from threading import Thread
import tkinter as tk
import random
# import pyaudio
from PIL import Image, ImageTk



TIME = 2
ANIMATION_INTERVAL = 30
FS = 44100
HEAD_WIDTH = 0.15
AMOUNT_OF_SPEAKERS = 9
DOWNSAMPLE = 1

ARROW_LENGTH = 200
HEIGHT = 390
WIDTH = 600
WIDTH_SPEAKER = 30
HEIGHT_SPEAKER = 30
ANGLE = 180/(AMOUNT_OF_SPEAKERS-1)
N = TIME*FS


devices = sd.query_devices()
# print(devices)
mic1 = devices[1]['name']
mic2 = devices[2]['name']
# print(mic1)
# print(mic2)

n = np.arange(0, TIME, 1/FS)
plotdata = np.zeros((N, 1))

fig, ax = plt.subplots()
line, = ax.plot(n, plotdata)


q = queue.Queue()


max_offset = HEAD_WIDTH/340
interval = 2*max_offset/AMOUNT_OF_SPEAKERS

# print("max offset: ", max_offset)
# print("interval: ", interval)

dict_of_intervals = {}
for i in range(-(AMOUNT_OF_SPEAKERS//2), (AMOUNT_OF_SPEAKERS//2)+1):
    dict_of_intervals[((i-0.5)*interval, (i+0.5)*interval)] = i+(AMOUNT_OF_SPEAKERS//2)+1

# pprint(dict_of_intervals)









def categoriser(sig, refsig):
    delay, _ = gcc_phat(sig, refsig)
    delay = round(delay, 15)
    return [value for key, value in dict_of_intervals.items() if is_between(delay, key)]


def is_between(delay, scope):
    return scope[0] <= delay < scope[1]


def plot_init():
    fig.set_size_inches(6, 4)
    ax.set_title("Real time microphone input")
    ax.set_xlabel("Time [s]")
    ax.set_ylabel("Amplitude")
    ax.set_ylim(-1.1, 1.1)
    line.set_ydata(plotdata)
    fig.set_tight_layout(tight=True)

    return line,


# file_path = "039.wav"
# _, muzyka = wavfile.read(file_path)
# muzyka = np.array(muzyka)
# muzyka = np.sum(muzyka, axis=1)
# max_amplitude = np.max(np.abs(muzyka))
# muzyka = muzyka/ max_amplitude
# muzyka = muzyka[:1136]
#
# zera = np.zeros(11)
# przesuniety = np.concatenate((zera, muzyka))


def audio_callback1(indata, frames, time, status):
    data = np.sum(indata, axis=1)/2
    # i = random.randint(0, 10)
    # zera = np.zeros(i)
    # przesuniety = np.concatenate((zera, muzyka))
    # speaker_no = categoriser(muzyka, przesuniety)[0]
    #
    # update_arrow(dictionary_arrow[speaker_no][0], dictionary_arrow[speaker_no][1])
    # print(len(data))
    print("1")
    q.put(data[::DOWNSAMPLE])

def audio_callback2(indata, frames, time, status):
    data = np.sum(indata, axis=1)/2
    print("2")
    q.put(data[::DOWNSAMPLE])


def update_plot(frame):
    global plotdata

    while True:
        try:
            data = q.get_nowait()
        except queue.Empty:
            break
        n_samples = len(data)
        plotdata = np.roll(plotdata, -n_samples, axis=0)
        plotdata[-n_samples:, :] = data.reshape((-1, 1))

    line.set_ydata(plotdata)

    return line,


def gcc_phat(sig, refsig, fs=44100, max_tau=None, interp=16):
    '''
    This function computes the offset between the signal sig and the reference signal refsig
    using the Generalized Cross Correlation - Phase Transform (GCC-PHAT)method.
    '''

    # make sure the length for the FFT is larger or equal than len(sig) + len(refsig)
    n = sig.shape[0] + refsig.shape[0]

    # Generalized Cross Correlation Phase Transform
    SIG = np.fft.rfft(sig, n=n)
    REFSIG = np.fft.rfft(refsig, n=n)
    R = SIG * np.conj(REFSIG)

    cc = np.fft.irfft(R / np.abs(R), n=(interp * n))

    max_shift = int(interp * n / 2)
    if max_tau:
        max_shift = np.minimum(int(interp * fs * max_tau), max_shift)

    cc = np.concatenate((cc[-max_shift:], cc[:max_shift + 1]))

    # find max cross correlation index
    shift = np.argmax(np.abs(cc)) - max_shift

    tau = shift / float(interp * fs)

    return tau, cc



def coordinates_of_speakers(angle):
    x = WIDTH / 2 - np.cos(np.radians(angle)) * 250 - 27
    y = HEIGHT - np.sin(np.radians(angle)) * 250 - 110
    return x,y


def coordinates_of_arrow(angle):
    x = WIDTH / 2 - np.cos(np.radians(angle)) * ARROW_LENGTH - 3
    y = HEIGHT - np.sin(np.radians(angle)) * ARROW_LENGTH - 85
    return x-15, y+15


dictionary_arrow = {}
for i in range(0,AMOUNT_OF_SPEAKERS):
    x,y = coordinates_of_arrow(ANGLE*i)
    dictionary_arrow[i+1] = (x+15,y+15)
# pprint(dictionary_arrow)



root = tk.Tk()
root.resizable(width=False, height=False)
root.configure(background='#00c3e3')
root.title("yś")
root.geometry('600x400')
line_canvas = tk.Canvas(root, highlightthickness=0, width=620, height=400, background='#00c3e3')
line_canvas.place(x=0, y=0)

angle_of_rotate = 0
for i in range(0,AMOUNT_OF_SPEAKERS):
    speakers_canvas = tk.Canvas(root,highlightthickness=0, width=70, height=70,background='#00c3e3')
    speakers_canvas.pack()
    original_image = Image.open("speaker.png")
    resized_image = original_image.resize((90, 90))

    rotated_image = resized_image.rotate(angle_of_rotate)
    image = ImageTk.PhotoImage(rotated_image)
    speakers_canvas.image = image
    speakers_canvas.create_image(-3,-2,image=image,anchor='nw')
    angle = i * ANGLE
    x, y = coordinates_of_speakers(angle)
    speakers_canvas.place(x=x - 15, y=y + 15)

    angle_of_rotate -= ANGLE



# file_path = "039.wav"
# _, muzyka = wavfile.read(file_path)
# muzyka = np.array(muzyka)
# muzyka = np.sum(muzyka, axis=1)
# max_amplitude = np.max(np.abs(muzyka))
# muzyka = muzyka/ max_amplitude
# muzyka = muzyka[:1136]
#
# zera = np.zeros(11)
# przesuniety = np.concatenate((zera, muzyka))
#
#
# speaker = categoriser(muzyka, przesuniety)[0]
# print(speaker)


def update_arrow(x, y):
    line_canvas.coords(arrow, 300, 334, x, y)


def update(i):
    if i<=AMOUNT_OF_SPEAKERS:
        x = dictionary_arrow[i][0]
        y = dictionary_arrow[i][1]
        line_canvas.coords(arrow, 300, 334, x, y)
        root.after(600, update, i+1)
    else:
        root.after(0, update, 1)



arrow = line_canvas.create_line(300, 334, dictionary_arrow[5][0], dictionary_arrow[5][1], fill='red', width=10, arrow='last')


root.after(600, update, 1)

# def pierwszy():
#     print("Thread 1 started")
#     input1 = sd.InputStream(samplerate=FS, channels=2, device=1, callback=audio_callback1)
#     with input1:
#         print(f"input1: {input1.active}")
#
# def drugi():
#     print("Thread 2 started")
#     input2 = sd.InputStream(samplerate=FS, channels=2, device=2, callback=audio_callback2)
#     with input2:
#         print(f"input2: {input2.active}")

# input1 = sd.InputStream(samplerate=FS, channels=2, device=1, callback=audio_callback1)
#
# input2 = sd.InputStream(samplerate=FS, channels=2, device=2, callback=audio_callback2)


# ani = FuncAnimation(fig, update_plot, init_func=plot_init, interval=ANIMATION_INTERVAL, blit=True, cache_frame_data=False)

# thread1 = Thread(target=pierwszy)
# thread2 = Thread(target=drugi)
#
# thread1.start()
# thread2.start()
# # plt.show()
# print(f"Thread 1 alive: {thread1.is_alive()}")
# print(f"Thread 2 alive: {thread2.is_alive()}")
# root.mainloop()
# thread1.join()
# thread2.join()


# with input1 and input2:
#
#     print(input1.is_active())
#     print(input2.is_active())
#     plt.show()
root.mainloop()

