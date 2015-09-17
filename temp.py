'''
-Converts celcius temperatures into farenheight temperature-

>>> temp_conv(0)
32.0

>>> temp_conv(117)
242.6

>>> temp_conv(77.32)
171.176

>>> temp_conv(52./79)
33.18481012658228

'''
import argparse

def temp_conv(c):
    f = (9.0/5)*c +32.
    return f

temp_conv(10)

if __name__ == "__main__":
    import doctest
    #doctest.testmod() 

    parser = argparse.ArgumentParser()
    parser.add_argument('-c', type = float)
    args = parser.parse_args()
    c = args.c
    
    print temp_conv(c)