import matplotlib
from numpy import array
import matplotlib.pyplot as plt
import numpy

x=numpy.loadtxt(r'C:\Users\gemslab\Desktop\新建文本文档 (2).txt')
y=numpy.loadtxt(r'C:\Users\gemslab\Desktop\新建文本文档 (3).txt')
fig=plt.figure()
ax=fig.add_subplot(121)
bx=fig.add_subplot(122)
datax=[1,2,3,4]
datay=[4,3,2,1]
ax.scatter(datax,datay,15.0*array(datax),15.0*array(datay))
bx.scatter(x,y)
plt.show()