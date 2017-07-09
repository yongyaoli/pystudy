#! /usr/bin/env python3
# -*- coding:utf-8 -*-

'''
获取对象信息
'''
import types

def fn():
    pass


class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Hasky(Dog):
    def run(self):
        print('Hasky is running...')

# type() 函数 判断对象的类型
print(type(123))
print(type('abc'))
print(type(None))
print(type(abs))
a = Animal()
print(type(a))

print(type(123)==type(456))

print(type(123)==int)

# 判断对象是否是函数
print(type(fn)==types.FunctionType)

print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x:x)==types.LambdaType)
print(type(x for x in range(10))==types.GeneratorType)

# 判断class的类型

a = Animal()
d = Dog()
h = Hasky()
print(isinstance(a, Hasky))
print(isinstance(a, Animal))
print(isinstance(d, Hasky))

# 能用 type()判断的基本类型 也可以用 isintance() 判断

print(isinstance('a', str))
print(isinstance(123, int))
print(isinstance(b'a', bytes))

# 判断一个变量是否是某些类型中的一种
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 3, 3), (list, tuple)))

print("==="*20)

# dir()函数可以获取对象的所有属性和方法
print(dir('abc'))

print(len('ABC'))
print('ABC'.__len__())
print('ABC'.lower())
print('ABC'.isupper())

# getattr() 可以获取一个对象的属性
# setattr() 可以设置一个对象的属性
# hasattr() 可以判断对象是否包含特定属性

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()


print(hasattr(obj, 'x'))     # 判断是否有x 属性
print(setattr(obj, 'y', 19)) # 设置一个 属性y ,y的值是  19
print(getattr(obj, 'y'))     # 获取一个属性 y的值
print(getattr(obj, 'z', 20)) # 获取一个属性的值，并设置没有值时返回的默认值

# print(getattr(obj, 'zz'))

print(getattr(obj, 'power'))  # 获取属性 power


f = getattr(obj, 'power')  # 获取属性 power 并赋值到 f
print(f)
print(f())


