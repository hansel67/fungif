from numpy import sin,exp,angle,floor,ceil,mod,zeros,asarray,ones,conj,sqrt
from numpy import power as pow, minimum as min, maximum as max
from math import pi
from math import pow as mpow
import os
from PIL import Image

defiter = 7

#math utility functions

def tri(x): #triangle wave with amplitude 1/4 centered at y=1/2 and tri(0)=0
    return 0.5-abs(x-floor(x)-0.5)

def digit(x,i,b): #the digit in the (b^i)s place of x
    return floor(x*pow(b,float(-i)))-b*floor(x*pow(b,float(-i-1)))

def bump(x,p=1.0): #a bump function centered at
    x = mod(x,0.9999)+0.00001
    return exp((1/(x*(x-1))+4)*p)

def dot(z): #circ(z)=1 if |z|<1 and 0 if |z|>=1
    return 1-min(floor(abs(z)),1)

#functions meant for the user

def arg(z):
    return angle(z)/(2*pi)

def re(z):
    return z.real

def im(z):
    return z.imag

def spiral(z):
    return arg(z)+abs(z)

def mandel(c,iter = defiter):
    z = zeros(c.shape)
    for i in range(iter):
        z = pow(z,2)+c
    return abs(z)

#fractal functions, all increasing

def cant(x,iter=defiter): #cantor f'n, monotonic
    y = floor(x)
    active = ones(x.shape)
    for i in range(iter):
        d = digit(x,-i,3)
        y += (1-mod(mod(d+1,3),2))*active/pow(2,i) #(0,1,2)->(0,1,1)
        active *= (1-mod(d,2)) #(0,1,2)->(1,0,1)
    return y

def mink(x,iter=defiter): #minkowski's ? f'n, monotonic
    y = zeros(x.shape)
    N = x
    active = D = ones(x.shape)
    ps_a = zeros(x.shape)
    UPR_BD = 10000
    for i in range(iter):
        Dtemp = D
        D = mod(N,D)
        N = Dtemp
        active *= 1-dot(D*UPR_BD)
        ps_a += active*floor(N/D)
        y += active*2*pow(-1,i)/pow(2,ps_a)
    return y

def blanc(X,iter=defiter): #takagi-landsberbg f'n
    w = 0.5
    Y = zeros(X.shape)
    for i in range(1,iter):
        Y += tri(X*pow(2.0,i))*pow(w,i)
    return Y

def wei(X,iter=defiter): #weierstrauss f'n
    a = 0.5
    b = 2.0
    Y = zeros(X.shape)
    for i in range(1,iter):
        Y += sin(2*pi*X*pow(b,i))*pow(a,i)
    return Y

def mob(z,P,s,Q,r):
    return r*s/(z-P)+Q

def schott(z,c1,r1,c2,r2,c3,r3,c4,r4):
    a = 1-dot(mob(z,0,1,c1,r1))
    a *= 1-dot(mob(z,0,1,c2,r2))
    a *= 1-dot(mob(z,0,1,c3,r3))
    a *= 1-dot(mob(z,0,1,c4,r4))
    return a

#color functions

def chk(z):
    A = mod(floor(2*z.real)+floor(2*z.imag),2.0)
    return (A,A,A)

def stripe(z):
    A = mod(floor(2*z.real),2.0)
    return (A,A,A)

def trip(A):
    return (A,A,A)

def prism(x,p = 1.0):
    x = mod(x,1.0)
    r = 1-bump(x,p)
    g = 1-bump(x+2/3,p)
    b = 1-bump(x+1/3,p)
    return (r,g,b)

def grey(x,p = 1.0):
    A = 2*tri(x)
    return (A,A,A)

def gray(x):
    return grey(x)

def tile(z,p):
    ih, iw, c = p.shape
    dp = 1/max(iw,ih)
    iw -= 1
    ih -= 1
    r = asarray([[p[int(mod(x.imag,ih*dp)/dp),int(mod(x.real,iw*dp)/dp),0] for x in y] for y in z])/255
    g = asarray([[p[int(mod(x.imag,ih*dp)/dp),int(mod(x.real,iw*dp)/dp),1] for x in y] for y in z])/255
    b = asarray([[p[int(mod(x.imag,ih*dp)/dp),int(mod(x.real,iw*dp)/dp),2] for x in y] for y in z])/255
    return (r,g,b)
