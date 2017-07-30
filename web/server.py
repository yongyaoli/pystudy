#! /usr/bin/env python3
#-*- coding: utf-8 -*-

# 从wsgiref 模块导入
from wsgiref.simple_server import make_server
# 导入自己写的application函数
from hello import application


httpd = make_server('',8000, application)
print('Serving HTTP on port 8000....')

# 开始
httpd.serve_forever()
