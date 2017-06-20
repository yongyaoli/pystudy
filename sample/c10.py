#! /usr/bin/env python3
# -*- coding:utf-8 -*-

"""
上一节：列表生成器，生成器
本节：迭代器
"""
from collections import Iterable
from collections import Iterator

# 可以直接作用于for 循环的数据类型：
# 1. 集合数据类型： list, tuple, dict,set, str 等
# 2. generator 包含生成器和带yield的generator fun
# 这些可以直接作用于for循环的对象统称为[可迭代对象]：Iterable

# 判断对象是否是 Iterable 对象
print(isinstance([], Iterable))
print(isinstance((), Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

# 可以被 next() 函数调用并不断返回下一个对象称为[迭代器]： Iterator
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))

# 生成器都是 Iterator, 但是 list,dict,str是Iterable,不是Iterator
# 可以使用iter() 将 list, dict,str 转换成 Iterator
print(isinstance([1, 2, 3], Iterator))
print(isinstance('aaa', Iterator))

print(isinstance(iter('aaa'), Iterator))
print("==="*30)

print("凡是可作用于for循环的对象都是 Iterable 类型")
print("凡是可作用于next() 函数的对象都是 Iterator类型，表示一个惰性计算的序列")

