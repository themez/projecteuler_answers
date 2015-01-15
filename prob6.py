'''
Created on Oct 10, 2012

@author: themez
'''

if __name__ == '__main__':
#    res1=0
#    res2sqrt=0
#    for i in range(1,101):
#        res1+=i**2
#        res2sqrt+=i
#    res2=res2sqrt**2
#    print(res2-res1)
    print(sum(range(1,101))**2-sum([i**2 for i in range(1,101)]))
    pass