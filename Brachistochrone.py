
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

#fig,axs=plt.subplots(2,2,figsize=(11*1.8,8.5*1.8))

#for ax in axs:
# ax.plot
#ax.plot(x+1,y,color="red",linewidth=linewidth)
#ax.plot(xl+1,yl,color="black",linewidth=linewidth)
#ax.plot(x2+1,y2,linewidth=linewidth)
# =============================================================================
# limir=[[0.5,1],[0,0.5]]
# limic=[[0,0.5],[0.5,1]]
# for n,row in enumerate(axs):
#     for m,col in enumerate(row):
#         col.plot(x+1,y,color="red",linewidth=linewidth)
#         col.plot(xl+1,yl,color="black",linewidth=linewidth)
#         col.plot(x2+1,y2,color="blue",linewidth=linewidth)
#         col.set_ylim(limir[n])
#         col.set_xlim(limic[m])
# 
# =============================================================================
limir=[[0.5,1],[0,0.5]]
limic=[[0,0.5],[0.5,1]]
for n in range(2):
    for m in range(2):
        fig,ax=plt.subplots(1,figsize=[11,8.5])
        
        ax.plot(x+1,y,color="red",linewidth=linewidth)
        ax.plot(xl+1,yl,color="black",linewidth=linewidth)
        ax.plot(x2+1,y2,color="blue",linewidth=linewidth)
        ax.set_ylim(limir[n])
        ax.set_xlim(limic[m])
        ax.grid()
        ax.axis('off')
        fig.tight_layout(pad=-0)
        fig.savefig("Brachistochrone"+str(n)+str(m))








fig.savefig("Brachistochrone", dpi=300)
ax.grid()
plt.show()