# order_manage.py
# 订单管理类
from db_oper import *
from order import *

class OrderManage:
    def __init__(self, db_oper):
        self.db_oper = db_oper  #实例化数据操作对象

    #根据订单号查询订单
    def query_by_id(self, order_id): 
        if not order_id:
            print("订单编号对象非法")
            return None
        if order_id == "":
            print("订单编号不能为空")
            return None
        
        sql = "select * from orders where order_id = '%s'" % order_id

        result = self.db_oper.do_query(sql)
        if not result:
            print("查询返回空对象")
            return None
        else:
            order_info = result[0]
            if not order_info:
                print("查询返回空对象")
                return None

            order_id = order_info[0]
            cust_id = order_info[1]
            
            if order_info[4]:
                products_num = int(order_info[4])
            else:
                products_num = 0

            if order_info[5]:
                amt = float(order_info[5])
            else:
                amt = 0.00

            return Order(order_id, cust_id, products_num, amt)

    # 查询所有订单
    def query_all_order(self):
        order_list = []
        sql = "select * from orders" 

        result = self.db_oper.do_query(sql)
        if not result:
            print("查询返回空对象")
            return None

        for order_info in result:
            order_id = order_info[0]
            cust_id = order_info[1]
            if order_info[4]:
                products_num = int(order_info[4])
            else:
                products_num = 0

            if order_info[5]:
                amt = float(order_info[5])
            else:
                amt = 0.00

            order_list.append(Order(order_id, cust_id, products_num, amt))

        return order_list

    # 新增订单
    def insert_order(self, order):  #插入对象
        sql = '''insert into orders(order_id, cust_id, products_num, amt) \
                 values('%s','%s',%d,%.2f)
        ''' % (order.order_id, order.cust_id, order.products_num, order.amt)
        print("\nsql:%s\n" % sql)
        result = self.db_oper.do_update(sql)
        print("执行结果，影响行数:%d" % result)
        return

    # 修改订单
    def update_order(self, order):
        sql = '''update orders \
                 set cust_id = '%s',
                     products_num = %d,
                     amt = %.2f
                where order_id = '%s'
        ''' % (order.cust_id, order.products_num, order.amt, order.order_id)
        print("\nsql:%s\n" % sql)
        result = self.db_oper.do_update(sql)
        print("执行结果，影响行数:%d" % result)
        return

if __name__ == "__main__":
    db_oper = DBOper()    #实例化数据访问对象
    db_oper.open_conn()   #打开数据库连接

    am = OrderManage(db_oper)  #实例化OrderManage对象

    # 根据订单编号查询
    # order = am.query_by_id("201801010001")
    # print(order)

    # 插入
    # new_order = Order("201801010012", "C0012", 7, 88.99)
    # am.insert_order(new_order)

    # 更新
    # new_order = Order("201801010012", "C0012", 6, 666666.66)
    # am.update_order(new_order)

    # 查询全部
    order_list = am.query_all_order()
    for a in order_list:
        print(a)

    db_oper.close_conn()


