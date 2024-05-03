import matplotlib.pyplot as plt
import numpy
import numpy as np
from icecream import ic
# Settings


plt.rc('font', family='serif')

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": "Helvetica",
})


def amplitude(t_periode):
    eps_b = 1  # Symbol Energie
    x = 2*eps_b/t_periode
    return np.sqrt(x)


def u1_t(t, t_period):
    u_1 = []
    for i in t:
        if i < 0:
            u_1.append(0)
        elif i <= t_period:
            u_1.append(amplitude(t_period)*np.sin((2*np.pi*i)/t_period))
        else:
            u_1.append(0)
    return np.array(u_1)


def u2_t(t, t_period, t_zero):
    u_2 = []
    for i in t:
        if i < t_zero:
            u_2.append(0)
        elif i <= t_period + t_zero:
            u_2.append(amplitude(t_period) * np.sin((2 * np.pi * (i-t_zero)) / t_period))
        else:
            u_2.append(0)
    return np.array(u_2)


def winkel_u1_u2(t_zero_array, t_period):
    winkel = []
    for i in t_zero_array:
        x = np.divide(2*i*np.pi, t_period)
        winkel.append(np.arccos(np.sin(x)/(2*np.pi)+np.cos(x)-i/t_period*np.cos(x)))
    return np.array(winkel)


time_start = -5
time_stop = 25
time_steps = 150
t_per = 10
time_span = np.linspace(time_start, time_stop, time_steps)
t_0_array = np.linspace(0, t_per, 100)
# t_0 = 5

# u1 = u1_t(time_span, t_per)
# u2 = u2_t(time_span, t_per, t_0)
phie = winkel_u1_u2(t_0_array, t_per)


# # Plot a
# plt.plot(time_span, u1, 'r-', label=r'$u_1(t)$')
# plt.plot(time_span, u2, 'b--', label=r'$u_2(t)$')
# plt.title(r'Signalformen')
# plt.ylabel(r'$u_1(t)$ und $u_2(t)$ in [sqrt($E_b / T$)]')
# plt.xlabel(r't in seconds')
# plt.xlim(time_start, time_stop)
# plt.ylim(numpy.amax(u1) + 0.1, numpy.amin(u1) - 0.1)


# Plot d
# plt.plot(t_0_array, phie, 'r-', label=r'$\varphi(T_0)$')
# plt.xlim(0, t_per)
# plt.ylim(0, numpy.amax(phie) + 0.2)
# plt.title(r'Winkel zwischen $u_1(t)$ und $u_2(t)$')
# plt.ylabel(r'$\varphi(T_0)$ in rad')
# plt.xlabel(r'$T_0$ in seconds')
# plt.axhline(y=np.pi/2, color='y', linestyle='--', label="90 degrees")


# # Plot h1
# t_0 = 5
# u1 = u1_t(time_span, t_per)
# u2 = u2_t(time_span, t_per, t_0)
# plt.plot(time_span, u1, 'r-', label=r'$u_1(t)$')
# plt.plot(time_span, u2, 'b--', label=r'$u_2(t)$')
# plt.title(r'Plot der Signale mit maximaler Distanz zueinander')
# plt.ylabel(r'$u_1(t)$ und $u_2(t)$ in [sqrt($E_b / T$)]')
# plt.xlabel(r't in seconds')
# plt.xlim(time_start, time_stop)
# plt.ylim(numpy.amax(u1) + 0.1, numpy.amin(u1) - 0.1)

#  Plot h21
# t_0 = 2.849
# u1 = u1_t(time_span, t_per)
# u2 = u2_t(time_span, t_per, t_0)
# plt.plot(time_span, u1, 'r-', label=r'$u_1(t)$')
# plt.plot(time_span, u2, 'b--', label=r'$u_2(t)$')
# plt.title(r'Plot der orthogonalen Signale $T_0 = 0.2849T$')
# plt.ylabel(r'$u_1(t)$ und $u_2(t)$ in [sqrt($E_b / T$)]')
# plt.xlabel(r't in seconds')
# plt.xlim(time_start, time_stop)
# plt.ylim(numpy.amax(u1) + 0.1, numpy.amin(u1) - 0.1)

# Plot h22
t_0 = 10
u1 = u1_t(time_span, t_per)
u2 = u2_t(time_span, t_per, t_0)
plt.plot(time_span, u1, 'r-', label=r'$u_1(t)$')
plt.plot(time_span, u2, 'b--', label=r'$u_2(t)$')
plt.title(r'Plot der orthogonalen Signale $T_0 = T$')
plt.ylabel(r'$u_1(t)$ und $u_2(t)$ in [sqrt($E_b / T$)]')
plt.xlabel(r't in seconds')
plt.xlim(time_start, time_stop)
plt.ylim(numpy.amax(u1) + 0.1, numpy.amin(u1) - 0.1)

plt.legend(fontsize=8)
plt.grid()
plt.show()
