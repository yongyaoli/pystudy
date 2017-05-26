#! /usr/bin/env python3
# -*- coding:utf-8 -*-

"""
长节学习到的是 dict set
本节学习的是函数
python 内置函数文档地址:https://docs.python.org/3/library/functions.html
查看函数帮助说明 help(abs)
"""

from fun import my_abs
# 从fun.py 里引入 my_abs 函数

# import platform
# print(platform.python_version())  #文件， 首选项，设置，用户设置
print("函数的调用:",end='\n')
help(abs)
help(max)
v = max(range(100))
print(v)

n1 = 255
n2 = 10000
VV = hex(n1)
XX = hex(n2)
print(VV)
print(XX)

print("函数名其实是指向一个函数对象的引用,可以赋值给一个变量")
B = hex
print(B(n1))
print("----"*30)

print("函数的定义： 使用关键字def , 函数名(参数...):  使用return 进行返回函数结果")

def my_fun(x):
    '''
    this is my first fun
    get the abs value
    the paramter shuld be a int
    '''
    if not isinstance(x,(int,float)):
        raise TypeError(" bad oper type")
    if x>=0:
        return x
    else:
        return -x

print(my_fun(-99))
print(my_fun(12))

help(my_fun)
print("---"*30)
print("1.一旦出现return 后面的语句就不再执行")
print("2.如果没用return语句，函数执行完毕也会返回结果，只是返回的是None")

print(my_abs(-91)) # my_abs 函数出自fun.py 中的my_abs 函数

# print(my_abs("1"))
help(isinstance)
print("返回多个结果: return 结果1,结果2...   实际返回的是一个tulp")

def mores(w,h,m=1):
    return w*m,h*m


XX = mores(120,60,3) 
print(XX)
print("----"*30)
print("注意：",end='\n')
print("定义函数式，需要确定函数名和参数个数",end='\n')
print("如有必要，对参数进行数据类型检测",end='\n')
print("函数内部可以使用return 随时返回结果",end='\n')
print("函数没用return 语句时，自动 return None",end='\n')
print("函数可以返回多个值，实际上是一个tulp")
print("----"*30)





