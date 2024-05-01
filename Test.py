import numpy as np
import matplotlib.pyplot as plt

"""
# Definieren der Funktion y(t) durch Faltung von x(t) und h(t)
def y(t, T):
    dt = t[1] - t[0]
    y_values = convolve(x(t, T), h(t, T)) * dt  # Faltung
    t_y = np.linspace(2*t[0], 2*t[-1], len(y_values))  # Zeitbereich für y(t)
    return t_y, y_values
# Berechnen der Werte für y(t)
t_y, y_values = y(t, T)

# Erstellen des Plots für y(t)
plt.figure(figsize=(6, 4))
plt.plot(t_y, y_values, label='$y(t)$')
plt.title('Ausgangssignal $y(t)$')
plt.xlabel('Zeit (t)')
plt.grid(True)
plt.legend()
plt.xticks([-T, 0, T], ['-T', '0', '+T'])
plt.xlim([t_y[0], t_y[-1]])
plt.show()

def y2(t, T):
    dt = t[1] - t[0]
    # Faltung von y1(t) und h(t)
    t_y1, y1_values = y(t, T)  # Berechnen der Werte für y1(t)
    h_values = h(t, T)
    y2_values = np.convolve(y1_values, h_values, mode='full') * dt

    # Zeitbereich für y2(t)
    t_y2 = np.linspace(2*t[0], 2*t[-1], len(y2_values))

    return t_y2, y2_values

# Berechnen der Werte für y2(t)
t_y2, y2_values = y2(t, T)


# Erstellen des Plots für y1(t)
plt.figure(figsize=(6, 4))
plt.plot(t_y, y_values, label='$y_1(t)$')
plt.title('Ausgangssignal $y_1(t)$')
plt.xlabel('Zeit (t)')
plt.grid(True)
plt.legend()
plt.xticks([-T, 0, T], ['-T', '0', '+T'])
plt.xlim([t_y[0], t_y[-1]])
plt.show()


# Erstellen des Plots für y2(t)
plt.figure(figsize=(6, 4))
plt.plot(t_y2, y2_values, label='$y_2(t)$')
plt.title('Ausgangssignal $y_2(t)$')
plt.xlabel('Zeit (t)')
plt.grid(True)
plt.legend()
#plt.xticks([-T, 0, T], ['-T', '0', '+T'])
plt.xlim([t_y2[0], t_y2[-1]])
plt.show()

# Funktion für y10(t) durch Kaskadierung von 10 LTI-Systemen mit h(t) als Impulsantwort
def y10(t, T, num_systems):
    dt = t[1] - t[0]
    # Berechne die Faltung von x(t) mit h(t) für jedes LTI-System
    y_values = x(t, T)
    h_values = h(t, T)
    for _ in range(num_systems):
        y_values = np.convolve(y_values, h_values, mode='same') * dt
    # Zeitbereich für y10(t)
    t_y10 = np.linspace(2*t[0], 2*t[-1], len(y_values))
    return t_y10, y_values

# Anzahl der LTI-Systeme in der Kaskade
num_systems = 10

# Berechnen der Werte für y10(t)
t_y10, y10_values = y10(t, T, num_systems)

# Plot von y10(t) mit erweiterter x-Achse
plt.figure(figsize=(12, 6))
plt.plot(t_y10, y10_values, label='$y_{10}(t)$', color='green')
plt.title('Output signal $y_{10}(t)$ of a cascade of 10 LTI systems')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.xlim([-10, 10])  # Grenzen der x-Achse von -10 bis 10
plt.show()
"""