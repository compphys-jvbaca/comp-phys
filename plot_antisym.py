'''
HW #3 
Name:Jacob Baca
Partner: Terry "Taco" Tran
'''

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm #color map
import numpy as np


def antisym(x1, x2, n1 = 1, n2 = 2, a = 1.0):
	psi1 = (2/a)*(np.sin((n1*np.pi*x1)/a)*np.sin((n2*np.pi*x2)/a))
	psi2 = (2/a)*(np.sin((n1*np.pi*x2)/a)*np.sin((n2*np.pi*x1)/a))
	psi = psi1 - psi2
	prob = np.abs(psi)**2
	return psi, prob

fig = plt.figure()
ax = fig.add_subplot(121, projection='3d')
plt.title("Wave Function")

ay = fig.add_subplot(122, projection='3d')
plt.title("Probability Density")

plt.suptitle("Antisymmetric Spatial Wave Function")
x1 = x2 = np.linspace(-1,1,77)
xv, yv  = np.meshgrid(x1,x2)
z,z2 = antisym(xv,yv)
ax.plot_surface(xv,yv,z, rstride = 1, cstride = 1, cmap=cm.coolwarm, linewidth = 0.2)
ay.plot_surface(xv,yv,z2, rstride = 1, cstride = 1, cmap=cm.coolwarm, linewidth = 0.2)

fig.text(.1, .02, 'The "effective" interaction between two neutral Fermions \
 (both spin up) that \n arises from the symmetry requirement on the total wave function.')

plt.show()