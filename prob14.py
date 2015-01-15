'''
Created on Oct 11, 2012

@author: themez
'''
def collatz(n):
    cnt=1
    temp=n
    while(temp!=1):
        if temp%2==0:
            temp=temp/2
        else:
            temp=3*temp+1
        cnt+=1
    return n,cnt
if __name__ == '__main__':
    maxi=0
    no=0
    for n,cnt in  [collatz(i) for i in range(1,1000000)]:
        if cnt>maxi:
            maxi=cnt
            no=n
    print (no, maxi)
        
        
