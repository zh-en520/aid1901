class A:
    def work(self):
        print('A,被调用')
    
class B(A):
    def work(self):
        '''此方法会覆盖父类的work方法'''
        print('B,被调用')
    
    def mywork(self):
        '''此方法内能否调用自己的work方法,同时又调用父类的work方法'''
        self.work()
        super(B,self).work()#或super().work()


b = B()
b.work()

b.work()#如何等于'a被调用'???
A.work(b)#'A,被调用',不提倡这种方式,可能会出现无限循环
super(B,b).work()
print('---------------')
b.mywork()
# a = A()
# a.work()