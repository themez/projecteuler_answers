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

def isAbundant(n):
    return sum(getProperDivisors(n))>n

def allAbundantUnderN(n):
    return [i for i in range(0,n) if(isAbundant(i))]

def main():
    abundants = allAbundantUnderN(28124)
    l = len(abundants)
    nums=set()
    for i in range(0, l):
        for j in range(0, l):
            n = abundants[i]+abundants[j]
            if n< 28124:
                nums.add(n)
    
    print sum(filter(lambda x: x not in nums, range(0, 28124)))
    #print sum(range(0,28124))-sum(nums)
if __name__ == '__main__':
    main()