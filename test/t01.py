#! /usr/bin/python
# -*- coding:utf-8 -*-

import urllib2

url='http://www.baidu.com/s?wd=test'
req=urllib2.Request(url)
res=urllib2.urlopen(req).read()
print(res)