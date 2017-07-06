#! /usr/bin/env python3
# -*- coding:utf-8 -*-

'''
面向对象： 封装，继承，多态
类（Class）：类是抽象的模版
实例（Instance）：实例是根据类创建出来的一个个具体的对象
'''

# 类定义关键字class
# class后的Student 既是类名
# (object) 表示该类是从哪个类继承下来的
class Student(object):
    pass

# 创建类的实例， 是通过类名+()
s = Student()

print(type(Student))
print(type(s))


print(Student)
print(s)
# 可以自由的给实例变量绑定属性
s.name = 'zhangsan'

print(s.name)

# 重新定义一个类
class Student2(object):
    # __init__ 方法 第一个参数永远是self,表示创建的实例本身
    # __init__ 内部可以把各种属性绑定到self, 因为self 就是指向创建的实例本身
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def print_score(self):
        print('%s 的成绩是 %s' % (self.name,self.score))

# 类有__init__方法了，创建实例时 就不能传入空的参数，必须传入指定的参数，self 不需要
stu = Student2('lisi',99)

print(stu.name)
print(stu.score)
# 因为print_score 函数最后是print 而不是 return 所以这里不用print
stu.print_score()


# 类 是创建实例的模版
# 实例 是一个一个具体的对象， 各实例拥有的数据都互相独立
# 方法就是与实例绑定的函数，方法可以直接访问实例的数据
# Python 允许实例变量绑定任何数据
