# -*- coding: utf-8 -*-
"""
Created on Sun May  7 19:08:45 2017

@author: Ray Justin O. Huang
"""
import numpy as np
import matplotlib.pyplot as plt

# Simulating standard Brownian motion
def brownian_motion(sigma, n, dt, startval, runs):
    B_si = startval
    storedvals = np.empty((runs+1,int(n/dt)))
    storedvals[0,0] = 0
    storedvals[:,0] = B_si
    brownianplot = plt.figure()
    brownianplotaxes = brownianplot.add_axes([0,0,1,1])
    brownianplotaxes.set_xlabel('Time')
    brownianplotaxes.set_ylabel('Value')
    for r in range(runs):
        B_si = startval
        for i in range(0,int(n/dt),int(dt/dt)):
            B_si = B_si + np.sqrt(sigma)*np.random.normal()
            if r == 0:
                storedvals[0,i] = i*dt
            storedvals[r+1,i] = B_si
        brownianplotaxes.plot(storedvals[0],storedvals[r+1])
            # print("Observation ",i+1,": ",B_si)
    return storedvals, brownianplot

sample = brownian_motion(1,365,0.001,0,10)