#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
python 3.4 之后 
urllib 和 urllib2合并为urllib 
引用修改为urllib.request
"""

import urllib.request

url='http://www.baidu.com/s?wd=test'
req=urllib.request.urlopen(url).read()
res = req.decode('UTF-8')
print(res) 
