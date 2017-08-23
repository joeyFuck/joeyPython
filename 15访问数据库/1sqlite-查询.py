import sqlite3
conn = sqlite3.connect('../sql/sqlite/test.db')
cursor = conn.cursor()
# 执行查询语句
cursor.execute('SELECT id,name from user')
# 获取执行结果集
values = cursor.fetchall()
print(values)



















