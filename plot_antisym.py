'''
returns the value of the total wave function ψ

'''

import numpy as np
import pdb
import argparse


def antisym(x1, x2, n1 = 1, n2 = 2, a = 1.0):
	psi1 = (2/a)*(np.sin((n1*pi*x1)/a)*np.sin((n2*pi*x2)/a))
	psi2 = (2/a)*(np.sin((n1*pi*x2)/a)*np.sin((n2*pi*x1)/a))
	psi = psi1 - psi2
	return psi


	
parser = argparse.ArgumentParser()
parser.add_argument('-x1', type = int)
parser.add_argument('-x2', type = int)
args = parser.parse_args()
print (args.x1, args.x2) #figure out