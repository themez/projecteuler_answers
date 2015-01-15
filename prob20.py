'''
Created on Oct 23, 2012

@author: themez
'''
def factorial(n):
    if n==1:
        return 1
    else:
        return n *factorial(n-1)
if __name__ == '__main__':
    digs = factorial(100)
    print reduce(lambda x,y:x+y, map(lambda x: int(x),str(digs)))
    pass