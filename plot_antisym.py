'''
returns the value of the total wave function phi
'''
from pylab import *
import numpy as np
%matplotlib inline
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm #color map

import numpy as np
import pdb
import argparse


def antisym(x1, x2, n1 = 1, n2 = 2, a = 1.0):
	psi1 = (2/a)*(np.sin((n1*np.pi*x1)/a)*np.sin((n2*np.pi*x2)/a))
	psi2 = (2/a)*(np.sin((n1*np.pi*x2)/a)*np.sin((n2*np.pi*x1)/a))
	psi = psi1 - psi2
	prob = np.abs(psi)**2
	return psi, prob

#parser = argparse.ArgumentParser()
#parser.add_argument('-x1', type = int)
#parser.add_argument('-x2', type = int)
#args = parser.parse_args()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x1 = x2 = np.linspace(0,100,77)
xv, yv  = np.meshgrid(x1,x2)
z = antisym(x1,x2)[0] #args.
ax.plot_surface(xv,yv,z, rstride = 1, cstride = 1, cmap=cm.coolwarm, linewidth = 0.2)

plt.show