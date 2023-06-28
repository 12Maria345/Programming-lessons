import numpy as np
import matplotlib.pyplot as plt
delt = 0.001
l = 0.01
xx = 0.5
e = 0.001


def func(x):
    return 31.75*pow(x, 3)-15.25*x+2

def Svenn(x) :
    h= delt
    x0 = x
    if(func(x)<=func(x-h) and func(x)<=func(x+h)):
        a0 = x0-h
        b0 = x0+h
    else :
        if(func(x0)<=func(x0-h) and func(x0)>=func(x0+h)):
            a0 = x0
            x1 = x0+h
        else:
            b0 = x0
            h = - h
            x1 = x0+h
        i = 1
        while(func(x0)>func(x1)):
            if(func(x1)<func(x0) and h == delt):
                a0 = x0
            if(func(x1)<func(x0) and h == -1*delt):
                b0 = x0
            x0 = x1
            x1 = x0+h*(2**i)
        if(func(x1)>func(x0) and h == delt):
                b0 = x1
        if(func(x1)>func(x0) and h == -1*delt):
                a0 = x1
    return (a0, b0)
print (Svenn(xx))
a0, b0 = Svenn(xx)

def Dikhotomia (a0, b0, ep, l0):
    a = a0
    b = b0
    while(b-a>l0):
        y = (a+b-ep)/2
        z = (a+b+ep)/2
        if(func(y)<func(z)):
            b = z
        else:
            a = y
    return ((b+a)/2, func((b+a)/2))
x_min, y_min = Dikhotomia(a0, b0, e, l)
print (x_min, y_min)

x = np.arange(-1, 1, 0.001)
y = func(x)
ax = plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.plot(x, y)
plt.plot([x_min],[y_min],'ro')
plt.text( x_min, -3.5, 'min',fontsize=12);
plt.show()