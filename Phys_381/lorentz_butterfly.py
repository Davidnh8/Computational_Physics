# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 12:03:24 2016

@author: bjackel
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import scipy.integrate
import numpy.random
import time

def dfunc(state ,t0, sigma=10.0, beta=8/3.0, rho=58.0):
    x, y, z = state
    return np.array([ sigma*(y-x), x*(rho-z)-y, x*y-beta*z])
    
#pdflush, pdfile = pdfig_init('-lorentz')
    
result = scipy.integrate.odeint( dfunc, [1.0, 1.0, 1.0], np.linspace(0.0, 20.0, 9999) )
result = result.T
    
    
fig, axes = plt.subplots(3, sharex=True)
for indx in [0,1,2]:
    axes[indx].plot( result[indx,:], lw=3 )
    axes[indx].set_ylabel(str(indx))
axes[0].set_title('Lorentz equations') 
axes[-1].set_xlabel('integration timestep')


fig, axes = plt.subplots(1, subplot_kw=dict(projection='3d'))
pline = axes.plot( result[0,:], result[1,:], result[2,:], 'g-' )
psym = axes.plot( [result[0,-1]], [result[1,-1]], [result[2,-1]], 'go')
plt.title('Lorentz equations') #$: $\\sigma=10$, $\\beta=8/3$, $\\rho=58$')
plt.show()

plt.ion()
for i in range(0, result.shape[1], 5):
    psym[0].set_data( result[0,i], result[1,i]) #, result[2,0:i])
    psym[0].set_3d_properties(result[2, i])
    plt.draw() #fig.canvas.renderer)
    time.sleep(0.01)# ; print(i)
    
    
def lyapunov(trajectory, origin):
    result = trajectory
    dx = result[:,origin:origin+1000].T - result[:,origin]
    dx = np.sqrt( np.sum(dx**2, axis=1) )
    return dx    
    
plt.clf()
for origin in range(5000, 8000, 750):
    plt.plot( lyapunov(result, origin) )
    
t = np.linspace(0.0, 12.0, 1500)    
r0 = result[:,5000]    
plt.clf()
ensemble = [  scipy.integrate.odeint( dfunc, r0 , t ) ]
for i in range(99):
    r1 = r0 + numpy.random.randn(3) * 1e-6 #; print(r1)
    ensemble.append( scipy.integrate.odeint( dfunc, r1 , t ) )
    
        
fig, axes = plt.subplots(1, subplot_kw=dict(projection='3d'))
for xyz in ensemble:
    pline = axes.plot( xyz[:300,0], xyz[:300,1], xyz[:300,2], 'g-' )
    pline = axes.plot( xyz[300:600,0], xyz[300:600,1], xyz[300:600,2], 'b-' )   
    pline = axes.plot( xyz[600:900,0], xyz[600:900,1], xyz[600:900,2], 'y-' )
      
        
fig, axes = plt.subplots(1, subplot_kw=dict(projection='3d'))
for xyz in ensemble:
    pline = axes.plot( xyz[600:900,0], xyz[600:900,1], xyz[600:900,2], 'y-' )
    pline = axes.plot( xyz[900:1200,0], xyz[900:1200,1], xyz[900:1200,2], 'r-' )
    pline = axes.plot( xyz[1200:,0], xyz[1200:,1], xyz[1200:,2], 'm-' )

plt.clf()    
xyz0 = ensemble[0]    
for xyz in ensemble:
    dxyz = xyz - xyz0
    plt.plot( np.sqrt( np.sum(dxyz**2, axis=1) ) )
    
plt.yscale('log')    