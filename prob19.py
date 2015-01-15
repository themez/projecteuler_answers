'''
Created on Oct 21, 2012

@author: Eddy.Zeng
'''

sday = (1900,1,1,0)


class Day(object):
    leapM = [1,3,5,7,8,10,12]
    nonLeapM = [4,6,9,11]
    spM = [2]
    def __init__(self,y,m,d):
        self.y=y
        self.m=m
        self.d=d
        self.isLeapYear = True if (self.y%400 == 0 or (self.y%100!=0 and self.y%4==0)) else False
    def __repr__(self):
        return "%s:%s:%s" %(self.y, self.m, self.d)
    def nthdOfYear(self):
        return (
            len(filter(lambda _: _<self.m, self.leapM))*31 + 
            len(filter(lambda _: _<self.m, self.nonLeapM))*30 + 
            len(filter(lambda _: _<self.m, self.spM))* (29 if self.isLeapYear else 28)+
            self.d
            )
    def minus(self, day):
        if(self.y==day.y):
            return self.nthdOfYear()- day.nthdOfYear()
        elif(self.y > day.y):
            return self.minus(Day(day.y+1, 1, 1)) + (day.daysOfYear()-day.nthdOfYear())+1
        else:
            return -day.minus(self)
    def __days2sday(self):
        return self.minus(Day(1900,1,1))
    def daysOfYear(self):
        if self.isLeapYear:
            return 366
        else:
            return 365
    def dayOfWeek(self):
        return self.__days2sday()%7+1

if __name__ == '__main__':
#    print Day(2012,10,23).dayOfWeek()
    count=0
    for y in range(1901, 2001):
        for m in range(1,13):
            if Day(y,m,1).dayOfWeek()==7:
                count+=1
    print count
    pass