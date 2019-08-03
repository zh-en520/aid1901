
class A:
    def work(self):
        print("A.work被调用")

class B(A):
    def work(self):
        '''此方法会覆盖父类的work方法'''
        print("B.work被调用!!!!")
    pass

b = B()
b.work()  # B.work被调用
A.work(b)  # A.work被调用





