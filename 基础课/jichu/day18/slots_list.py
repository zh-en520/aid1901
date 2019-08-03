# 此示例示意类的__slots__属性的作用
class Human:
    #限定Human类型的对象只能有name和age实例属性
    __slots__ = ['name','age']
    def __init__(self,n,a):
        self.name = n
        self.age = a
    
    def show_info(self):
        print(self.name,'今年',self.age,'岁')
    
h1 = Human('Tarena',17)
h1.show_info()#17
h1.Age = 18#报错
h1.show_info()#17