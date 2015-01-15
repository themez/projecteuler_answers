'''
Created on Oct 9, 2012

@author: themez
'''
from math import sqrt
def isPrime(nu):
    if nu==2:
        return True
    sqt=int(sqrt(nu))
    for i in range(2,sqt+1):
        if nu%i==0:
            return False
    else:
        return True

def main(n):
    max=1
    for i in range(2,int(sqrt(n))):
        if n%i==0 and isPrime(i):
            max=i
    return max
        
if __name__ == '__main__':
    print(main(600851475143))
    pass