'''
Created on Oct 23, 2012

@author: themez
'''
def getProperDivisors(n):
    ds = []
    for i in range(1, n/2+1):
        if n%i==0:
            ds.append(i)
    return ds
def d(n):
    return sum(getProperDivisors(n))
if __name__ == '__main__':
    amicableNums=[]
    for i in range(1, 10001):
        if d(d(i))==i and i!=d(i):
            print i
            amicableNums.append(i)
    print sum(amicableNums)
    pass