# -*- codeing = utf-8 -*-
# @Time : 2020/9/2211:27
# @Author : Shaye
# @File : testSqlite3.py
# @Sofeware : PyCharm

import sqlite3

# 轻便型数据库

conn = sqlite3.connect("database.db")    # 打开或创建数据库文件
print("Open database(数据库) successfully")


c = conn.cursor()   # 创建操作数据库对象
# 创建表
# sql0 = '''
#     create table company
#         (id int primary key not null ,
#          name text not null,
#          age int not null,
#          address char(50),
#          salary real);
# '''
# c.execute(sql0)   # 执行 sql 语句

# # 插入
# sql1 = '''
#     insert into company (id,name,age,address,salary)
#     values(1,"张三",25,"重庆",5000);
# '''
# sql2 = '''
#     insert into company (id,name,age,address,salary)
#     values (2,"李硕",22,"成都",8000);
# '''
# c.execute(sql1)   # 执行 sql 语句
# c.execute(sql2)   # 执行 sql 语句
#
# conn.commit()    # 提交 操作(创建表，插入数据需要提交操作，查询不需要)


# 查询
sql = '''
    select id,name,address,salary from company
'''
cursor = c.execute(sql)     # 存在返回值

for row in cursor:
    print(row)

conn.close()     # 关闭 数据库连接

print("successfully")


