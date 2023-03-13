# -*- coding: utf-8 -*-
"""
=====================
Peluruhan Radioaktif
Solusi Eksak
By B_ 31.01.2023
=====================
"""

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['figure.dpi'] = 300
# plt.rc('font', size=10) #controls default text size
plt.rc('axes', titlesize=18) #fontsize of the title
plt.rc('axes', labelsize=18) #fontsize of the x and y labels
plt.rc('xtick', labelsize=16) #fontsize of the x tick labels
plt.rc('ytick', labelsize=16) #fontsize of the y tick labels
# plt.rc('legend', fontsize=10) #fontsize of the legend
# plt.rcParams.update(plt.rcParamsDefault)
# %matplotlib inline

# Initialize Variable
tmin = 0
tmax = 5
tau = 0.5
Ngrid = 200
t = np.linspace(tmin,tmax,Ngrid)
NU0 = 100

# Calculate Uranium Decay
NU = NU0*np.exp(-t/tau)


# Plot
plt.plot(t,NU,'-',linewidth=3.0)
plt.xlabel('$t (s)$')
plt.ylabel('$N_U(t)$')
# plt.xlabel('$t (s)$',fontsize=28)
# plt.ylabel('$N_U(t)$',fontsize=28)
plt.show()
