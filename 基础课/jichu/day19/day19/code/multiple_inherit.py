# multiple_inherit.py

# 此示例示意多继承的语法和用法
class Car:
    def run(self, speed):
        print("汽车以", speed, '公里/小时的速度行驶')
    
class Plane:
    def fly(self, height):
        print("飞机以海拔", height, '米的高度飞行')

class PlaneCar(Car, Plane):
    '''PlaneCar为飞行汽车类'''

p1 = PlaneCar()
p1.fly(10000)
p1.run(300)











