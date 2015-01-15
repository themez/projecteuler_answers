'''
Created on Oct 10, 2012

@author: themez
'''
import math

def isPrime(n):
    """check if n is a prime"""
    primes=getPrimesLT(n)
    return n in primes

def getPrimesLT(n):
    """get primes less than n """
    primes=[2]
    for i in range(3,n+1,2):
        sqt=math.sqrt(i)
        for prime in primes:
            if prime>sqt:
                primes.append(i)
                break
            if i%prime==0:
                break
    return primes
if __name__ == "__main__":
    assert(isPrime(1)==False)
    assert(isPrime(2)==True)
    assert(isPrime(3)==True)
    assert(isPrime(4)==False)
    assert(isPrime(5)==True)
    assert(isPrime(6)==False)
    assert(isPrime(7)==True)
    `