import matplotlib.pyplot as plt
import numpy as np

# Settings

db_list = [-10,-20,-30,-40,-50,-60,-70]
p_r = 2*pow(10, -12)
n_0 = 4.047*pow(10, -21)
B_1 = 2.46*pow(10, 6)
B_2 = 120*pow(10, 3)
plt.rc('font', family='serif')

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": "Helvetica",
})


def calculate_ebdn0(mode, b, p_r, n_0, db_list):
    c_list = []
    eb_list = []
    power_list = []
    eb_n0_list = []
    w_eff_list = []
    for i in db_list:
        power_list.append(np.power(10, (i / 10)) * p_r)

    if mode:
        for i in power_list:
            c_list.append(b*np.log2(1 + np.divide(i, n_0*b)))
        for i in range(len(c_list)):
            eb_list.append(np.divide(power_list[i], c_list[i]))
        for i in eb_list:
            eb_n0_list.append(10*np.log10(np.divide(i, n_0)))
        for i in c_list:
            w_eff_list.append(np.divide(i, b))
    else:
        for i in power_list:
            c_list.append(b * np.log2(1 + np.divide(i, n_0 * b)))
        for i in range(len(c_list)):
            eb_list.append(np.divide(p_r, c_list[i]))
        for i in eb_list:
            eb_n0_list.append(10 * np.log10(np.divide(i, n_0)))
        for i in c_list:
            w_eff_list.append(np.divide(i, b))
    return np.array(eb_n0_list), np.array(w_eff_list)


x = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


# plt.plot(x, get_C_values(B_1, n_0 , get_p_values(db_list, p_r)), 'b-', label=r'Transfer')
plt.plot(x, calculate_ebdn0(True, B_1, p_r, n_0, db_list)[0], 'r-', label=r'$E_b/N_0$ in dB (S-band)')
plt.plot(x, calculate_ebdn0(True, B_1, p_r, n_0, db_list)[1], 'b-', label=r'$W_eff$ in bits/s/Hz (S-band)')
plt.plot(x, calculate_ebdn0(True, B_2, p_r, n_0, db_list)[0], 'y-', label=r'$E_b/N_0$ in dB (VHF)')
plt.plot(x, calculate_ebdn0(True, B_2, p_r, n_0, db_list)[1], 'g-', label=r'$W_eff$ in bits/s/Hz (VHF)')
plt.title(r'Transferverhalten über die Wochentage')
plt.ylabel(r'$C$ in bit/s')
plt.xlabel(r'Days')
plt.legend(fontsize=8)
plt.grid()
plt.show()
