#! /usr/bin/env python3
# -*- coding:utf-8 -*-


"""
上一节课学习了 数据类型，变量,字符串，编码
本节学习 list, tuple, 条件判断， 循环
"""

__author__ = "Liyy"

print("list 是一种有序的集合，可以对元素随时进行增加，删除操作")

classstu = ["zhang", "Li", "Xiao"]
print(classstu)
print("classstu 的类型是:%s,长度是%d"%(type(classstu), len(classstu)))
print("classstu 的第一个元素是:%s,最后一个元素是:%s"%(classstu[0], classstu[(len(classstu)-1)]))

print("最后一个元素可以使用长度减一，也可以直接使用-1,%s"%classstu[-1])
print("倒数第二个就是-2:%s,倒数第三个就是-3:%s"%(classstu[-2], classstu[-3]))

print("插入元素: 直接对list调用append函数")
classstu.append("wang")
print("最新的是:%s"%classstu)
print("指定位置插入: 使用insert 函数")
classstu.insert(1, "Mick")
print("在索引1处插入'Mick'%s"%classstu)
print("调用pop(i)方法删除元素，不传参数默认删除最后一个")
classstu.pop()
print("删除完最后一个之后%s"%classstu)
classstu.pop(1)
print("删除索引1之后%s"%classstu)

print("修改元素: 直接给指定元素赋值")
classstu[1]=99
print("将索引1 的值修改为99:%s, list 中的元素可以不是一种类型"%classstu)
print("list的元素可以是另外一个list")
classstu.append(["Male", 18])
print("最新的list：%s"%classstu)
print("输出一个子元素:%s"%classstu[3][1])
print("====="*10)


print("tuple:有序列表，一旦初始化 不能修改")

tu = ("zhang", "Li", "Xiao")
print("tulpe使用的是'()', list 使用的是'[]' :")
print(tu)
print("tulpe 不可变，所以没有insert() ,append()")

tu2 =(1,)
print("注意：当声明tulpe时，即使只有一个元素 最后也要加上,")
print(tu2)
print("---"*30)
print("作业:")
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])
print(L[1][1])
print(L[2][2])
print("list,tulpe 结束")
print("===="*30)

print("条件判断")

age = 20
if age >= 6:
    print(">=6")
elif age >= 18:
    print(">=18")
elif age >= 30:
    print(">=30")
else:
    print("old")

x = "a"
if x:
    print("只要X是非零数值，非空字符串，非空list, 就是True")

# inp = input("请输入你心中的数字:")
inp = "100"
print("你输入的是:%s"% inp)
print("转换 一下是:%d"%int(inp))
if int(inp) == 100:
    print("我猜对了")
else:
    print("没有猜对")

if inp == '100':
    print("你真的猜对了")
else:
    print("你还是没有猜对啊")

print("----"*30)
print("作业：")

h = 1.75
w = 84

bmi = w/(h*h)

print("bmi:%s"%bmi)

if bmi > 32:
    print("你是严重肥胖啊")
elif bmi > 28:
    print("你是肥胖啊")
elif bmi > 25:
    print("你是过重啊")
elif bmi > 18.5:
    print("你的体重正常")
else:
    print("你的体重过轻了")

print("条件判断 结束")
print("===="*30)
print("循环")

print("第一种循环: for ... in,依次把list或tuple中的每个元素迭代出来")
for s in tu:
    print(s)

print("range()函数可以生成一个整数序列,再使用list()转换为list")

print(list(range(10)))
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

print("第二种循环：while 循环,只要条件满足就不断循环")
su = 0
n = 99
while n>0:
    su = su +n
    n = n-2
print(su)
print("====="*30)
print("作业")
L = ['Bart', 'Lisa', 'Adam']
for n in L:
    print("Hello,%s!"%n)

print("break 是直接跳出循环, continue 是跳过当前循环")


