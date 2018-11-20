# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def rot(x,y,th):
    newx=np.cos(th)*x-np.sin(th)*y
    newy=np.sin(th)*x+np.cos(th)*y
    return newx,newy

#normalized cycloid
t=np.linspace(0,np.pi,1000)
x=(t-np.sin(t))
y=(1-np.cos(t))
x=x/np.max(x)
y=y/np.max(y)
x,y=rot(x,y,np.pi/2)

#linear
xl=np.linspace(0,1,1000)
yl=xl
xl,yl=rot(xl,yl,np.pi/2)

#circle
t=np.linspace(0,np.pi/2,1000)
xc=np.cos(t)
yc=np.sin(t)
xc,yc=rot(xc,yc,np.pi)
yc=yc+1

#parabola
x2=np.linspace(-1,0,1000)
y2=x2**12

linestyle='-'
linewidth=3

fig,ax=plt.subplots(1,figsize=(16,16))
ax.plot(x,y,color="red",linewidth=linewidth)
ax.plot(xl,yl,color="black",linewidth=linewidth)
#ax.plot(xc,yc)
ax.plot(x2,y2,linewidth=linewidth)

fig.savefig("Brachistochrone", dpi=300)

plt.show()