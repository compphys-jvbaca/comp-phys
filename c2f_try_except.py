'''
    
    The utility of try...except...else
    
    At some point, one needs to do
    
    C = args.C
    
    But what if the user forgot enter C at the command line?
    Yes, the Python shell will catch the error, but the error message
    is often uninformative.  
    
    And to the user, it appears the programmer hasn't done their job well.

'''


import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-C', type = float)
args = parser.parse_args()


try:
    # if C is not entered at the command line, args.C will be of type None
    args.C/2.
# would this catch the error?
# print C
except:
    print '\nYou failed to provide Celsius degrees as input on the command line!\n'
    raise TypeError
else:
    C = args.C

F = 9.0*C/5 + 32
print '{:g} C is {:.1f} F'.format(C, F)
