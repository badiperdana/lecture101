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
