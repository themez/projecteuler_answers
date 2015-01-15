'''
Created on Oct 10, 2012

@author: themez
'''

if __name__ == '__main__':
    
    for a in range(1,300):
        for b in range(a,(1000-a)/2):
            if a**2+b**2==(1000-a-b)**2:
                print("%d,%d,%d"%(a,b,1000-a-b))
    pass