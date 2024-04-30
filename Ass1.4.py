import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve


# Definieren Sie die Funktionen x(t) und h(t)
def x(t, T):
    return np.where(np.abs(t) <= T/2, 1, 0)

def h(t, T):
    return np.where(np.abs(t) <= T/2, 1, 0)

# Definieren Sie den Zeitbereich und T
T = 2
t = np.linspace(-T, T, 1000)

# Berechnen Sie die Werte für x(t) und h(t)
x_values = x(t, T)
h_values = h(t, T)
"""
# Erstellen Sie die Plots
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(t, x_values, label='x(t)')
plt.title('x(t)')
plt.xlabel('Zeit (t)')
plt.grid(True)
plt.legend()
plt.xticks([-T/2, T/2], ['-T/2', 'T/2'])  # Setzen Sie die x-Achsen-Ticks
plt.xlim([-T, T])  # Setzen Sie die Grenzen der x-Achse

plt.subplot(1, 2, 2)
plt.plot(t, h_values, label='h(t)')
plt.title('h(t)')
plt.xlabel('Zeit (t)')
plt.grid(True)
plt.legend()
plt.xticks([-T/2, T/2], ['-T/2', 'T/2'])  # Setzen Sie die x-Achsen-Ticks
plt.xlim([-T, T])  # Setzen Sie die Grenzen der x-Achse

plt.tight_layout()
plt.show()

"""
# Definieren Sie die Funktion y(t) durch Faltung von x(t) und h(t)
def y(t, T):
    dt = t[1] - t[0]  # Zeitinkrement
    y_values = convolve(x(t, T), h(t, T)) * dt  # Faltung
    t_y = np.linspace(2*t[0], 2*t[-1], len(y_values))  # Zeitbereich für y(t)
    return t_y, y_values

# Berechnen Sie die Werte für y(t)
t_y, y_values = y(t, T)

# Erstellen Sie den Plot für y(t)
plt.figure(figsize=(6, 4))
plt.plot(t_y, y_values, label='$y_1(t)$')
plt.title('Ausgangssignal $y_1(t)$')
plt.xlabel('Zeit (t)')
plt.grid(True)
plt.legend()
plt.xticks([-T, 0, T], ['-T', '0', '+T'])  # Setzen Sie die x-Achsen-Ticks
plt.xlim([t_y[0], t_y[-1]])  # Setzen Sie die Grenzen der x-Achse
plt.show()

