#! /usr/bin/env python3
# -*- coding:utf-8 -*-

'''
上节学习函数 的参数
本节学习递归函数: 函数内部调用函数本身
'''

def fact(n):
    '''
        阶乘函数
    '''
    if n==1:
        return 1
    return n*fact(n-1)


num = fact(10)
print(num)
print(10*fact(9))
print(fact(100))


#fact(999)   # 栈溢出





