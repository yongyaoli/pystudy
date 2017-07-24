#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import struct

'''
struct
用来解决bytes 和其他二进制数据类型的转换
'''

# python 中 b'str'可以表示字节

b = struct.pack('>I', 10240099)
print(b)
# pack的第一个参数是处理指令
# >I ： >表示字节顺序是big-endian, 也就是网络序,I表示4字节无符号整数
#  后面的参数个数要和处理指令一致


#struct模块定义的数据类型可以参考Python官方文档：
#https://docs.python.org/3/library/struct.html#format-characters


