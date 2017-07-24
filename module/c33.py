#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools
'''
itertools 
提供了非常有用的用于操作迭代对象的函数
'''
# count 会创建一个无限的迭代器
n = itertools.count(10,1)
for i in n:
    if i>=1000: # 不进行break会一直循环输出
        break
    print(n)

# cycle 会把传入的一个序列无限重复下去
cs = itertools.cycle('ABC')

# for c in cs: //无限循环
#     print(c)

# repeat 负责把一个元素无限重复下去，第二个参数可以限定重复次数
ns = itertools.repeat('A', 10)
for n in ns:
    print(n)

# 无限序列只有在for 迭代时才会无限迭代下去
# 如果只是创建一个迭代对象，不会生成无限序列

# takewhile() 根据条件判断截取一个有限的序列
na = itertools.count(1)
ns = itertools.takewhile(lambda x: x<=10, na)

print(list(ns))    

# chain() 可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('ABC','def'):
    print(c)

# groupby() 把迭代器中相邻的重复元素挑出来放在一起

for key, group in itertools.groupby('AAAbbCCCAAA'):
    print(key, list(group))

    
