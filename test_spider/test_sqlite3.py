import sqlite3


# '''
# conn=sqlite3.connect("test.db")   #打开或创建数据库文件
#
# c=conn.cursor()   #获取游标
#
#
#
# sql = '''
#       create table company
#       (id int primary key not null,
#       name text not null,
#       age int not null,
#       address char(50),
#       salary real);
#
#
# '''
#
#
#
#
# c.execute(sql)    #执行sql语句
# conn.commit()     #提交数据库操作
# conn.close()      #关闭数据库连接
#
#
# print("Opend database successfully")
#
# '''

# #插入数据
# conn=sqlite3.connect("test.db")   #打开或创建数据库文件
#
# c=conn.cursor()   #获取游标
#
#
#
# sql1 = '''
#     insert into company(id,name,age,address,salary)
#     values(1,"张三",32,"成都",8000);
#
# '''
#
# sql2 = '''
#     insert into company(id,name,age,address,salary)
#     values(2,"李四",32,"重庆",80000);
#
# '''
#
#
#
#
# c.execute(sql1)    #执行sql语句
# c.execute(sql2)
# conn.commit()     #提交数据库操作
# conn.close()      #关闭数据库连接



#查询数据

conn=sqlite3.connect("test.db")   #打开或创建数据库文件

c=conn.cursor()   #获取游标



sql = "select id,name,address,salary from company"




cursor=c.execute(sql)    #执行sql语句

for row in cursor:
    print("id = ",row[0])
    print("name = ", row[1])
    print("address = ", row[2])
    print("salary = ", row[3],"\n")


conn.close()      #关闭数据库连接