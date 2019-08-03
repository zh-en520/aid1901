# order.py
# 订单类,接收数据库中订单记录的值
class Order:
    def __init__(self,order_id,cust_id,amt):
        self.order_id = order_id
        self.cust_id = cust_id
        self.amt = amt
    
    def __str__(self):#重写__str__方法
        ret = '订单号:%s,客户:%s,金额:%.2f'\
            %(self.order_id,self.cust_id,self.amt)
        return ret