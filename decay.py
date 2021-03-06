from math import sin
from numpy import arange,log,exp
import matplotlib.pyplot as plt

rate=log(2.)/5730.

def f(x,t):
    return -rate*x

a = 0.0
b = 4000000.0
N = 50
h = (b-a)/N

tpoints = arange(a,b,h)
xpoints = []
x = 1.


for t in tpoints:
    xpoints.append(x)
    k1 = h*f(x,t)
    k2 = h*f(x+0.5*k1,t+0.5*h)
    k3 = h*f(x+0.5*k2,t+0.5*h)
    k4 = h*f(x+k3,t+h)
    x += (k1+2*k2+2*k3+k4)/6

plt.plot(tpoints,xpoints,'m')
plt.plot(tpoints,exp(-rate*tpoints),'b*')
plt.xlabel('years')
plt.ylabel('Fractional remaining populations')

plt.ion()
plt.show()
