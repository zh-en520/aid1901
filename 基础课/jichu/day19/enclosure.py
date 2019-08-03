class A:
    def __init__(self,v):
        self.__money__ = v
    
    def buy(self,obj,m):
        self.__money__ -= m
        print('买',obj,'花了',m,'元,剩余',self.__money__,'元')
        #调用自己的私有方法
        self.__m()

    def __m(self):
        print('这是a类对象的私有实例方法')
a = A(1000)
a.buy('电子书',600)
a.money = 0
a.buy('耳机',100)
a.__m()#出错,私有实例方法不能在类的外部调用