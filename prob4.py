'''
Created on Oct 9, 2012

@author: themez
'''
def isPalindromic(n):
    return int(str(n)[::-1])==n

def hasProduct3(n):
    for i in range(100,999):
        if n%i==0 and len(str(n/i))==3:
            return True
    else:
        return False
if __name__ == '__main__':
    for i in range(998001,9009,-1):
        if isPalindromic(i) and hasProduct3(i):
            print(i)
            break
    pass