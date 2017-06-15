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
#print(fact(1000))  # 这里不会输出错误


#fact(1000)   # 栈溢出, 下方有代码时 不会抛出错误信息
# 检测到哪一层出现异常
# for i in range(900,1000):
#     try:
#         fact(i)
#         print("测试到：%d"%i)
#     except RuntimeError as e:
#         print("%d 出现异常:%s"%(i,e))
#         break;

print("---"*30)

def fact1(n):
    return fact_iter(n,1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num-1,num*product)


print(fact1(5))        

