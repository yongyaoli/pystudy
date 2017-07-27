#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from contextlib import contextmanager
from contextlib import closing
from urllib.request import urlopen

# 读写文件，必须使用完毕后正确关闭
# 方法1
try:
    f = open('/users/liyongyao/work/python/pystudy/notice.txt', 'r',encoding='utf-8')
    print(f.name)
    c = f.read()
    print(c)
finally:
    if f:
        f.close()
        
print('--'*20)
# 方法2
with open('/users/liyongyao/work/python/pystudy/notice.txt', 'r', encoding='utf-8') as f:
    print(f.name)
    print(f.read())


# 任何对象 只要实现了上下文管理，就可以用于with语句

class Query:
    def __init__(self, name):
        self.name = name
    
    def query(self):
        print(' query is a %s...' % self.name)

@contextmanager
def create_query(name):
    print('begin')
    q = Query(name)
    yield q
    print('end')

with create_query('Bob') as q:
    print(q.query())


# 如果一个对象没有实现上下文，可以使用closing()把对象变为上下文对象
 
with closing(urlopen('http://www.baidu.com')) as f:
    for i in f:
        print(i)