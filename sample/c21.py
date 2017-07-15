#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
1.多重继承：
class myclass(父类1, 父类2)
多重继承 取的是 最近的那个父类的方法
2.定制类

'''

class Animal(object):
    def say(self):
        print('我是动物')

class Mammal(Animal):
    def say(self):
        print('我是哺乳动物')

class Bird(Animal):
    def say(self):
        print('我是鸟类')


class Runnable(object):
    def run(self):
        print('running....')

class Flyable(object):
    def fly(self):
        print('Flying....')


class Dog(Mammal,Runnable):
    def say(self):
        print('我是狗狗')

class Parrot(Bird,Flyable):
    def say(self):
        print('我是鹦鹉')


d = Dog()
d.say()
d.run()

p = Parrot()
p.say()
p.fly()
print('---'*20)
print('定制类: 1.__str__  类说明')

class Student(object):
    def __init__(self,name):
        self.name = name
    # 返回给用户看到的字符串
    def __str__(self):
        return 'This is Student,name:%s' % self.name
    # 给程序看的，调试服务用的  s = Student(),在交互式环境下输入 s 显示的
    # 简约的写法 __repr__ = __str__
    def __repr__(self):
        return 'This is repr'
print(Student('Jack'))
s = Student('Tom')
print(s)

# __iter__  是一个函数可以用于 for...in 循环， __next__()

class Fib:
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器
    # python3  好像不再使用 __next__  而是使用next
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 10000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值
    # python3 使用 next 替代 __next__
    def next(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration
        return self.a

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己
    
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a +b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
         
fib = Fib()
for n in fib:
    print(n)

print(fib[0])
print(fib[1])
print(fib[2])
print(fib[3])
print(fib[10])
print(fib[100])


print(fib[0:5])
print(fib[:10])
print(fib[:10:2])

# __getattr__

class Stu:
    def __init__(self):
        self.name = 'Liyy'
    def __getattr__(self, attr):
        if attr == 'score': # 如果是获取没有的属性 score  就返回99
            return 99
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
s = Stu()
print(s.name)
print(s.score)
# print(s.sex)

# REST API, __getattr__ 的链式调用
class Chain:
    def __init__(self, path=''):
        self._path = path
    
    def __getattr__(self, path):
        return Chain('%s/%s' %(self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().status.user.time.list)
# print(Chain().users('mick').respos)

# 定义__call__() ,可以直接对实例进行调用
class MyClass:
    def __init__(self, name):
        self._name = name
    
    def __call__(self,s=''):
        print('My is %s. %s' % (self._name, s))

m = MyClass('Tom')
m()
m('zzzzz')

print(callable(MyClass('zhang')))
print(callable([1, 2 ,3]))
print(callable(None))
print(callable('str'))
# https://docs.python.org/3/reference/datamodel.html#special-method-names
# python 官方文档


