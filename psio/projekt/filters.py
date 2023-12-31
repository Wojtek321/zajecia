from scipy.signal import butter, lfilter, freqz, filtfilt
import matplotlib.pyplot as plt
import numpy as np


FS = 44100
LOW_FREQ_CUTOFF = 1500
HIGH_FREQ_CUTOFF = 3000
ORDER = 6


# designing lowpass filter
normal_low_cutoff = LOW_FREQ_CUTOFF/(FS/2)
coefficients = butter(ORDER, normal_low_cutoff, btype='low', analog=False)
b_low = coefficients[0]
a_low = coefficients[1]


# designing highpass filter
normal_high_cutoff = HIGH_FREQ_CUTOFF/(FS/2)
coefficients = butter(ORDER, normal_high_cutoff, btype='high', analog=False)
b_high = coefficients[0]
a_high = coefficients[1]


def lowpass_filter(signal):
    # return lfilter(b_low, a_low, signal)
    return filtfilt(b_low, a_low, signal)


def highpass_filter(signal):
    # return lfilter(b_high, a_high, signal)
    return filtfilt(b_high, a_high, signal)


def main():
    fig, axs = plt.subplots(1, 2)
    fig.set_size_inches(14, 6)

    w, h = freqz(b_low, a_low, fs=FS)
    ax = axs[0]
    ax.plot(w, np.abs(h))
    ax.plot(LOW_FREQ_CUTOFF, 0.5*np.sqrt(2), 'ko')
    ax.axvline(LOW_FREQ_CUTOFF, color='k')
    ax.set_xlabel("Frequency [Hz]")
    ax.set_ylabel("Gain")
    ax.set_title("Lowpass filter frequency response")

    w, h = freqz(b_high, a_high, fs=FS)
    ax = axs[1]
    ax.plot(w, np.abs(h))
    ax.plot(HIGH_FREQ_CUTOFF, 0.5*np.sqrt(2), 'ko')
    ax.axvline(HIGH_FREQ_CUTOFF, color='k')
    ax.set_xlabel("Frequency [Hz]")
    ax.set_ylabel("Gain")
    ax.set_title("Highpass filter frequency response")

    fig.set_tight_layout(tight=True)
    plt.savefig("Filtry.png")

    # t = 0.01
    # fs = 44100
    # n = np.arange(0, t, 1/fs)
    # sin = np.sin(2*np.pi*500*n)
    # sin2 = np.sin(2*np.pi*2000*n)
    # plt.plot(sin)
    # plt.show()
    # plt.clf()
    # plt.plot(sin+sin2)
    # plt.show()
    # plt.clf()
    # plt.plot(lowpass_filter(sin+sin2))
    # plt.show()


if __name__ == "__main__":
    main()