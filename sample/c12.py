#! /usr/bin/env python3
# -*- coding:utf-8 -*-
from collections import Iterator
from functools import reduce

'''
map/reduce 函数
'''
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回

def f(x):
    return x * x

r = map(f, [1,2,3,4,5,6,7,8,9])
# r 是一个list
print(r)
print(list(r))
print(isinstance(r, Iterator))
print(type(r))
s = map(f,(11,12,13,14,15,16,17))
print(s)
print(isinstance(s, Iterator))
print(type(s))
# 示例3
t = map(lambda x: x + 1, range(10))
print(t)
print(type(t))
for i in t:
    print(i)

# map() 作为高阶函数，事实上 它把运算规则抽象了
st = map(str, [1,2,3,4,5,6,7,8])
print(st)

print("----"*30)
print("-------reduce-------")
print("reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算")

# 比如一个序列求和

def add(x, y):
    return x + y

r = reduce(add, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(r)
# eg: 求和运算可以直接使用BIF 函数： sum()
print(sum([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# 如果要把[1,2,3,4,5] 变成整数 12345 
def fn(x, y):
    return x * 10 + y

print(reduce(fn, [1,2,3,4,5]))

# 字符串转int

def char2num(s):
    return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]
def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

  
str2int('123456789')

