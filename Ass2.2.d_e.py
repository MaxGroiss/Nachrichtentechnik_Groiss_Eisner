import matplotlib.pyplot as plt
import numpy
import numpy as np
from icecream import ic
# Settings
import scipy.interpolate as sp

T = 1
N_0 = 1
A = 1

const = 4*np.sqrt(A)*T/N_0
beta = np.linspace(0.1,3,1000000)
print("Done")

def func(beta_in):
    func_out = []
    pre_step = 0
    save_step = 0
    save_b = 0
    for b in beta_in:
        step = np.divide((-(np.exp(-b)-1)), b*np.sqrt(np.divide(1, b)))
        func_out.append(step)
        if step > pre_step:
            save_step = pre_step
            save_b = b
        pre_step = step
    print(f"Max Function = {save_step} Max b = {save_b}")

    return np.array(func_out),save_b,save_step



plt.rc('font', family='serif')

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": "Helvetica",
})

tuple_in = func(beta)
snr = tuple_in[0]
b_max = tuple_in[1]
func_max = tuple_in[2]
plt.plot(beta, snr, 'r-', label=r'$Var Teil SNR$')

plt.title(r'Plot des variablen Teils der SNR Optimierung')
plt.ylabel(r'Variabler Faktor SNR')
plt.xlabel(r'$\beta$')
plt.axhline(func_max)
plt.axvline(b_max)
plt.legend(fontsize=8)
plt.grid()
plt.show()
