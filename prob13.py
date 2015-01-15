'''
Created on Oct 11, 2012

@author: themez
'''

if __name__ == '__main__':
    nus=[]
    with open("C:/workspace/program/euler/apps/data/prob13.txt","r") as f:
        for rawLine in f:
            nus.append(int(rawLine))
    print str(sum(nus))[0:10]
