# -*- coding: utf-8 -*-
"""
Created on Mon May  8 11:50:06 2017

@author: Ray Justin O. Huang
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

L = 1500
alpha = 0.25
sigma = 0.75
m = 0.24
mu = 0.06
w = 10000
H = 9000
F = 5000

varpack = [L, alpha, sigma, m, mu, w, H, F]

n = 365
dt = 0.001
Sigma = 1

# Stochastic bee model
def stochastic_bee(Sigma, n, dt, varpack):
    L, alpha, sigma, m, mu, w, H, F = varpack
    storedvals = np.empty((3,int(n/dt)))
    
    for i in range(0,int(n/dt),int(dt/dt)):
        H_old = H
        H = H + ((L*(H+F))/(w+H+F) - H*(alpha - sigma*(F/(H+F))) - mu*H)*dt + \
            np.sqrt(Sigma)*np.random.normal()
        F = F + (H_old*(alpha - sigma*(F/(H_old+F))) - m*F)*dt + \
            np.sqrt(Sigma)*np.random.normal()
        storedvals[0,i] = i*dt
        storedvals[1,i] = H
        storedvals[2,i] = F
    
    return storedvals

run1 = stochastic_bee(Sigma, n, dt, varpack)

beedata = pd.DataFrame(run1.T[:,1:], index=run1[0], columns=['Hive Bees','Forager Bees'])

plt.plot(run1[0, :], run1[1, :])
plt.ylabel('Hive Bees')
plt.xlabel('Days')

run2 = stochastic_bee(1, 365, 0.001, varpack)

plt.plot(run2[0], run2[1])
plt.ylabel('Hive Bees')
plt.xlabel('Days')
plt.plot(run2[0], run2[2])
plt.ylabel('Forager Bees')
plt.xlabel('Days')

stochasticbee1 = plt.figure()
stochasticbee1axes = stochasticbee1.add_axes([0,0,1,1])
stochasticbee1axes.plot(run2[0],run2[1], label='Hive Bees')
stochasticbee1axes.plot(run2[0],run2[2], label='Forager Bees')
stochasticbee1axes.legend()
stochasticbee1axes.set_xlabel('Days')
stochasticbee1axes.set_ylabel('Number of Bees')
stochasticbee1axes.set_title('Bee Population Fluctuation with Standard Brownian Motion')