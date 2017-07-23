#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
datetime
python处理日期📅和时间⌚️的标准库
'''
#datetime是个模块，模块下包含一个datetime 类
from datetime import datetime, timedelta
 
now = datetime.now()  # 获取当前时间
print(now)
print(type(now))  # 类型

dt = datetime(2017,8,1,12,20) # 指定日期和时间构造一个datetime
print(dt)

# datetime 转换为 timestamp
# 在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp

ts = dt.timestamp()  # 将日期转换为 timestamp, 浮点(float)小数,小数位表示毫秒数
print(ts)
t = 1429417200.0
print(datetime.fromtimestamp(t))  # timestamp 转换为 datetime, 获取的是本地时间
print(datetime.utcfromtimestamp(t))  # UTC 时间

# str 和 datetime 互转
cday = datetime.strptime('2017-7-12 23:19:32', '%Y-%m-%d %H:%M:%S')
print(cday)
sday = datetime.now().strftime('%a, %b %d %H:%M')
print(sday)

# datetime加减： 需要导入 timedelta
n = datetime.now()
print(n)
print('加2个小时', n+timedelta(hours=2))
print('减3天', n-timedelta(days=3))
print('加1天2个小时', n+timedelta(days=1, hours=2))



print('datetime 表示的时间需要时区才能确定一个特定的时间，否则只能视为本地时间')
print('如果要存储datetime, 最佳方法是转换为timestamp再存储，因为timestamp的值与时区完全无关')




