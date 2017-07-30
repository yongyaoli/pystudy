#! /usr/bin/env python3
#-*- coding: utf-8 -*-

# python3 下使用的是 pymysql3
import pymysql

'''
mysql
'''

try:
    #链接mysql
    conn = pymysql.connect(host='localhost', user='root', passwd='rootroot', db='ny_cms', port=3306, charset='utf8')
    # 获取游标
    cur = conn.cursor()
    
    #cur.execute('select * from ny_users')
    #print('test:%s'% (cur.rowcount))

    #cur.execute('create table if not exists ny_users(id int primary key auto_increment,username varchar(20),passwd varchar(20))')
    r = cur.rowcount
    if r>0:
        print('创建表ny_users成功')
    else:
        print('创建表ny_users失败')
    # 注意 参数写法， 参数占位符是%s;   后方参数使用的是[]
    cur.execute('insert into ny_user(username,passwd) values(%s,%s)',['user','123456'])
    print(cur.rowcount)
    #千万不可忘记提交
    conn.commit()  # 千万不可忘记提交
    # 千万不可忘记提交
    # 执行insert 等操作后要调用commit() 提交事务
    cur.execute('select * from ny_user')
    da = cur.fetchall()
    print(da)

    cur.close()
    conn.close()
except Exception as e:
    print(e)