import matplotlib.pyplot as plt
import numpy
import numpy as np
from icecream import ic
# Settings
import scipy.interpolate as sp

def dirac_delta(t_in):
    pulse_out = []
    for t in t_in:
        if -0.001 < t < 0.001:
            pulse_out.append(1)
        else:
            pulse_out.append(0)
    return np.array(pulse_out)


def rect_funct(f_in,junktion):
    pulse_out = []
    for f in f_in:
        if np.abs(f) <= junktion:
            pulse_out.append(1)
        else:
            pulse_out.append(0)
    return np.array(pulse_out)


def sinc_function(t_in, t_period_in):
    f_out = []
    for t in t_in:
        if t != 0:
            x = np.sin(np.pi * 1/t_period_in * t)/(np.pi * 1/t_period_in * t)
            f_out.append(x)
        else:
            f_out.append(1)
    return np.array(f_out)


plt.rc('font', family='serif')

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": "Helvetica",
})

# Plot 321

# time = np.arange(-10,11,0.01)
# print(dirac_delta(time))
# print(time)
# plt.plot(time, dirac_delta(time), 'b', label=r'$R_n(t)$')
# plt.title(r'Plot der ACF $R_n(t)$')
# plt.ylabel(r'$N_0$ in W/Hz')
# plt.xlabel(r't in seconds')
# plt.xlim(-10, 10)

## Plot 322
#time = [0  ,1  ,2  ,3  ,4  ,5  ,6  ,7  ,8  ,9 ,"..."]
## time = np.arange(0,11,1)
## np.append(time,[[11]])
#
#print(time)
#plt.plot(time, np.linspace(1,1,11), 'b', label=r'$S_n(f)$')
#plt.title(r'Plot der PSD $S_n(t)$')
#plt.ylabel(r'$N_0$ in W/Hz')
#plt.xlabel(r'f in Hz')
#plt.xlim(0, 10)

# # Plot 331
# T = 0.1
# freq = np.arange(-20,20.01,0.01)
#
# plt.plot(freq, rect_funct(freq, 1/(2*T)), 'b', label=r'$S_x(f)$')
# plt.title(r'Plot der PSD $S_x(f)$')
# plt.ylabel(r'$N_0 \cdot T^2$ in [$N_0 \cdot T^2$] $ \rightarrow T = 0.1 $ s')
# plt.xlabel(r'f in Hz')
# plt.xlim(-15, 15)

# Plot 332
T = 0.1
time = np.arange(-10,11,1)
print(time)
print(sinc_function(time,1))
new = sp.BSpline(time , sinc_function(time,1), k=0)
y = [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]
print(len(y))
x = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,-0.01,0,0.01,1,2,3,4,5,6,7,8,9,10]
print(len(x))
plt.step(x, y, 'b', label=r'$R_y(m)$')
plt.title(r'Plot der ACF $R_y(m)$')
plt.ylabel(r'$N_0 \cdot T $ in [$N_0 \cdot T$] $ \rightarrow T = 0.1 $ s')
plt.xlabel(r'm')
plt.xticks(np.arange(-10,11,1))
plt.xlim(-10, 10)





plt.legend(fontsize=8)
plt.grid()
plt.show()
