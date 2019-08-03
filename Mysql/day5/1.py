# query_test.py
# 查询示例
# 1)导入pymysql
import pymysql
from db_conf import *
conn = pymysql.connect(host,user,passwd,dbname)
#3)创建游标对象
cursor = conn.cursor()
#4)使用游标对象提供的方法,执行SQL语句
sql = 'select * from orders'
cursor.execute(sql)
result = cursor.fetchall()
#5)提交事务(如果需要)
#6)打印数据
for r in result:
    order_id = r[0]
    cust_id = r[1]
    if not r[5]:
        amt = 0
    else:
        amt = r[5]
    print('订单编号:%s,客户编号:%s,金额:%.2f'\
        %(order_id,cust_id,amt))
#7)关闭游标
cursor.close()
#8)关闭数据库连接对象
conn.close()