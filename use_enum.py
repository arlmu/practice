#! /usr/bin/python3
# -*- coding: utf-8 -*-

from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fir = 5
    Sat = 6

day1 = Weekday.Mon

print('day1 = ',day1)
print('Weekday.Tue=', Weekday.Tue)
print('weekday[tue] =', Weekday['Tue'])
print('weekday.Tue.value = ',Weekday.Tue.value)



for name, member in Weekday.__members__.items():
    print(name, '=>', member)


M = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul','Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

print(M.Jan)
for name, member in M.__members__.items():
    print(name, '=>', member, ',', member.value)
