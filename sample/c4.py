#! /usr/bin/python3
# -*- coding:utf-8 -*-

"""
上一节课学习了 list, tuple, 条件判断， 循环
本节学习 dict set
"""

__author__ = "Liyy"
print("---"*20)
print("dict 字典，键值对的形式存放")

stu = {"zhang":16, "li":17, "wang":18} # 声明
print(stu["li"])   #获取值
stu["li"] = 99       #重新赋值
print(stu["li"])   #查看
stu["zzz"] = 1      #如果key不存在 就直接添加了  应该是python3.5的新特性
print(stu)
# 判断key是否存在 1
print('zzz' in stu)
print('z' in stu)
# 判断key是否存在 2
print(stu.get('zzz'))  #如果存在就返回值
print(stu.get('z',0))   # 如果不存在 就返回None, 或者自己指定的值
if stu.get('zzz')==None:
    print('没有')
else:
    print("有:%s"%stu.get('zzz'))

print(stu.pop("zzz"))  #删除一个key

print(stu)

print("dict内部存放的顺序和key放入的顺序是没有关系的")
print("dict的key必须是不可变对象")
print("---"*30)

print("set 与dict类似，但是不存储value, 是一组key的集合")
ss = set([1,2,3])
print(ss)
ss.add(3)  # 添加元素，会自动过滤重复元素
ss.add(4)
ss.add(5)
print(ss)

ss.remove(3)  #删除元素
print("=======================")
# 两个set 交集，并集
s2 = set([1,2,8,9,0])
print(ss)
print(s2)
print(ss & s2)

print(ss | s2)
