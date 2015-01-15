'''
Created on Oct 11, 2012

@author: themez
'''
from math import sqrt
def countDivs(n):
    if n==1:
        return 1
    cnt=0
    for i in range(1,int(sqrt(n))+1):
        if n%i ==0:
            cnt+=2
    return cnt
if __name__ == '__main__':
    current=1
    iCur=1
    while(True):
        if countDivs(current)>500:
            print current
            break
        else:
            iCur+=1
            current+=iCur
        
    pass