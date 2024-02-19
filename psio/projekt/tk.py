import tkinter as tk
import numpy as np
from PIL import Image, ImageTk
from pprint import pprint

ARROW_LENGTH = 200
HEIGHT = 390
WIDTH = 600
AMOUNT_OF_SPEAKERS = 7
WIDTH_SPEAKER = 30
HEIGHT_SPEAKER = 30
ANGLE = 180/(AMOUNT_OF_SPEAKERS-1)



def coordinates_of_speakers(angle):
    x = WIDTH / 2 - np.cos(np.radians(angle)) * 250-27
    y = HEIGHT - np.sin(np.radians(angle)) * 250 -110
    return x,y

def coordinates_of_arrow(angle):
    x = WIDTH / 2 - np.cos(np.radians(angle)) * ARROW_LENGTH - 3
    y = HEIGHT - np.sin(np.radians(angle)) * ARROW_LENGTH - 85
    return x-15, y+15


dictionary_arrow = {}
for i in range(0,AMOUNT_OF_SPEAKERS):
    x,y = coordinates_of_arrow(ANGLE*i)
    dictionary_arrow[i+1] = (x,y)
# pprint(dictionary_arrow)


root = tk.Tk()
root.resizable(width=False, height=False)
root.configure(background='#00c3e3')
root.title("yś")
root.geometry('600x400')

line_canvas = tk.Canvas(root,highlightthickness=0, width=620, height=400, background='#00c3e3')
line_canvas.place(x=0, y=0)
line_canvas.create_line(300,334,dictionary_arrow[5][0]+15, dictionary_arrow[5][1]+15,fill='red', width=10, arrow='last')



# for i in range(0,AMOUNT_OF_SPEAKERS):
#     speakers_canvas = tk.Canvas(root, width=WIDTH_SPEAKER, height=HEIGHT_SPEAKER)
#     speakers_canvas.configure(bg='green')
#     angle = i*ANGLE
#     x,y = coordinates_of_speakers(angle)
#     speakers_canvas.place(x=x-15,y=y+15)
angle_of_rotate = 0
for i in range(0,AMOUNT_OF_SPEAKERS):
    speakers_canvas = tk.Canvas(root,highlightthickness=0, width=70, height=70,background='#00c3e3')
    speakers_canvas.pack()
    original_image = Image.open("assets/iamges/speaker.png")
    resized_image = original_image.resize((90, 90))

    rotated_image = resized_image.rotate(angle_of_rotate)
    image = ImageTk.PhotoImage(rotated_image)
    speakers_canvas.image = image
    speakers_canvas.create_image(-3,-2,image=image,anchor='nw')
    angle = i * ANGLE
    x, y = coordinates_of_speakers(angle)
    speakers_canvas.place(x=x - 15, y=y + 15)

    angle_of_rotate -= ANGLE

root.mainloop()