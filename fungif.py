import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math as m
import os, shutil

def cos(z):
    return np.cos(z)
def sin(z):
    return np.sin(z)
def tan(z):
    return np.tan(z)
def exp(z):
    return np.exp(z)
def arg(z):
    return np.angle(z)/(2*m.pi)
def pow(z,w):
    return np.power(z,w)
def oss(x):
    return np.sin(x*2*m.pi)

pi = m.pi

print()
filename = input("filename: ")
ext = '.'+input("filetype: ")
numframes = int(input("# frames: "))
sidelen = int(input("sidelen : "))
print()
print("f is a real-valued f'n taking cpx input z and time input t 0->1")
print(" cpx valued f'ns: sin cos tan pow exp")
print("real valued f'ns: abs arg .real .imag")
print()
func = input("f(z,t)=")
print()

numcols, numrows = sidelen,sidelen
w,h = 5,5
fps = 30

fig = plt.figure(figsize=(w,h),dpi=1.3*numcols/w,frameon=False)

xx = np.arange(-w/2,w/2,w/numcols)
yy = np.arange(-h/2,h/2,h/numrows)

x, y = np.meshgrid(xx,yy)
z = x + 1j * y

ims = []

for i in range(numframes+1):
    t = i/numframes
    print("Painting frame",i,"of",numframes,end='\r')
    exec("f="+func)

    plt.axis('off')
    im = plt.pcolormesh(xx,yy,np.mod(f,1),animated = True,vmin = 0,vmax = 1,
                        shading = 'auto',cmap = 'twilight')
    ims.append([im])

print()

cwd = os.getcwd()
direc = cwd+'\\FUN_GIFS\\'
if not(os.path.isdir('FUN_GIFS')):
    os.system("mkdir FUN_GIFS")

while os.path.exists(direc+filename+ext):
    filename += 'x'

print("Saving "+filename+"...")

ani = animation.ArtistAnimation(fig, ims, interval=1000/fps)
ani.save(filename+ext)

shutil.move(cwd+"\\"+filename+ext,direc+filename+ext)

descrip = open(direc+filename+'.txt',"w")
descrip.write(filename+"(z,t)="+func)
descrip.close()

os.system(direc+filename+ext)
print()
