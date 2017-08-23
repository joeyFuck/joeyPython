#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a test module"""

__author__ = 'Joey zhu'

# 数据库表是一个二维表，包含多行多列。把一个表的内容用Python的数据结构表示出来的话，可以用一个list表示多行，
# list的每一个元素是tuple，表示一行记录，比如，包含id和name的user表：
# [
#     ('1', 'Michael'),
#     ('2', 'Bob'),
#     ('3', 'Adam')
# ]
# 但是用tuple表示一行很难看出表的结构。如果把一个tuple用class实例来表示，就可以更容易地看出表的结构来：
# class User(object):
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
#
# [
#     User('1', 'Michael'),
#     User('2', 'Bob'),
#     User('3', 'Adam')
# ]
# 这就是传说中的ORM技术：Object-Relational Mapping，把关系数据库的表结构映射到对象上。

# 在Python中，最有名的ORM框架是SQLAlchemy。我们来看看SQLAlchemy的用法。

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class Person(Base):
    # 表的名字:
    __tablename__ = 'person'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接:
engine = create_engine('mysql+pymysql://root:lovemary@localhost:3306/test?charset=utf8') # 为了支持中文，?charset=utf8
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
# create_engine()用来初始化数据库连接。SQLAlchemy用一个字符串表示连接信息：
# '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
# 新增
# 创建session对象:
session = DBSession()
# 创建新User对象:
new_person = Person(id='6', name='中文')
# 添加到session:
session.add(new_person)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()
























