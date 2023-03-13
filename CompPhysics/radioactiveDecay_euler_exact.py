"""
=====================
Peluruhan Radioaktif
By B_ 31.01.2023
=====================
"""

import matplotlib.pyplot as plt
import numpy as np

# Initialize Variable
tmin = 0
tmax = 5
tau = 0.5

# Calculate Decay Exact
Nexact = 200
te = np.linspace(tmin,tmax,Nexact)
NU0 = 100
NUe = NU0*np.exp(-te/tau)

# Calculate Decay Numeric
# Ngrid = 20
# dt = (tmax-tmin)/Ngrid
dt = 0.1
Ngrid = np.int8((tmax-tmin)/dt)
t = np.zeros(Ngrid)

NU = np.zeros(Ngrid)
NU[0] = NU0
for ii in range(0,Ngrid-1):
    NU[ii+1] = NU[ii] - (NU[ii]/tau)*dt
    t[ii+1] = t[ii] + dt

# Plot
plt.plot(te,NUe,'-',linewidth=3.0)
plt.plot(t,NU,'o')
plt.xlabel('$t (s)$')
plt.ylabel('$N_U(t)$')
# plt.xlabel('$t (s)$',fontsize=28)
# plt.ylabel('$N_U(t)$',fontsize=28)
plt.show()
