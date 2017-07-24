#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
collections
python 内建的一个集合模块，提供了许多有用的集合
'''
from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import Counter

# namedtuple 
# tuple 表示不变的集合
# namedtuple用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用的某个元素

Point = namedtuple('Point', ['x', 'y'])
p = Point(2, 3)
print(p.x)
print(p.y)

print(isinstance(p, Point)) # true
print(isinstance(p, tuple)) # true

# namedtuple('名称),[属性list])

# deque 
# list 存储数据，索引访问元素很快，但是插入，删除很慢， 因为list是线性存储
#  deque 是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
print('---'*20)
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)
q.popleft() # 删除左侧的
print(q)
q.popleft() # 再次删除一个
print(q) 
q.pop()
print(q)

# defaultdict
# dict 引用的Key不存在，就抛出KeyError
# 如果希望key不存在时，返回一个默认值 可以使用defaultdict
print('--'*20)
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])
# ⚠️ 默认值是调用函数返回的，函数中创建defaultdict对象时传入
# 除了key不存在时返回默认值, defaultdict的其他行为跟dict是完全一样的

# OrderedDict
# dict key是无序的，如果保持key的顺序，可以用OrderedDict
print('--'*20)
d = dict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
print(d)
di = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(di)
# ⚠️ OrderedDict 的key 会按照插入的顺序排列，不是按key本身排序

# Counter
# Counter 事一个简单的计数器, 例如，统计字符出现的个数
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] +1

print(c)



