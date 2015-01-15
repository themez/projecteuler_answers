'''
Created on Oct 29, 2012

@author: themez
'''
from datetime import datetime

def main():
    count=0
    i = 123456789
    while(i<1000000000):
        s = str(i)
        se = set(s)
        if (not "0" in se) and len(se) == len(s):
            count+=1
        i+=1
    print(count)
    while(i<=9876543210):
        s = str(i)
        se = set(s)
        if len(se) == len(s):
            count+=1
            if count==1000000:
                print(i)
                break
        i+=1
if __name__ == '__main__':
    print datetime.now()
    main()
    print datetime.now()
    pass