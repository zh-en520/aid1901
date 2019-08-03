import pymysql
import random

try:
    # 1. 连接数据库
	# 连接参数根据实际情况修改 
    conn = pymysql.connect("localhost", "root", "123456", "eshop")

    # 2. 获取游标
    cursor = conn.cursor()

    tmp = 0
    for i in range(1,100): # 空值插入多少笔数据
        tmp += 1
        order_id = "20180101%08d" % i   # 订单编号
        cust_id = "C%08d" % i   # 客户编号
        product_num = random.randint(1,5)   # 商品数量
        amt = product_num * 10    # 价格

        # 3. 执行SQL语句
        sql = ''' insert into orders 
        values('%s', '%s', now(), 1, %d, %.2f)
        ''' % (order_id, cust_id, product_num, amt)
        print(sql)
        cursor.execute(sql)
        if (tmp % 100 == 0):
            conn.commit()
    conn.commit()
    print("insert ok")
except Exception as e:
    print(e)
    conn.rollback()
finally:
    # 4. 关闭游标
    cursor.close()

    # 5. 关闭数据库连接
    conn.close()