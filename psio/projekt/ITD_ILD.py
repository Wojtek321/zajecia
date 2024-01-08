from filters import lowpass_filter, highpass_filter
import numpy as np
from scipy.signal import convolve, correlate
from gcc_phat import gcc_phat
from pyroomacoustics.experimental.localization import tdoa



def ITD(Y_l, Y_r, fs=44100):
    Y_l = lowpass_filter(Y_l)
    Y_r = lowpass_filter(Y_r)

    # i = np.argmax(Y_l)
    # j = np.argmax(Y_r)
    #
    # return np.abs(i-j) / fs

    # itd, _ = gcc_phat(Y_r, Y_l)
    # return itd

    # cc = correlate(Y_r, Y_l, mode='full')
    # idx_lag = np.argmax(np.abs(cc))
    # toa_diff = idx_lag - 512
    #
    #
    # toa_diff = toa_diff / fs
    # return toa_diff

    # """
    # Ogólna korelacja krzyżowa z transformacją fazową (GCC-PHAT).
    #
    # Parametry:
    # - sig_x: Sygnał wejściowy 1
    # - sig_y: Sygnał wejściowy 2
    #
    # Zwraca:
    # - delay: Szacowane opóźnienie czasowe między sygnałami w próbkach
    # """

    # cross_corr = convolve(Y_l, Y_r[::-1], mode='full')
    # delay = np.argmax(np.abs(cross_corr)) - len(Y_l) + 1
    #
    # return np.abs(delay)/fs



    time = tdoa(Y_l, Y_r, fs=fs)
    return time


def ILD(Y_l, Y_r):
    Y_l = highpass_filter(Y_l)
    Y_r = highpass_filter(Y_r)

    l = sum(Y_l) / len(Y_l)
    r = sum(Y_r) / len(Y_r)

    return 20*np.log10(r/l)