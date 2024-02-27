from utils.tools import ITD, ILD
from utils.consts import FS
from joblib import load
from gui.app import Window
import sounddevice as sd
import numpy as np
import os


MODEL = 'k_neighbors_regressor.joblib'

root = Window(round_to_speaker=True)

devices = sd.query_devices()
# print(devices)
mic_name = devices[1]['name']


model = load(os.path.join('modeling/models', MODEL))
scaler_x = load('data/scalers/scaler_x.joblib')
scaler_y = load('data/scalers/scaler_y.joblib')


def audio_callback(indata, frames, time, status):
    indata /= np.max(np.abs(indata))

    Y_l = indata[:,0]
    Y_r = indata[:,1]

    itd = ITD(Y_l, Y_r, fs=FS)
    ild = ILD(Y_l, Y_r)

    X = [itd, ild]
    X = scaler_x.transform(np.reshape(X, (1, -1)))
    Y = model.predict(X)
    Y = scaler_y.inverse_transform(np.reshape(Y, (-1, 1)))
    angle = np.ravel(Y)[0]
    print(angle)
    root.update_arrow(angle)



input = sd.InputStream(samplerate=FS, channels=2, device=mic_name, callback=audio_callback, blocksize=10000)


with input:
    root.mainloop()
