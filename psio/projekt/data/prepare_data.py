from utils import ITD, ILD, measurement_number
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from scipy.io import wavfile
from scipy.signal import convolve
from librosa import resample
from netCDF4 import Dataset
from joblib import dump
import numpy as np
import os



TIME = 0.1
SIGNALS_PATH = '../assets/signals'
SIGNALS = ['eyeofthetiger.wav', 'guitar.wav', 'music.wav', 'nirvana.wav', 'noise.wav', 'podcast.wav', 'shrek.wav', 'trumpet.wav', 'voice.wav']
SOFA_PATH = '../assets/sofa_files'
SOFA_FILES = ['mit.sofa', 'sadie.sofa']
angles = np.concatenate((range(0, 91, 5), range(270, 360, 5)))
X = []
Y = []



for sofa in SOFA_FILES:
    path = os.path.join(SOFA_PATH, sofa)

    sofa_file = Dataset(path, "r", format="NETCDF4")
    sofa_fs =  sofa_file['Data.SamplingRate'][:][0]

    ARR = sofa_file['SourcePosition'][:]


    for signal in SIGNALS:
        path = os.path.join(SIGNALS_PATH, signal)

        fs, data = wavfile.read(path)
        data = data / (np.max(np.abs(data)))
        data = data[:int(TIME * fs)]
        data = resample(data, orig_sr=fs, target_sr=sofa_fs)


        for angle in np.random.choice(angles, 20):
            idx = measurement_number(angle, ARR)

            H_l = sofa_file["Data.IR"][idx,1,:]
            H_r = sofa_file["Data.IR"][idx,0,:]

            Y_l = convolve(data, H_l)
            Y_r = convolve(data, H_r)

            itd = ITD(Y_l, Y_r, sofa_fs)
            ild = ILD(Y_l, Y_r)
            X.append([itd, ild])
            Y.append(angle)



scaler_x = MinMaxScaler()
scaler_y = MinMaxScaler()

X = scaler_x.fit_transform(X)

Y = np.array(Y).reshape(-1, 1)
Y = scaler_y.fit_transform(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

dump(scaler_x, '../data/scalers/scaler_x.joblib')
dump(scaler_y, '../data/scalers/scaler_y.joblib')
