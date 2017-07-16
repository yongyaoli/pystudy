#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
常用零碎功能：
1. 输出python 版本
2. 获取当前文件路径
'''
import sys
import os
# 1. 输出python 版本
print(sys.version) # 简略信息
print(sys.version_info) # 详细信息

# 2. 获取当前文件路径
print(os.path.abspath(__file__)) # 绝对路径， 加文件名
print(os.path.split(os.path.realpath(__file__))[0])


