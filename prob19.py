'''
Created on Oct 21, 2012

@author: Eddy.Zeng
'''

sday = (1900,1,1,0)


class Day(object):
    def __init__(self,y,m,d):
        self.y=y
        self.m=m
        self.d=d
    def __days4y(self, y):
        if y%400 == 0 or (y%100!=0 and y%4==0):
            return 366
        else:
            return 365
    def __days2MileStone(self):
        
    def days(self):
        if self.y%400 == 0 or (self.y%100!=0 and self.y%4==0):
            return 366
        else:
            return 365
    def dayOfWeek(self):
        
def 

if __name__ == '__main__':
    
    pass