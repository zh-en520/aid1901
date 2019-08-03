# insert_test.py
# 插入测试
import pymysql
from db_conf import *
#创建数据库连接
try:
    conn = pymysql.connect(host,user,passwd,dbname)
    cursor = conn.cursor() #获取游标
    #定义sql语句
    # sql = '''insert into orders
    # (order_id,cust_id,amt)
    # values('201801010002','C0002',444.55)
    # '''
    sql = 'delete from orders where amt=444.55'
    cursor.execute(sql)#执行SQL语句
    conn.commit()#提交事务
    print('插入成功')

except Exception as e:
    conn.rollback()#回滚事务
    print(e)
cursor.close()
conn.close()
