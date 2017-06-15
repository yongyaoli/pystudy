#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Iterable

"""
上一节递归， 没懂， 尾递归 更没懂
本节：高级特性， 切片， 迭代

"""
__author__ ="Liyy"

print('-------切片-------')
L = ["zhangsan","lisi","wanger","mazi","ly","tom","jerrey"]
print(L)
NL = L[0:3]
print("L[0:3]表示索引从0开始取，到索引为3，但是不包含3,如果从第0个元素开始取，可以省略第一个0, L[3]")
print(NL)
print(L[3])
print("支持倒数切片，倒数第一个元素是-1")
print(L[-1:])
print(L[-3:])
LI = range(100)
print(LI)
print("取11-20个数")
print(LI[11:20])
print("前10个数字 每2个取1个")
print(LI[:10:2])
print("所有数据 每5各取出一个")
print(LI[::5])
print("复制一个函数")
NLI = LI[:]
print(NLI)

print("--------------tulp切片结果仍然是tulp--------------")
t = (1,2,3,4,5,6)
print(t[:3])
s = "ABCDEFGH"
print(s[2:6])

print("给定一个list/tulp/dict/str, 我们可以通过for循环来遍历这个list/tulp/dict/str,这种遍历称之为迭代")
print(L)
print(t)
d = {"a":1,"b":2,"c":3}
print(d)
for k in d:  # 循环dict 的key
    print(k)  # 输出dict的key

for v in d.values(): # 循环dict 的value
    print(v)

for k, v in d.items():   # 循环dict的项，包含key,value
    print("k:%s, v:%s"%(k,v))

print("判断对象是否可迭代，1. 引入Iterable, 2. isinstance函数")


result = isinstance(d,Iterable)

print(result)

print(isinstance(123,Iterable))  # 数字不是可迭代对象

print("对没有下标的list进行下标循环")

for i,v in enumerate(['A','B','C','D']):
    print(i,v)


help(enumerate)
  
