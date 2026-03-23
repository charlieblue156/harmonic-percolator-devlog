# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 14:30:29 2026

@author: charl
"""
import numpy as np
import matplotlib.pyplot as plt

I_C=-65.49e-6
V_T=26e-3
R_C=30e3
beta=50
R_S=1e4

R_f=np.linspace(1e2, 5e5, num=1000)

g_m=I_C/V_T
r_pi=beta/g_m
A=g_m * (1/R_f+1/R_C)**(-1) * (1/R_S+1/R_f+1/r_pi)**(-1)
B=-1/R_f
R_o=(1/R_f+1/R_C)**(-1)
R_i=(1/R_S+1/R_f+1/r_pi)**(-1)


R_of=R_o/(1+A*B)
R_in=R_i/(1+A*B)


plt.plot(np.log10(R_f), R_of, label='$R_{of}$', markersize=4, color="darkblue")
plt.plot(np.log10(R_f), R_in, label='$R_{if}$', markersize=4, color="red")
plt.xlabel('log10 Feedback Resistor Resistance', fontsize=16)
plt.ylabel('Amplifier Resistance / $\Omega$', fontsize=16)
plt.legend(fontsize=16)
plt.grid(True)
plt.tight_layout()
plt.show()