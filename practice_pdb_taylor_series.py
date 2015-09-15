'''
>>> L(1) - 0.697975466546841684 < 1e-6 
True

'''

import pdb
from math import *

def L(x, n=1000):
    if x<-1:
        return 'x cannot be below -1. Try Again'
    #pdb.set_trace()
    for i in range(1, n+1):
	approx = 0.0
        approx += (1.0/i)*(x/(1.0000000+x))**(i)
    	if i == n-1:    
    	    o_approx = approx 
    fracerror = (abs(o_approx - approx) / approx) * 100
    print 'Oh nooooooooooo, stop!', fracerror  
    return approx

x = 400
y = L(x)
approx = 0
print 'Taylor Series Approximation:', y
from math import log  #you would guess math module would have log...yes!
#exact_val = log(1+x)
#print 'exact_val', exact_val
#from math import log1p  #more accurate for small x.
#print 'log1p output', log1p(x)

if __name__ == "__main__":
    
    import doctest
    doctest.testmod() 
    
    x =1000
    y = L(x)
    print 'series approx', y