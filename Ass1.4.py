import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve

# Definieren der Funktionen x(t) und h(t)
def x(t, T):
    return np.where(np.abs(t) <= T/2, 1, 0)

def h(t, T):
    return np.where(np.abs(t) <= T/2, 1, 0)

# Definition des Zeitbereichs t und der Variable T
T = 1
t = np.linspace(-T, T, 1000)

x_values = x(t, T)
h_values = h(t, T)

# Erstellen des Plots
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(t, x_values, label='x(t)')
plt.title('x(t)')
plt.xlabel('Zeit (t)')
plt.grid(True)
plt.legend()
plt.xticks([-T/2, T/2], ['-T/2', 'T/2'])
plt.xlim([-T, T])

plt.subplot(1, 2, 2)
plt.plot(t, h_values, label='h(t)')
plt.title('h(t)')
plt.xlabel('Zeit (t)')
plt.grid(True)
plt.legend()
plt.xticks([-T/2, T/2], ['-T/2', 'T/2'])
plt.xlim([-T, T])

plt.tight_layout()
plt.show()

# Definition der Abtastfrequenz und der Anzahl von Samples
sample_rate = 100
num_samples = 500
T = sample_rate

# Erzeugung einer Rechteckwelle (Signal) mit einem Impuls zwischen 2*sample_rate und 3*sample_rate
wave = np.fromfunction(lambda i: (2 * sample_rate < i) & (i < 3 * sample_rate), (num_samples,)).astype(np.cfloat)

# Anzahl der Faltungen
num_convolutions = 10

# Initialisierung der Liste für die resultierenden Wellenformen
waves = [wave]

# Faltung der Rechteckwelle mit sich selbst und Normalisierung durch die Abtastfrequenz
for _ in range(num_convolutions):
    # Faltung des letzten Signals in der Liste mit der ursprünglichen Rechteckwelle und Normalisierung
    convolved_wave = np.convolve(waves[-1], wave, mode='same') / sample_rate
    # Hinzufügen des gefalteten Signals zur Liste
    waves.append(convolved_wave)

# Anpassen der x-Achse
x = np.arange(-num_samples//2, num_samples//2)

# Finden des Index des Maximums
max_index = np.argmax(waves[-1])
shifted_x = x - x[max_index]

# Plotten der gefalteten Welle mit verschobenen x-Werten
plt.figure(figsize=(10, 6))
plt.plot(shifted_x, waves[-1],)
plt.legend()
plt.grid()
plt.xlabel('Zeit t')
plt.xticks([-T, 0, T], ['-T', '0', '+T'])
plt.title('$y_{10}(t)$')
plt.show()




