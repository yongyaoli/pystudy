#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
'''
上一节：切片， 迭代
本节：列表生成式, 生成器
'''
print('--'*10,'列表生成器','--'*10)
li = [x*x for x in range(1, 11)] #x*x 要生成的元素, for循环生成，
print(li)

#可以在for后面 加上if 判断
MYLI = [x*x for x in range(1, 11) if x % 2 == 0]
print(MYLI)

# 多重循环
MYSEC = [m + n for m in 'ABCDEFG' for n in 'ZXCVBNM']
print(MYSEC)
print(len(MYSEC))

#列出当前目录下所有文件和目录名
MENULIST = [d for d in os.listdir('.')] # os.listdir 可以列出文件和目录
print(MENULIST)
print(os.listdir('.'))

# for循环可以使用多个变量，比如dict, items()
D = {"A":"1", "B":"2", "C":"3", "D":"4"}

for k, v in D.items():
    print(k, '=', v)

NL = [k+'='+v for k, v in D.items()]
print(NL)


# 把列表所有字符串变小写
L = ['Tom', 'Jerry', 'Li', 'Fance']
NNL = [x.lower() for x in L]
print(NNL)
print('---'*30)
L1 = ['Hello', 'World', 18, 'Apple', None]
TNNL = [x.lower() for x in L1 if isinstance(x, str)]
print(TNNL)

print('--'*10,'生成器','--'*10)
print("生成器：列表元素可以通过计算得出，在循环的过程中不断推算后续元素")
# 创建生成器: 将列表生成器的[] 修改为() 就创建了一个生成器:generator
G = (x * x for x in range(10))
print(G)
 
print(next(G))
print(next(G))
print(next(G))
print(next(G))
print(next(G))
print(next(G))
print(next(G))
print(next(G))
print(next(G))
print(next(G))

# print(next(G))  # 抛出StopInteration异常
# generator 保存的是算法，每次调用 next(G) 就会算出G的下一个元素的值，没有更多元素时 抛出StopIteration异常
# 因为generator 是可迭代对象，所以可以使用for 循环
# 上方使用next 已经输出完G的所有元素，再次使用for 就没有元素可输出，所以是个空，需要重新声明一个 生成器可供循环
print('---'*30)
GG = (x * x for x in range(10))
for n in GG:
    print(n)

# 斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到
print('--'*10,'Fibonacci','--'*10)
def fib(max):
    n, a, b = 0, 0, 1
    while n<max:
        print(b)
        a, b = b, a+b
        n = n +1
    print('done')

fib(6)

# 上述函数修改为 生成器
print('---------------------------')
def fib2(max):
    n,  a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n+1
    return   # 作为生成器，因为每次迭代就会返回一个值，所以不能显示的在生成器函数中return 某个值，包括None值也不行，否则会抛出“SyntaxError”的异常，但是在函数中可以出现单独的return，表示结束该语句。
print('上述函数为定义生成器的 第二种方法：如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator')
print(fib2(6))

for x in fib2(6):
    print(x)

# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
print('----'*30)
g = fib2(6)

print('---'*30)

def triangles(max):
    i = 0
    L = [1]
    while i < max:
            yield L
            L = [1] + [ L[x-1] + L[x] for x in range(1, len(L))] +[1]
            i = i + 1
    return 

for n in triangles(12):
    print(n)
