#! /usr/bin/env python3
# -*- coding:utf-8 -*-
import sys,os
from bs4 import BeautifulSoup
#1.如何去获取标签里的内容
html = "<h3>没有</h3>"
soup = BeautifulSoup(html, 'html.parser') #创建对象，解析网页

print(soup.h3) # 对象直接加 标签名称就可以获取标签及标签内容
print("----"*20)
# 如何获取文件的内容
file = os.path.split(os.path.realpath(__file__))[0]+'\\a.html' # 获取文件
# open('a.html') UnicodeDecodeError: 'gbk' codec can't decode byte 0x80 in position 205: illegal multibyte sequence
# 解决办法： 1.open(file,'r', encoding='UTF-8') 2.open(file,'rb')
soup2 = BeautifulSoup(open(file, 'rb'), 'html.parser')
print(soup2.prettify())

#2:  字符串格式化:%s, format
print("http://baidu.com/?s=%s"%'2')
print('http://baidu.com/?s={}'.format(2))




#url = "http://www.dbmeinv.com/?pager_offset="


