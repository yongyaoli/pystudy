#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
操作文件和目录
'''

import os 
n = os.name
if n == 'nt':
    print('window system')
elif n=='posix':
    print('Linux / Unix / Mac OS X')
    print(os.uname())  # os.uname() 在window 上不支持
else:
    print('unkonw sytem')

print(os.uname())