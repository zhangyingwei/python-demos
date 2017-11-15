# encoding-utf-8

import matplotlib.pyplot as plt
import math

import numpy
from mpl_toolkits.mplot3d import Axes3D

def sayHello():
    print("hello python 你好")

fig = plt.figure()
ax = Axes3D(fig)

x = range(0,100)
# x = [i/1000 for i in x]
# plt.plot(x,[math.log(y,math.e) for y in x],label="y3")

def getY(y):
    a = 10
    return y/(y+a)

def getY2(y):
    a = 5
    return y/(y+a)

def getY3(y):
    return 1-(1/y)


x = range(0,20)
y = range(0,20)
def getZ(x, y):
    k1 = 2
    k2 = 5
    result = []
    for xx in x:
        for yy in y:
            z = (k1*xx+k2*yy)**2
            result.append([z])
    return result

z = getZ(x,y)

print(x)
print(y)
print(z)
ax.plot_surface(numpy.array(x), numpy.array(y), numpy.array(z), rstride=1, cstride=1, cmap='rainbow')


# x = [a*1 for a in x]
# plt.plot(x,[getY(y) for y in x],label="y3")
# x = [a*3 for a in x]
# plt.plot(x,[getY2(y) for y in x],label="y")
# plt.plot(x,[y**2 for y in x],label="y")



# print(x)
# print([getY(y) for y in x][:100])

plt.show()