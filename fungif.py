import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math as m
import os

def cos(x):
    return np.cos(x)
def sin(x):
    return np.sin(x)
def tan(x):
    return np.tan(x)
def exp(x):
    return np.exp(x)
pi = m.pi

filename = input("filename:")
filename += '.'+input("filetype:")
numframes = int(input("# of frames:"))
func = input("f(z,t)=")

numcols, numrows = 540, 540
w, h = 5, 5
fps = 30

fig = plt.figure(figsize=(w, h), dpi=numcols/w)
direc = os.getcwd()


x = np.arange(-w/2,w/2,w/numcols)
y = np.arange(-h/2,h/2,h/numrows)

xx, yy = np.meshgrid(x,y)
z = xx + 1j * yy

ims = []

for i in range(numframes):
    t = i/numframes
    print(i,"of",numframes,end='\r')
    exec("f="+func)
    plt.axis('off')
    fig.tight_layout()
    im = plt.pcolormesh(x,y,np.mod(f,1),animated = True,vmin = 0,vmax = 1,
                        shading = 'auto',cmap = 'hsv')
    ims.append([im])

ani = animation.ArtistAnimation(fig, ims, interval=1000/fps)

ani.save(filename)
os.system(filename)
