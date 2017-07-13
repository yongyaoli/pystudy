#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
实例属性和类属性
'''

# 可以通过给实例绑定属性 的方法是通过实例变量或者通过 self 变量

class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')

# 如果Student 类本身需要绑定一个属性， 可以直接在class中定义一个属性，这种属性是类属性
class Student2(object):
    name = 'zhang' 

ss = Student2()
print(ss.name)

print(Student2.name)
ss.name = 'lisi'
print(ss.name)
print(Student2.name)
del ss.name
print(ss.name)

# 相同名字的实例属性将屏蔽掉类属性
# 当你删除实例属性后，访问的将是类属性