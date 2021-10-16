import os, sys, imageio
import numpy as np
from numpy import cos,sin,tan,exp,pi,floor,ceil,mod
from numpy import power as pow, minimum as min, maximum as max
from funcs import *

i = 1j
funstr = ">\"F*.U/'N-_:_-G'\I.*F\"<"

cwd = os.getcwd()
direc = cwd+'\\fungifs\\'

if not(os.path.isdir('fungifs')):
    os.system("mkdir fungifs")

if not(os.path.exists('fungifs\\fungif_settings.txt')):
    settings_file = open(direc+'fungif_settings.txt',"w")
    settings_file.write("""filename = 'fungif'
h = 540
w = 540
fps = 24.0
numbeats = 4.0
bpm = 60.0
scale = 1.0""")
    settings_file.close()

while(True):

    os.system("cls")
    print()
    print(funstr)
    print()
    func = input("(r,g,b)(z,t) = ")
    print()

    settings_file = open(direc+'fungif_settings.txt',"r")
    settings = settings_file.read()
    exec(settings)
    settings_file.close()

    if p != "":
        if os.path.exists(p):
            inpt = Image.open(p)
            iw, ih = inpt.size
            p = asarray(inpt)
            inpt.close()

    numframes = int(numbeats*fps*60/bpm)
    dt = numframes/30
    dz = 2*scale/min(h,w)
    yy = np.arange(-(h/2)*dz,(h/2)*dz,dz)
    xx = np.arange(-(w/2)*dz,(w/2)*dz,dz)
    x, y = np.meshgrid(xx,yy)
    z = x + 1j * y

    if func == '':
        sys.exit()
    if func == '?':
        os.startfile(direc + "fungif_settings.txt")
        continue

    initname = filename
    initlen = len(initname)

    while os.path.exists(direc+filename+'.gif'):
        if filename == initname:
            filename = initname+'1'
            continue
        else:
            filename = str(filename[0:initlen])+str(int(filename[initlen:len(filename)+1])+1)

    with imageio.get_writer(direc+filename+'.gif', mode='I',fps = fps) as writer:
        for k in range(numframes):
            t = k/numframes
            print(funstr[0:int(t*len(funstr))+1],end='\r')
            exec("F ="+func)
            data = np.dstack(F)*255
            image = data.astype(np.uint8)
            writer.append_data(image)

    descrip = open(direc+filename+'.txt',"w")
    descrip.write(filename+" = "+func+"\n\n")
    descrip.write(settings)
    descrip.close()

    print()
    print()

    os.system(direc+filename+'.gif')
