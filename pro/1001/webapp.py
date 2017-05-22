#! /usr/bin/env python3
# -*- coding:utf-8 -*-
import web
import os

#import platform 

#print(platform.python_version())  # 输出python版本
"""
使用Web.py 框架开发电影下载网站
"""
__author__ = "Liyy"

urls = (
    '/', 'hello', # hello 是一个类，对应下方的class hello
    '/page/list_(\d+).html','hello',
    '/movie/(\d+).html','movieinfo'
)
root = os.path.dirname(__file__)
#print(os.path.join(root,'templates/'))

render = web.template.render(os.path.join(root,'templates/'))

dbb = web.database(dbn='mysql', host='127.0.0.1', port=3306, user='root', pw='root', db='33hao', charset="utf8")

#render = web.template.render()

app = web.application(urls, globals())

class hello:
    def GET(self,page=1): #函数名是该请求的请求方式
        page = int(page)
        data = dbb.query("select * from 33hao_article where article_id limit %d,%d"%((page-1)*15,15))
        #print(data[0]["article_title"])
        #return render.index(data[0]["article_title"])
        return render.index(data)


class movieinfo:
    def GET(self,id): 
        data = dbb.query("select * from 33hao_article where article_id=%s"%id)[0]
        print(data)
        print(data.article_title)
        return render.movie(data)

if __name__ == "__main__":
    app.run()

