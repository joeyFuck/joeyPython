# 因为MySQLdb不支持python3,需要导入pymysql
# Connector/Python 只支持到python 3.4 这里用的是3.6所以官网或pip安装mysql python useless
import pymysql.cursors

conn = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='lovemary',
    db='test',
    charset='utf8'
)
# 获取游标
cursor = conn.cursor()
# 创建user表:
cursor.execute('create table person (id varchar(20) primary key, name varchar(20))')

# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into person (id, name) values (%s, %s)', ['1', 'Michael'])
print(cursor.rowcount)
# 提交事务:
conn.commit()
cursor.close()

# http://www.cnblogs.com/bincoding/p/6789456.html






























