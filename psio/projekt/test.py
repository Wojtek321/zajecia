from scipy.signal import correlate
import matplotlib.pyplot as plt
import numpy as np


# a = [1, 2, 3, 4]
# print([x**2 for x in a])

N = 32
fs = 1
n = np.arange(0, N)
a = 3*np.sin(2*np.pi * 3 * n / N + np.pi/2)
b = 5*np.sin(2*np.pi * 3 * n / N)
# b = 1.1*np.roll(a, 2)


corr = correlate(b, a, mode='same')

a_auto = correlate(a, a, mode='same')[int(N/2)]
b_auto = correlate(b, b, mode='same')[int(N/2)]

corr = corr / np.sqrt(a_auto * b_auto)

# delay_arr = np.linspace(-0.5 * N / fs, 0.5 * N / fs, N)
delay = np.argmax(corr) - int(N/2) + 1
print(delay)

plt.stem(a)
plt.grid(True)
plt.show()
plt.clf()
plt.stem(b)
plt.grid(True)
plt.show()
plt.clf()
plt.plot(corr)
plt.show()



# n = len(a)
# corr = correlate(b, a, mode='same') / np.sqrt(correlate(a, a, mode='same')[int(n / 2)] * correlate(b, b, mode='same')[int(n / 2)])
#
# delay_arr = np.linspace(-0.5 * n / fs, 0.5 * n / fs, n)
# delay = delay_arr[np.argmax(corr)]
