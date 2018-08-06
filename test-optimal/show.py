#!/usr/bin/env python3

from mpl_toolkits.mplot3d import Axes3D
import numpy
import matplotlib.pyplot as plt
import math

data = numpy.loadtxt('build/path.txt')

plt.figure(figsize=(18, 18))
ax = plt.axes()
plt.xlim(18)
plt.ylim(18)
for i in range(len(data)):
    plt.arrow(data[i,0],data[i,1],0.5*math.cos(data[i,2]),0.5*math.sin(data[i,2]),width=0.01)
#fig = plt.figure()
#ax = fig.gca(projection='3d')
#ax.plot(data[:,0],data[:,1],data[:,2],'.-')
plt.show()
