#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.parse
import urllib.request
from bs4 import BeautifulSoup 
import os
import time
#import sys  
#sys.setdefaultencoding('utf-8')  #输出的内容是utf-8防止出现编码问题， python3 已解决此问题

#http://www.dbmeinv.com/dbgroup/show.htm?cid=2
url = 'http://www.dbmeinv.com/dbgroup/show.htm?cid=2&pager_offset=2'

def getpic(url):
    '''
        获取豆瓣妹子图
    '''
    header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.7 Safari/537.36"}

    req = urllib.request.Request(url,headers=header)
    response = urllib.request.urlopen(req, timeout = 20)
    d = response.read()
    ch_d= d.decode('utf-8')
    soup = BeautifulSoup(ch_d,'html.parser')
    #print(soup.img) # 输出一个
    girls = soup.find_all('img')
    for i in girls:
        full_path = i.get('src')
        print(full_path[(full_path.rfind('/')+1):]) # 截取文件的文件名
        path =('%s\\img\\img%s.jpg'%(os.path.split(os.path.realpath(__file__))[0],full_path[(full_path.rfind('/')+1):])) #文件保存路径
        urllib.request.urlretrieve(full_path, path)
        print("正在下载%s..."%i.get('src'))


if __name__ == '__main__':
    #getpic(url)
    for p in range(1,5):
        p+=1
        url='http://www.dbmeinv.com/dbgroup/show.htm?cid=2&pager_offset=%s'%p
        getpic(url)
    print("下载完成!")
