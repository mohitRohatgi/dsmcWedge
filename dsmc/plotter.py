# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 18:58:38 2016

@author: mohit
"""
import numpy as np
import matplotlib.pyplot as plt

temperature = np.loadtxt('wedge_super_temperature.txt').view(float)
plt.contourf(temperature)
plt.colorbar()
plt.savefig('temp.png', bbox_inches='tight')
plt.clf()

number_density_0 = np.loadtxt('wedge_super_number_density_0.txt').view(float)

number_density_1 = np.loadtxt('wedge_super_number_density_1.txt').view(float)

number_density = number_density_0 + number_density_1
plt.contourf(number_density)
plt.colorbar()
plt.savefig('num_den.png', bbox_inches='tight')
plt.clf()

mach = np.loadtxt('wedge_super_mach.txt').view(float)
plt.contourf(mach)
plt.colorbar()
plt.savefig('mach.png', bbox_inches='tight')
plt.clf()

pressure = np.loadtxt('wedge_super_pressure.txt').view(float)
plt.contourf(pressure)
plt.colorbar()
plt.savefig('pressure.png', bbox_inches='tight')
plt.clf()
