#! /usr/bin/env python3
# -*- coding:utf-8 -*-
'''
序列化
'''
# 需要引入 pickle 模块
import pickle
# JSON
import json

# 声明一个字典
d = dict(name='zhangsan', age=20, score=90)

f = open('dump.txt', 'wb')
#  pickle.dumps()把任意对象序列化一个bytes
# j = pickle.dumps(d)
pickle.dump(d, f) # 返回None
f.close()

# 读取文件
ff = open('dump.txt', 'rb')
dd = pickle.load(ff)
ff.close()
print(dd)

# json.dumps() 返回一个标准的JSON
jd = dict(name='Bob', age=20, score=88)
#nj = json.dumps(jd)
# print('JSON dumps:', nj)

jf = open('json.txt','w') # 使用wb 方式：TypeError: a bytes-like object is required, not 'str'
tms = json.dump(jd, jf)
# print(tms)

# 读取JSON字符串并反序列化
#n = json.loads(nj)
#print('读取JSON:',n)

jf = open('json.txt','rb')
nnj = json.load(jf)
print('文件里读取JSON，',nnj)


# json 序列号class

class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('zhangsan', 19, 99)  # 实例化一个class
jj = json.dumps(s, default= lambda obj: obj.__dict__) # 实例转化为 json
# ⚠️ 注意 定义__slots__的class 是没有__dict__属性的
print(jj)

# 反序列化
# 需要先定义一个函数， 传入dict
def dict2stu(d):
    return Student(d['name'], d['age'], d['score']) # 实例化一个class 然后返回
json_s ='{"name": "zhangsan", "age": 19, "score": 99}'
strs = json.loads(json_s, object_hook=dict2stu)
print(strs)

