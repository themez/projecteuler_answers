'''
Created on Oct 10, 2012

@author: themez
'''
import math
def degree(A,B,C):
    return abs(math.atan2(B[1]-A[1],B[0]-A[0])-math.atan2(C[1]-A[1],C[0]-A[0]))
def has45Degree(k,a,b,c):
    A,B,C = zip([a,b,c], map(lambda x: x**2/k ,[a,b,c]))
    if abs(degree(A,B,C)-math.pi/4)<=0.01 or abs(degree(B,C,A)-math.pi/4)<=0.01 or abs(degree(C,A,B)-math.pi/4)<=0.01:
        print("A:%s,B:%s,C:%s"%(degree(A,B,C),degree(B,C,A),degree(C,A,B)))
        return True
    else:
        return False
def F(K,X):
    cnt=0
    for k in range(1,K+1):
        for a in range(-X,X-1):
            for b in range(a+1,X):
                for c in range(b+1,X+1):
                    if has45Degree(k,a,b,c):
                        print("%d,%d,%d,%d"%(k,a,b,c))
                        cnt+=1
                    else:
                        print("fail:%d,%d,%d,%d"%(k,a,b,c))
    return cnt
if __name__ == '__main__':
    print F(1,10)
#    print degree((0,0),(100,1),(1,1))
    pass