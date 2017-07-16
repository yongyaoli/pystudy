#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
操作文件和目录
'''

import os  
import sys
print(sys.version_info)
n = os.name
if n == 'nt':
    print('window system')
elif n=='posix':
    print('Linux / Unix / Mac OS X')
    print(os.uname())  # os.uname() 在window 上不支持
else:
    print('unkonw sytem')

print(os.uname())
print('---'*20)
# 环境变量
print(os.environ)
print('---'*20)
# print(os.environb)
# 获取某个环境变量的值
print('环境变量, USER:',os.environ.get('USER'))
print('环境变量, PATH:',os.environ.get('PATH'))

# 操作文件和目录
# 查看当前目录的绝对路径
print(os.path.abspath('.'))

# 指定目录下新建目录
# 先把新目录表示出来
np = os.path.join('/Users/liyongyao/work/python/pystudy', 'testdir') # 使用join 是为了兼容所有操作系统
print(np)
# os.mkdir(np) # 创建文件夹
# os.rmdir(np) # 删除文件夹
# 拆分路径
print(os.path.split('/Users/liyongyao/work/python/pystudy/testdir/red.txt'))

# 获取文件扩展名
print(os.path.splitext('/Users/liyongyao/work/python/pystudy/testdir/red.txt'))

# 重命名文件
#os.rename('/Users/liyongyao/work/python/pystudy/testdir/red.txt','/Users/liyongyao/work/python/pystudy/testdir/r.py')

# 删除文件
#os.remove('/Users/liyongyao/work/python/pystudy/testdir/r.py')



# 列出当前目录下的所有目录
l = [x for x in os.listdir('.') if os.path.isdir(x)]
print(l)

# 列出所有 .py文件
p =[x for x in os.listdir('.') if os.path.isfile(x) and os.path.split(x)[1]=='.txt']
print(p)