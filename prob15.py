'''
Created on Oct 11, 2012

@author: themez
'''
from operator import mul
if __name__ == '__main__':
    print reduce(mul,range(21,41))/reduce(mul, range(1,21))
    pass