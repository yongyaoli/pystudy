#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
python 3.4 之后 
urllib 和 urllib2合并为urllib 
引用修改为urllib.request
http://www.111cn.net/phper/python/68713.htm
"""
import urllib.parse
import urllib.request

url='http://www.baidu.com/s?wd=test'
req=urllib.request.urlopen(url).read()
res = req.decode('UTF-8')
print(res) 


# 添加headers 请求 模仿浏览器访问
header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.7 Safari/537.36"}
req = urllib.request.Request(url,headers=header)

print("---"*30)
url = 'http://mail.163.com/'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {
'act' : 'login',
'login[email]' : 'yzhang@i9i8.com',
'login[password]' : '123456'
}
data = urllib.parse.urlencode(values)
req = urllib.request.Request(url, data)
req.add_header('Referer', 'http://www.python.org/')
response = urllib.request.urlopen(req)
the_page = response.read()
print(the_page.decode("utf8"))