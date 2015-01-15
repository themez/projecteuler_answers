'''
Created on Oct 10, 2012

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
#    def findNextPrime(current,cnt):
#        if cnt==10001:
#            print current
#        else:
#            findNextPrime(current+1,cnt+1 if isPrime(current) else cnt)
def main():
    cnt=0
    current=2
    while(True):
        if isPrime(current):
            cnt+=1
            if cnt==10001:
                print current
                break
        
        current+=1
        
if __name__ == '__main__':
    main()
    pass