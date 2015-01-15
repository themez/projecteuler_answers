'''
Created on Oct 10, 2012

@author: themez
'''
def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)
def mcm(x,y):
    return x*y/gcd(x,y)
if __name__ == '__main__':
    res=1
    for i in range(1,21):
        res=mcm(res,i)
    print res
    pass