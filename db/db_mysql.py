'''
mysql 数据库

MySQL是Web世界中使用最广泛的数据库服务器。
SQLite的特点是轻量级、可嵌入，但不能承受高并发访问，适合桌面和移动应用。
MySQL是为服务器端设计的数据库，能承受高并发访问，同时占用的内存也远远大于SQLite。
'''

'''
pip3 install mysql-connector-python --allow-external mysql-connector-python
'''

# 导入MySQL驱动:
import mysql.connector

# 连接数据库
conn = mysql.connector.connect(user='root',password='root',database='gpi')
cursor = conn.cursor()

# 创建表:
cursor.execute('create table test  ( id varchar(20) primary key, name varchar(20)　) ')

# 添加数据
cursor.execute('insert into test (id, name) values ("1", "user") ')
print(cursor.rowcount)

# 提交事务
conn.commit()
cursor.close()

# 查询
cursor = conn.cursor()
cursor.execute('select * from test ')
print(cursor.fetchall())
cursor.close()
conn.close()

'''
如果MySQL的版本≥5.5.3，可以把编码设置为utf8mb4
utf8mb4和utf8完全兼容，但它支持最新的Unicode标准，可以显示emoji字符。
执行INSERT等操作后要调用commit()提交事务；
MySQL的SQL占位符是%s
'''