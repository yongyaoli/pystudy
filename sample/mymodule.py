#! /usr/bin/env python
# -*- coding:utf-8 -*-

# 文件的第一个字符串是 模块的说明文档
' this is a module demo [这是一个测试模块]'
# __author__ 指定 文档作者
__author__ = 'Liyy'
# 引入sys 模块
import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('your len is 1, %s' % args[0])
    elif len(args) == 2:
        print('your len is 2, sec:%s' % args[1])
    else:
        print('your len is  long')

# if __name__ == '__main__' 表示
# 只有在命令行运行本模块 ，特殊变量__name__ 的值才是 __main__
if __name__ == '__main__':
    test()
