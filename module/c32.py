#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib

'''
hashlib 通过了常见的摘要算法，eg: MD5, SHA1
'''
print('MD5--'*20)
m = hashlib.md5()
m.update('how to use md5 in python'.encode('utf-8'))

print(m.hexdigest())

# 如果数据量大，可以多次update(), 最后计算结果一样
mm = hashlib.md5() # 不能使用👆的m
mm.update('how to '.encode('utf-8'))
mm.update('use md5 '.encode('utf-8'))
mm.update('in python'.encode('utf-8'))
print(mm.hexdigest())

print('SHA1--'*20)
sh = hashlib.sha1()
sh.update('how to '.encode('utf-8'))
sh.update('use md5 '.encode('utf-8'))
sh.update('in python'.encode('utf-8'))
print(sh.hexdigest())

# SHA1的结果是160bit字节, 通常用一个40位的16进制字符串表示



