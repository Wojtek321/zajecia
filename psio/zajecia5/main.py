import numpy as np
import matplotlib.pyplot as plt


N = 32
n = np.arange(0, N)
x1 = np.sin(2*np.pi*n/N)
x2 = np.ones((32))

def Sa(x):
    return 2 * x

def Sb(x):
    return x + 1

def Sc(x):
    wynik = []
    for i in range(0, len(x)-1):
        wynik.append(x[i+1] - x[i])
    return wynik


fig, axs = plt.subplots(2, 2)
fig.set_size_inches(14, 10)
ax = axs[0,0]; ax.plot(x1); ax.set_title("x1[n]"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki"); ax.set_ylim(-1, 4)
ax = axs[0,1]; ax.plot(x2); ax.set_title("x2[n]"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki"); ax.set_ylim(0, 4)
ax = axs[1,0]; ax.plot(Sa(x1) + Sa(x2)); ax.set_title("S{x1[n]} + S{x2[n]}"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki"); ax.set_ylim(0, 4)
ax = axs[1,1]; ax.plot(Sa(x1 + x2)); ax.set_title("S{x1[n] + x2[n]}"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki"); ax.set_ylim(0, 4)
fig.set_tight_layout(tight=True)
plt.savefig("Zadanie1_a")


fig, axs = plt.subplots(2, 2)
fig.set_size_inches(14, 10)
ax = axs[0,0]; ax.plot(x1); ax.set_title("x1[n]"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki"); ax.set_ylim(-1, 4)
ax = axs[0,1]; ax.plot(x2); ax.set_title("x2[n]"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki"); ax.set_ylim(0, 4)
ax = axs[1,0]; ax.plot(Sb(x1) + Sb(x2)); ax.set_title("S{x1[n]} + S{x2[n]}"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki"); ax.set_ylim(0, 4)
ax = axs[1,1]; ax.plot(Sb(x1 + x2)); ax.set_title("S{x1[n] + x2[n]}"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki"); ax.set_ylim(0, 4)
fig.set_tight_layout(tight=True)
plt.savefig("Zadanie1_b")


a = Sc(x1)
b = Sc(x2)
c = []
for i in range(0, len(a)):
    c.append(a[i]+b[i])


fig, axs = plt.subplots(2, 2)
fig.set_size_inches(14, 10)
ax = axs[0,0]; ax.plot(x1); ax.set_title("x1[n]"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki"); ax.set_ylim(-1, 4)
ax = axs[0,1]; ax.plot(x2); ax.set_title("x2[n]"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki"); ax.set_ylim(0, 4)
ax = axs[1,0]; ax.plot(c); ax.set_title("S{x1[n]} + S{x2[n]}"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki"); ax.set_ylim(-0.3, 0.3)
ax = axs[1,1]; ax.plot(Sc(x1 + x2)); ax.set_title("S{x1[n] + x2[n]}"); ax.set_ylabel("Amplituda"); ax.set_xlabel("Numer probki"); ax.set_ylim(-0.3, 0.3)
fig.set_tight_layout(tight=True)
plt.savefig("Zadanie1_c")


