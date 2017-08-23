# 可见，ORM就是把数据库表的行与相应的对象建立关联，互相转换。
#
# 由于关系数据库的多个表还可以用外键实现一对多、多对多等关联，相应地，ORM框架也可以提供两个对象之间的一对多、多对多等功能。
#
# 例如，如果一个User拥有多个Book，就可以定义一对多关系如下：


# class User(Base):
#     __tablename__ = 'user'
#
#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))
#     # 一对多:
#     books = relationship('Book')
#
# class Book(Base):
#     __tablename__ = 'book'
#
#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))
#     # “多”的一方的book表是通过外键关联到user表的:
#     user_id = Column(String(20), ForeignKey('user.id'))


# 当我们查询一个User对象时，该对象的books属性将返回一个包含若干个Book对象的list。






