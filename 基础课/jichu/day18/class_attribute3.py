class Car:
    total_count = 0#创建类属性，用来保存汽车的数量

#类属性可以通过此类的实例直接访问（取值不能赋值）
c1 = Car()#创建一个实例（对象）

# 类属性可以通过此类对象的'__class__'属性间接访问
c1.__class__.total_count = 888

print(c1.total_count)#888
print(Car.total_count)#888