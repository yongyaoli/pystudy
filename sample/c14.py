#! /usr/bin/env python3
# -*- coding:utf-8 -*-

'''
装饰器：   
在不修改函数定义的情况下对函数增加功能的方式 就是装饰器：Decorator
'''
from datetime import datetime
import functools
# 引入 functools 是为了解决 装饰器本身需要传入参数时 函数__name__ 变动的问题



def now():
    print(datetime.now())

f = now
f()
print(now.__name__)  # __name__ 属性可以拿到函数的名字
print(f.__name__)    # 也是输出 now
print("-------")
# 为now 函数天津装饰器
# 声明一个添加日志的装饰器
def log(func):
    @functools.wraps(func)
    def warpper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return warpper
# 带参数   
def log2(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper 
    return decorator



@log
def now2():
    print(datetime.now())

now2()

# 效果  now = log2('log2')(now)
@log2('log2')
def now3():
    print(datetime.now())

now3()

print('***'*20)
print('偏函数， 需要 import functools')
print('functools.partial 的作用就是把一个函数的某些参数固定住，返回一个新函数')
int2 = functools.partial(int, base=2)
print(int2('1000000'))

