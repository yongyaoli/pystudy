#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# 导入sqlite3 驱动
import sqlite3
'''
sqllite
'''

# 链接demo.db，如果不存在就会自动创建
conn = sqlite3.connect('demo.db')
# 创建一个cursor(游标)
cursor = conn.cursor()
# 执行一个创建user表的sql
#sql = 'create table user(id int primary key, name varchar(20))'
#cursor.execute(sql)

# 执行一个插入数据的sql
cursor.execute('insert into user(id, name) values (5, \'mazi\')')
# 通过rowcount 获得插入的行数
rc = cursor.rowcount
print(rc)
# 关闭游标
cursor.close()
# 提交事务
conn.commit()
# 关闭连接
conn.close()

c = sqlite3.connect('demo.db')
cc =c.cursor()
# 删除一个
cc.execute('delete from user where id=?' ,('2'))
rrc = cc.rowcount
print('删除id 为1的 %s' %(rrc))
# 修改一个
cc.execute('update user set name =? where id=?',('xxx','3'))
rrc2 = cc.rowcount
print('修改')
cc.execute('select * from user');
v = cc.fetchall()
print(v)
cc.close()
c.close()
