'''
Created on Oct 11, 2012

@author: themez
'''

if __name__ == '__main__':
    n=9999
    cnt=0
    while(n!=0):
        print n
        n=n&(n-1)
        cnt+=1
    print cnt
