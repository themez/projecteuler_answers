'''
Created on Oct 11, 2012

@author: themez
'''



if __name__ == '__main__':
    data=[]
    with open("C:/workspace/program/euler/apps/data/prob18","r") as f:
        for rawLine in f:
            data.append( [int(x) for x in rawLine.split(" ")])
            
    current=-1
    suma=0
    stra=2**16
    def getStraBit(i):
        if len(bin(stra))-2>abs(i):
            return int(bin(stra)[i])
        else:
            return 0
        
    while(stra!=0):
        stra-=1
        temp=0
        current=-1
        for i, dataLine in enumerate(data):
            current+=getStraBit(-i-1)
            temp+=dataLine[current]
            
        suma= temp if temp>suma else suma
    print suma
