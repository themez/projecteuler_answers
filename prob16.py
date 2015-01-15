'''
Created on Oct 11, 2012

@author: themez
'''
from operator import add
if __name__ == '__main__':
    
    print reduce(lambda x,y:add(x,int(y)),str(2**1000),0)
    pass