import os, imageio
import numpy as np
from numpy import cos,sin,tan,exp,pi

def arg(z):
    return np.angle(z)/(2*m.pi)
def pow(z,w):
    return np.power(z,w)
def re(z):
    return z.real
def im(z):
    return z.imag
def min(a,b):
    return np.minimum(a,b)
def max(a,b):
    return np.maximum(a,b)
def bump(x,p):
    x = np.mod(x,0.99)+0.0001
    return np.exp((1/(x*(x-1))+4)*p)

i = 1j
myfps = 24
scale = 2
h = w = 540
numbeats = 4
bpm = 60
filename = 'fungif'
funstr =">\"F*.U/'N-_:_-G'\I.*F\"<"
numframes = int(numbeats*myfps*60/bpm)
dt = numframes/30

os.system("cls")
print()
print(funstr)
print()
func =  input("f(z,t) = ")
print()

dz = scale*2/min(h,w)
yy = np.arange(-scale,scale,dz)
xx = np.arange(-scale,scale,dz)
x, y = np.meshgrid(xx,yy)
f = z = x + 1j * y

cwd = os.getcwd()
direc = cwd+'\\fungifs\\'
if not(os.path.isdir('fungifs')):
    os.system("mkdir fungifs")

while os.path.exists(direc+filename+'.gif'):
    if filename == 'fungif':
        filename = 'fungif1'
        continue
    else:
        filename = filename[0:6]+str(int(filename[6:len(filename)+1])+1)

with imageio.get_writer(direc+filename+'.gif', mode='I',fps = myfps) as writer:
    for k in range(numframes):
        t = k/numframes
        print(funstr[0:int(t*len(funstr))+1],end='\r')
        exec("f ="+func)
        if is_all_zero = np.all((arr == 0))
        r = 1-bump(f,1.3)
        g = 1-bump(f+2/3,1.3)
        b = 1-bump(f+1/3,1.3)
        data = np.dstack((r,g,b))*255
        image = data.astype(np.uint8)
        writer.append_data(image)

descrip = open(direc+filename+'.txt',"w")
descrip.write(filename+"="+func)
descrip.close()

print()
print()

os.system(direc+filename+'.gif')
