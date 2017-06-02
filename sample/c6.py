#! /usr/bin/env python3
# -*- coding:utf-8 -*-

'''
上节学习函数： 函数的定义;bif 函数的查看;函数调用
本节学习函数的参数
'''


def demo(arg):
    return arg*3.14
    

print(demo(77))	

print("--"*40)

print("默认参数\n")

def demo2(arg,math=3.14):
    return arg*math

print(demo2(77,2))

print(demo2(77))
print("必选参数在前，默认参数在后,多个默认参数时 可以指定参数名")

def demo3(name, age=18,sex='男'):
    print("我是%s, 今年%d岁,是个%s"%(name,age,sex))

demo3('张三')
demo3('小丽', sex='女')

print("默认参数必须指向不可变对象\n")

print("**可变参数:")
def calc(*number):
    sum = 0
    for n in number:
        sum = sum + n*n
    return sum

print(calc(1,2,3,4))

num = [1,2,3,4,5]
print(calc(*num))

print("**关键字参数:")
print("可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict")

def person(name,age,**kw):
    print("name:%s, age:%d,other:%s"%(name,age,kw))
    print(len(kw))


person('zhangsan', 18, gender='男', mail="1000@qq.com")
print("可以先组装一个dict,然后把dict 转换为关键字参数")
extra = {'gender':'男', 'mail':'1000@qq.com', 'phone':'186*******'}
person('jack', 22, **extra)


