'''
Created on Oct 10, 2012

@author: themez
'''
from datetime import datetime
from primeUtil import getPrimesLT
if __name__ == '__main__':
    print datetime.now()
    print(sum(getPrimesLT(2000000)))
    print datetime.now()