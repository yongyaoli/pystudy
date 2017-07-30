#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
'''
SQLAchemy: ORM框架
'''

# 创建对象的基类
Base = declarative_base()

# 定义User 对象
class User(Base):
    # 表名
    __tablename__ = 'ny_user'

    # 表结构
    id = Column(int, primary_key = True)
    username = Column(String(20))
    passwd = Column(String(20))

# 可以继续定义表

engine = create_engine('mysql+pymysql://root:rootroot@localhost:3306/ny_cms') 

# 创建DBSession类型
DBSession = sessionmaker(bind=engine)

session = DBSession()

new_user = User(username='zhangsan', passwd='admin888')
session.add(new_user)
session.commit()
session.close()


##AttributeError: type object 'int' has no attribute '_set_parent_with_dispatch'