# 此示例示意钻石继承的方法
class A:
    def go(self):
        print('A')
    
class B(A):
    def go(self):
        print('B')

class C(A):
    def go(self):
        print('C')

class D(B,C):
    def go(self):
        print('D')
        super().go()#super(D,self).go()

for cls in D.__mro__:
    print(cls)
print('D.__mro__:',D.__mro__)
d = D()
d.go()    
