#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
访问限制
继承，多态
'''
__author__ = 'Liyy'


# 类内部变量 名称修改为 _变量名，表示私有private
class Student(object):
    def __init__(self, name, score):
        self._name = name   # 初始化时赋值给私有变量
        self._score = score
    
    def print_score(self):
        print('%s:%s' % (self._name, self._score))
    
    def set_name(self,name):
        self._name = name

    def get_name(self):
        return self._name

    def set_score(self,score):
        if 0< score < 100:
            self._score = score
        else:
            raise ValueError('bad score')


st = Student('zhang',100)
st.print_score()

st.set_name('lisi')
st.print_score()


st.set_score(99)  # 通过自定义的函数 修改变量,赋值时会被检测
st.print_score()

#  直接赋值还是可以的，只不过不符合习惯
st._name ='king'
st.print_score()


# 双下划线开头，并且双下划线结尾 的变量 是特殊变量， 可以直接访问，不是private
# 一个下划线开头的是private ,不可访问，但是不强制
print('==='*20)
print('继承')

class Animal(object):
    def run(self):
        print('Animal is runing...')


class Dog(Animal):
    #pass
    def run(self):
        print('Dog is runing...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

v = Dog()
v.run()
c = Cat()
c.run()

# class 也是一个类型
print(isinstance(v, Animal))
print(isinstance(v, Dog))
print(isinstance(v, Cat))

b = Animal()
print(isinstance(b, Dog))

# 继承可以把父类的所有功能直接拿来用，不必重新做起
# 子类只需要新增资金特有的功能就可以， 也可以重写父类的方法
# 动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的

#动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子

