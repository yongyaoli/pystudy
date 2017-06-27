#! /usr/bin/env python3
# -*- coding:utf-8 -*-


'''
BIF 函数 filter
filter:接收一个函数和序列，把传入的函数依次作用于每个序列元素，根据返回值说True还是False决定是否保留该元素

BIF 函数 sorted
排序： sorted函数可以对list进行排序

返回函数： 函数作为返回值
'''

# 保留奇数
def is_odd(n):
    '''
    保留奇数
    '''
    return n % 2 ==1

l = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print(type(l))
print(l)

# 删除空字符串
def not_empty(s):
    return s and s.strip()

print(filter(not_empty,['A', '', 'B', 'C',None,'','0']))


print('---'*30)

print(sorted([1, 90, -12, 12,-23]))

print("---"*30)

def lazy_sum(*args):
    def sum():
        nx = 0
        for n in args:
            nx = nx +n
        return nx
    return sum

s = lazy_sum(1, 2, 3, 4, 5, 6)
print(s)

print(s())

