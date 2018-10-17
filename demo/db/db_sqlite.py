'''
SQLite是一种嵌入式数据库，它的数据库就是一个文件 　
由于SQLite本身是C写的，而且体积很小
经常被集成到各种应用程序中，甚至在iOS和Android的App中都可以集成
在Python中使用SQLite，不需要安装任何东西，直接使用。
'''


'''
游标是一段私有的SQL工作区,也就是一段内存区域,用于暂时存放受SQL语句影响到的数据。
通俗理解就是将受影响的数据暂时放到了一个内存区域的虚表中，而这个虚表就是游标
'''


'''
操作关系数据库
1.首先需要连接到数据库，一个数据库连接称为Connection；
2.连接到数据库后，需要打开游标，称之为Cursor，通过Cursor执行SQL语句
'''

'''
import  sqlite3
# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('test.db')
# 创建一个Cursor:
cursor = conn.cursor()
# 执行一条SQL语句，创建user表:
cursor.execute('create  table user (id varchar(20) primary key,name varchar(20)  )')
# 继续执行一条SQL语句，插入一条记录:
cursor.execute('insert into user (id, name) values(1,"test")')
# 通过rowcount获得插入的行数:
print(cursor.rowcount)
# 关闭Cursor:
cursor.close()
# 提交事务:
conn.commit()
# 关闭Connection:
conn.close()
'''

'''
sqlite查询
'''

import  sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('select * from user where id=1')
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()

'''
使用Python的DB-API时，只要搞清楚Connection和Cursor对象，打开后一定记得关闭，就可以放心地使用。

使用Cursor对象执行insert，update，delete语句时，执行结果由rowcount返回影响的行数，就可以拿到执行结果。

使用Cursor对象执行select语句时，通过featchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录。

'''