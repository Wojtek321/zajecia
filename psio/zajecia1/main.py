import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import square, sawtooth


# x = np.arange(-10, 11)
# y = np.power(x, 2) + 5
# plt.plot(x, y)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.grid(True)
# plt.show()


x = np.arange(0, 2*np.pi, 0.2)
sin = np.sin(x)
cos = np.cos(x)
plt.plot(x, sin, label='sin(x)')
plt.plot(x, cos, label='cos(x)')
plt.legend()
# plt.grid(True)
plt.show()


# f = 1000
# A = 2
# fs = 10000
# t = np.linspace(0, 0.005, int(0.005*fs))
# y = A*np.sin(2*np.pi*f*t)
# plt.plot(t*1000, y)
# plt.xlabel('Czas [ms]')
# plt.ylabel('Napiecie [V]')
# plt.show()


# f = 1000
# t = np.linspace(0, 0.005, 1000)
# A = 2
# y = A*np.cos(2*np.pi*f*t)
# plt.plot(t, y)
# plt.xlabel('Czas [ms]')
# plt.ylabel('Napiecie [V]')
# plt.show()


# f = 1000
# t = np.linspace(0, 0.005, 1000)
# A = 2
# y = A*square(2*np.pi*f*t)
# plt.plot(t, y)
# plt.xlabel('Czas [ms]')
# plt.ylabel('Napiecie [V]')
# plt.show()


# f = 1000
# t = np.linspace(0, 0.005, 1000)
# A = 2
# y = A*sawtooth(2*np.pi*f*t, width=0.5)
# plt.plot(t, y)
# plt.xlabel('Czas [ms]')
# plt.ylabel('Napiecie [V]')
# plt.show()


# f = 1000
# t = np.linspace(0, 0.005, 1000)
# A = 2
# y = A*sawtooth(2*np.pi*f*t)
# plt.plot(t, y)
# plt.xlabel('Czas [ms]')
# plt.ylabel('Napiecie [V]')
# plt.show()


for i in range(0, 11):
    print(str(i).strip("\n"))