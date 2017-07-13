#！/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
__slots__
@property
'''


from types import MethodType

# python 是动态语言， 创建实例后 可以给该实例绑定任何属性和方法
class Student(object):
    pass

s = Student()
s.name = 'Liyy'  # 动态为实例绑定属性

print(s.name)

def set_age(self, age):  # 定义一个函数作为 实例方法
    self.age = age

s.set_age = MethodType(set_age, s)  #为一个实例绑定方法

s.set_age(19)

print('%s : %s' % (s.name,s.age))

# 给class 绑定方法，所有实例都拥有绑定方法
def set_score(self, score):
    self.score = score

Student.set_score = set_score  # 为class绑定方法。 为实例绑定方法（s.set_age = MethodType(set_age, s)）

print('==='*20)
print('使用__slots__ 可以限制实例的属性')

class Student2(object):
    __slots__ = ('age', 'name') # 使用tuple 定义允许绑定的属性名称


ss = Student2()
ss.name = 'Micke'
print(ss.name)

ss.age = 19
print(ss.age)

#ss.sex = 'F'
#print(ss.sex)

# __slots__  只对当前类有效，子类不起作用
class GraduateStudent2(Student2):
    pass

g = GraduateStudent2()
g.email = 'e@1.com'
print(g.email)

# 假如子类也声明__slots__  那么子类允许定义的属性就是自身的加父类的
class NewStudents(Student2):
    __slots__ = ('sex')

n = NewStudents()
n.sex ='F'
print(n.sex)
n.name ='zhang'
n.age =19
print(n.name, n.age)

#n.email ='bb@11.com'  # 报错 AttributeError: 'NewStudents' object has no attribute 'email'
# print(n.email)