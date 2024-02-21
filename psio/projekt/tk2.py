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
import math



FS = 44100
HEAD_WIDTH = 0.15
AMOUNT_OF_SPEAKERS = 9

ARROW_LENGTH = 200
HEIGHT = 400
WIDTH = 600
WIDTH_SPEAKER = 30
HEIGHT_SPEAKER = 30
ANGLE = 180/(AMOUNT_OF_SPEAKERS-1)

size_X = 600
size_Y = 400


max_offset = HEAD_WIDTH/340
interval = 2*max_offset/AMOUNT_OF_SPEAKERS

# print("max offset: ", max_offset)
# print("interval: ", interval)

# dict_of_intervals = {}
# for i in range(-(AMOUNT_OF_SPEAKERS//2), (AMOUNT_OF_SPEAKERS//2)+1):
#     dict_of_intervals[((i-0.5)*interval, (i+0.5)*interval)] = i+(AMOUNT_OF_SPEAKERS//2)+1

# pprint(dict_of_intervals)






def coordinates_of_speakers(angle):
    x = WIDTH / 2 - np.cos(np.radians(angle)) * 250 - 27
    y = HEIGHT - np.sin(np.radians(angle)) * 250 - 110
    return x,y


def coordinates_of_arrow(angle):
    x = WIDTH / 2 - np.cos(np.radians(angle)) * ARROW_LENGTH
    y = HEIGHT - np.sin(np.radians(angle)) * ARROW_LENGTH - 85
    return x-15, y+15


dictionary_arrow = {}
for i in range(0,AMOUNT_OF_SPEAKERS):
    x,y = coordinates_of_arrow(ANGLE*i)
    dictionary_arrow[i+1] = (x+15,y+15)
#pprint(dictionary_arrow)



root = tk.Tk()
root.resizable(width=False, height=False)
root.configure(background='#00c3e3')
root.title("yś")
root.geometry(f'{size_X}x{size_Y}')
line_canvas = tk.Canvas(root, highlightthickness=0, width=620, height=400, background='#00c3e3')
line_canvas.place(x=0, y=0)


#glosniki
angle_of_rotate = 0
for i in range(0,AMOUNT_OF_SPEAKERS):
    speakers_canvas = tk.Canvas(root,highlightthickness=0, width=70, height=70,background='#00c3e3')
    speakers_canvas.pack()
    original_image = Image.open("assets/images/speaker.png")
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


# def update(i):
#     if i<=AMOUNT_OF_SPEAKERS:
#         x = dictionary_arrow[i][0]
#         y = dictionary_arrow[i][1]
#         line_canvas.coords(arrow, 300, 334, x, y)
#         root.after(600, update, i+1)
#     else:
#         root.after(0, update, 1)

def angle_rounding(angle):
    step = 180/(AMOUNT_OF_SPEAKERS-1)
    #print(step)
    angles_of_speakers = []
    for i in range(0,AMOUNT_OF_SPEAKERS+1):
        angles_of_speakers.append(i*step-(step/2))
    #pprint(angles_of_speakers)
    if angle not in angles_of_speakers:
        rounded_angle = round(angle / step) * step
    else:
        rounded_angle = math.ceil(angle / step) * step
    return rounded_angle

kat = 22.5
# kat_zaokraglony = angle_rounding(kat)
# print(kat_zaokraglony)
x, y = coordinates_of_arrow(kat + 90)
# x, y = coordinates_of_arrow(kat_zaokraglony + 90)
arrow = line_canvas.create_line(300, 345, x+15, y+15, fill='red', width=10, arrow='last')

#arrow = line_canvas.create_line(300, 334, dictionary_arrow[AMOUNT_OF_SPEAKERS//2+1][0], dictionary_arrow[AMOUNT_OF_SPEAKERS//2+1][1], fill='red', width=10, arrow='last')
if __name__ == '__main__':
    root.mainloop()

