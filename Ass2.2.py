import numpy as np
import matplotlib.pyplot as plt

# Definiere die Parameter
alpha = 1.0
t = np.linspace(-1, 5, 1000)

# Definiere die Einheitssprungfunktion u(t)
u = np.heaviside(t, 1)

# Definiere die Impulsantwort h(t)
h = np.exp(-alpha * t) * u

# Plotten der Impulsantwort
plt.figure(figsize=(10, 6))
plt.plot(t, h, label=r'$h(t) = e^{-\alpha t} u(t)$')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title('Impulsantwort $h(t)$')
plt.xlabel('Zeit $t$')
plt.ylabel('$h(t)$')
plt.grid(True)
plt.legend()
plt.show()
