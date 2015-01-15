'''
Created on Oct 11, 2012

@author: themez
'''

digits={
        1:"one",
        2:"two",
        3:"three",
        4:"four",
        5:"five",
        6:"six",
        7:"seven",
        8:"eight",
        9:"nine",
        10:"ten",
        11:"eleven",
        12:"twelve",
        13:"thirteen",
        14:"fourteen",
        15:"fifteen",
        16:"sixteen",
        17:"seventeen",
        18:"eighteen",
        19:"nineteen",
        20:"twenty",
        30:"thirty",
        40:"forty",
        50:"fifty",
        60:"sixty",
        70:"seventy",
        80:"eighty",
        90:"ninety"
        }
def word(n):
    return digits.get(n,None)

def words(n):
    w=""
    if word(n/100)!=None:
        w+=(word(n/100)+" hundred")
    if word(n-n/100*100)!=None:
        w+=(" and "+word(n-n/100*100) if len(w)!=0 else word(n-n/100*100))
        return w
    elif word( (n-n/100*100)-(n-n/10*10) )!=None:
        w+=(" and "+word(n-n/100*100-(n-n/10*10)) if len(w)!=0 else word(n-n/100*100-(n-n/10*10)))
        if word(n-n/10*10)!=None:
            w+=("-"+word(n-n/10*10))
    else:
        if word(n-n/10*10)!=None:
            w+=(word(n-n/10*10))
    return w
if __name__ == '__main__':
    
    print sum([len(w.replace(" ","").replace("-","")) for w in [words(i) for i in range(1,1000)]])+11
        
