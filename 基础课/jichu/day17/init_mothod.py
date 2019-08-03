# 此示例示意初始化方法的定义方法方式和调用传参
# class Car:
#     '''小汽车类'''
#     def __init__(self,c,b,m):
#         self.color = c
#         self.brand = b
#         return [1,2,3]#初始化方法不能返回除Ｎone以外的其他属性
#         self.model = m
#         print('初始化方法被调用',c,b,m)

#     def run(self,speed):
#         print(self.color,'的',self.brand,self.model,'正在以',speed,'公里/小时的速度行驶')
# a4 = Car('红色','奥迪','A4')
# a4.run(233)
# a4.__init__('黑色','宝马','x5')
# print(dir(a4))