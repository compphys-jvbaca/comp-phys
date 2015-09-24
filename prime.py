'''

HW #3
Name : Jacob Baca
Partner : Terry Tran

>>> Prime(-37, 30)
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

>>> Prime(1, 81)
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]
'''
import numpy as np
import pdb
import argparse

def Prime(a, b):
    if a <=1:
        a = 2
    prime_lst = []
    lst = np.arange(a,b)
    for m in lst:
        test = []
        for n in range(2,10):
            if n == m:
                continue
            rem = m % n
            test.append(rem)

        if 0 not in test:
            prime_lst += [m]

    return prime_lst

#if __name__ == "__main__":
#   import doctest
#   doctest.testmod()

parser = argparse.ArgumentParser()
parser.add_argument('-a', type = int)
parser.add_argument('-b', type = int)
args = parser.parse_args()
print Prime(args.a, args.b)


