import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math as m

numframes = 100
numcols, numrows = 540, 540
w, h = 5, 5
numframes = 200
fps = 30
filename = 'rainbowsin.mp4'

fig = plt.figure()

x = np.arange(-w/2,w/2,w/numcols)
y = np.arange(-h/2,h/2,h/numrows)

xx, yy = np.meshgrid(x,y)
z = xx + 1j * yy

ims = []

for i in range(numframes):
    t = i/numframes
    print(i,"of",numframes,end='\r')
    f = z.real + np.sin(2*np.pi*(z.imag+t))
    plt.axis('scaled')
    im = plt.pcolormesh(x,y,np.mod(f,1),animated = True,vmin = 0,vmax = 1,
                        shading = 'auto',cmap = 'hsv')
    ims.append([im])

ani = animation.ArtistAnimation(fig, ims, interval=1000/fps)

ani.save(filename)
plt.show()
