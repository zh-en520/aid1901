class A:
    def m(self):
        print('A.m被调用')

class B:
    def m(self):
        print('B.m被调用')
#小王感觉小张和小李写的两个类自己都可以用
class AB(A,B):
    pass

ab = AB()
ab.m()#请问调用谁