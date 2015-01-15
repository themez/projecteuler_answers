'''
Created on Oct 23, 2012

@author: themez
'''
alphaMap = {
            'A':1,
            'B':2,
            'C':3,
            'D':4,
            'E':5,
            'F':6,
            'G':7,
            'H':8,
            'I':9,
            'J':10,
            'K':11,
            'L':12,
            'M':13,
            'N':14,
            'O':15,
            'P':16,
            'Q':17,
            'R':18,
            'S':19,
            'T':20,
            'U':21,
            'V':22,
            'W':23,
            'X':24,
            'Y':25,
            'Z':26
            }
def evalName(name):
    value=0
    for s in name:
        value+=alphaMap.get(s,0)
    return value

if __name__ == '__main__':
    data=None
    with open("C:/workspace/program/euler/apps/data/names.txt","r") as f:
        data = sorted(map(lambda x: x.strip('"'),f.read().split(",")))
    print sum([evalName(name)*(i+1) for i,name in enumerate(data)])
        
    pass