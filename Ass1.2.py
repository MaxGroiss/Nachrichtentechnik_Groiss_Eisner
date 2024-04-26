import matplotlib.pyplot as plt
import numpy as np

# Settings

db_list = [-10,-20,-30,-40,-50,-60,-70]
p_r = 2*pow(10, -12)
n_0 = 4.047*pow(10, -21)
B_1 = 2.46*pow(10, 6)

plt.rc('font', family='serif')

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": "Helvetica",
})

def get_p_values(db_list, p_r):
    p_list = []
    for i in db_list:
        p_list.append(pow(10, i/10)*p_r)
    return p_list


def get_C_values(B, n_0, p_list):
    c_days = []
    for i in p_list:
        c_days.append(B*np.log2(1+(i)/(n_0*B)))
    return np.array(c_days)







x = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


plt.plot(x, get_C_values(B_1, n_0 , get_p_values(db_list, p_r)), 'b-', label=r'TEst')
plt.title(r'Maximale Übertragungsrate')
plt.ylabel(r'$C$ in bit/s')
plt.xlabel(r'Days')
plt.legend(fontsize=8)
plt.grid()
plt.show()
