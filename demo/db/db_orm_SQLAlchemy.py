'''
ORM：
Object-Relational Mapping，把关系数据库的表结构映射到对象上
'''

# 导入:
from  sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'test'
    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接:
# 数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名
engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/gpi')

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建数据库操作会话
sess = DBSession()

# 插入数据
new_user = User(id='7', name='sqlalchemy')
sess.add(new_user)
sess.commit()

# 查询
sess = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = sess.query(User).all()

print(user)
sess.close()


# 如果一个User拥有多个Book，就可以定义一对多关系如下：
#
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
# 当我们查询一个User对象时，该对象的books属性将返回一个包含若干个Book对象的list
