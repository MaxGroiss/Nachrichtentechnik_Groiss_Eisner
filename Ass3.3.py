import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Task E:
# Define the parameters
N0 = 1  # Power spectral density
sigma = np.sqrt(N0 / 2)  # Standard deviation

# Define the range for r
r = np.linspace(-4 * sigma, 4 * sigma, 1000)

# Define the pdf of r given the signal is absent
pdf_r_absent = (1 / np.sqrt(np.pi * N0)) * np.exp(-r**2 / N0)

# Plot the pdf
plt.figure(figsize=(10, 6))
plt.plot(r, pdf_r_absent, label='$f_r(r|\mathrm{absent})$', color='blue')
plt.title('Wahrscheinlichkeitsdichtefunktion $f_r(r|\mathrm{absent})$')
plt.xlabel('Empfängerausgang $r$')
plt.ylabel('Dichtefunktion $f_r(r|\mathrm{absent})$')
plt.legend()
plt.grid(True)
plt.show()

# Task F:
# Define the mean and standard deviation of the Gaussian noise
mean_signal = 1  # Assuming A = 1
std_dev = np.sqrt(0.5)  # Assuming N0 = 1

# Generate a range of values for r
r = np.linspace(-3*std_dev, 5*std_dev, 1000)

# Calculate the pdf of r
pdf_signal = norm.pdf(r, mean_signal, std_dev)

# Plot the pdf
plt.figure(figsize=(10, 6))
plt.plot(r, pdf_signal, label='$f_r(r|\mathrm{present})$', color='green')
plt.title('Wahrscheinlichkeitsdichtefunktion $f_r(r|\mathrm{present})$')
plt.xlabel('Empfängerausgang $r$')
plt.ylabel('Dichtefunktion $f_r(r|\mathrm{present})$')
plt.legend()
plt.grid(True)
plt.show()


