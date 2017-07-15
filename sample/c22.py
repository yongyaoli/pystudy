#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# 需要引入enum
#import sys
#print(sys.version_info) 

# 当需要更精确的控制枚举类型，可以从Enum派生出自定义的类， 需要引入 unique
from enum import Enum, unique

'''
枚举类
'''
# 定义枚举
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# 输出
print(Month.Jan)
# 循环
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


# 自定义枚举类型,  @unique 装饰器可以帮助检查保证没有重复值, 取到有重复值的key时 报错
@unique
class Weekday(Enum): 
    Sun = 0 # 周日 值为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
    

print(Weekday.Mon)
print(Weekday['Sun'])
 
day1 = Weekday.Mon
print(day1 == Weekday.Mon)
print(day1 == Weekday.Thu)

print(Weekday(1))