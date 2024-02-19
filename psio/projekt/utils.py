from scipy.signal import butter, filtfilt, correlate, freqz
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
    return filtfilt(b_low, a_low, signal)


def highpass_filter(signal):
    return filtfilt(b_high, a_high, signal)


def ITD(Y_l, Y_r, fs=44100):
    Y_l = lowpass_filter(Y_l)
    Y_r = lowpass_filter(Y_r)

    n = len(Y_l)

    corr = correlate(Y_r, Y_l, mode='same') / np.sqrt(correlate(Y_l, Y_l, mode='same')[int(n / 2)] * correlate(Y_r, Y_r, mode='same')[int(n / 2)])

    delay_arr = np.linspace(-0.5 * n / fs, 0.5 * n / fs, n)
    delay = delay_arr[np.argmax(corr)]
    return delay


def ILD(Y_l, Y_r):
    Y_l = highpass_filter(Y_l)
    Y_r = highpass_filter(Y_r)

    l = sum(Y_l**2)
    r = sum(Y_r**2)

    return 10 * np.log10(l/r)


def measurement_number(az, ARR):
    condition1 = (ARR[:,0] == az)
    condition2 = (ARR[:,1] == 0)

    row_indices = np.where(np.all(np.logical_and(condition1[:, None], condition2[:, None]), axis=1))[0]
    return row_indices[0]




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
    plt.savefig("Filters_frequency_responses.png")


if __name__ == "__main__":
    main()