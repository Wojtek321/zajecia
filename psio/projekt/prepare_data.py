import os
from scipy.io import wavfile
from scipy.signal import convolve
# from numpy import convolve
import numpy as np
from librosa import resample
from netCDF4 import Dataset
from ITD_ILD import ITD, ILD
import sounddevice as sd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, PolynomialFeatures
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from joblib import dump, load


TIME = 0.0001
SIGNALS_PATH = 'signals'
SIGNALS = ['eyeofthetiger.wav', 'guitar.wav', 'music2.wav', 'podcast.wav', 'shrek.wav', 'trumpet.wav']
SOFA_PATH = 'sofa_files'
SOFA_FILES = ['mit.sofa', 'sadie.sofa']
list1 = range(0, 91, 5)
list2 = range(270, 360, 5)
angles = np.concatenate((list1, list2))
ITDS = []
ILDS = []
Y = []

def measurement_number(az):
    condition1 = (ARR[:,0] == az)
    condition2 = (ARR[:,1] == 0)

    row_indices = np.where(np.all(np.logical_and(condition1[:, None], condition2[:, None]), axis=1))[0]
    return row_indices[0]


# for sofa in SOFA_FILES:
#     path = os.path.join(SOFA_PATH, sofa)
#
#     sofa_file = Dataset(path, "r", format="NETCDF4")
#     sofa_fs =  sofa_file['Data.SamplingRate'][:][0]
#     ears_distance = sofa_file['ReceiverPosition'][1, 1] - sofa_file['ReceiverPosition'][0, 1]
#     # print(f"fs: {sofa_fs}")
#     # print(f"distance: {ears_distance}")
#
#     ARR = sofa_file['SourcePosition'][:]
#
#
#     for signal in SIGNALS:
#         path = os.path.join(SIGNALS_PATH, signal)
#
#         fs, data = wavfile.read(path)
#         data = data / (np.max(np.abs(data)))
#         data = data[:TIME * fs]
#         data = resample(data, orig_sr=fs, target_sr=sofa_fs)
#
#
#         for angle in np.random.choice(angles, 15):
#             idx = measurement_number(angle)
#
#             H_l = sofa_file["Data.IR"][idx,1,:]
#             H_r = sofa_file["Data.IR"][idx,0,:]
#
#             Y_l = convolve(data, H_l)
#             Y_r = convolve(data, H_r)
#
#             ITDS.append(ITD(Y_l, Y_r, sofa_fs))
#             ILDS.append(ILD(Y_l, Y_r))
#             Y.append(angle)
#
#
#
# X = np.column_stack((ITDS, ILDS))
#
# scaler_x = MinMaxScaler()
# X = scaler_x.fit_transform(X)
# # print(X)
#
#
# Y = np.array(Y)
# Y = Y.reshape(-1, 1)
# scaler_y = MinMaxScaler()
# Y = scaler_y.fit_transform(Y)
# # print(Y)
#
#
#
#
# X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
#
#
# model = RandomForestRegressor()
# model.fit(X_train, Y_train)
# Y_pred = model.predict(X_test)
# print("random forest:")
# print('R2: ', r2_score(Y_test, Y_pred))
# print('MAE: ', mean_absolute_error(Y_test, Y_pred))
# print('MSE: ', mean_squared_error(Y_test, Y_pred))
# dump(model, 'model.joblib')
# dump(scaler_x, 'scaler_x.joblib')
# dump(scaler_y, 'scaler_y.joblib')

# model = SVR()
# model.fit(X_train, Y_train)
# Y_pred = model.predict(X_test)
# print("svr:")
# print('R2: ', r2_score(Y_test, Y_pred))
# print('MAE: ', mean_absolute_error(Y_test, Y_pred))
# print('MSE: ', mean_squared_error(Y_test, Y_pred))








model = load('model.joblib')
scaler_x = load('scaler_x.joblib')
scaler_y = load('scaler_y.joblib')



sofa_file = Dataset('sofa_files/sadie.sofa', "r", format="NETCDF4")
sofa_fs =  sofa_file['Data.SamplingRate'][:][0]
ears_distance = sofa_file['ReceiverPosition'][1, 1] - sofa_file['ReceiverPosition'][0, 1]
ARR = sofa_file['SourcePosition'][:]

fs, data = wavfile.read('signals/scooby.wav')
data = data / (np.max(np.abs(data)))
data = data[:int(TIME * fs)]
data = resample(data, orig_sr=fs, target_sr=sofa_fs)

angle = 90
idx = measurement_number(angle)

H_l = sofa_file["Data.IR"][idx,1,:]
H_r = sofa_file["Data.IR"][idx,0,:]

Y_l = convolve(data, H_l)
Y_r = convolve(data, H_r)

itd = ITD(Y_l, Y_r, sofa_fs)
ild = ILD(Y_l, Y_r)



X = np.array([itd, ild]).reshape(1, -1)
X = scaler_x.transform(X)


kat = model.predict(X)

print(scaler_y.inverse_transform(kat.reshape(1, -1)))