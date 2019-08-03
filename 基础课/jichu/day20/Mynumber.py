# 此示例示意自定义的类,添加相应方法,让此类的对象能够使用运算符进行操作
class Mynumber:
    def __init__(self,value):
        self.data = value
    
    def __repr__(self):
        return 'Mynumber(%s)'%self.data

    def __add__(self,other):
        v = self.data + other.data
        return Mynumber(v)

    def __sub__(self,rhs):
        s = self.data - rhs.data
        return Mynumber(s)
    
    def __mul__(self,rhs):
        l2 = self.data * rhs
        return Mynumber(l2)

    def __rmul__(self,lhs):
        l = self.data * lhs
        return Mynumber(l)


l1 = Mynumber([1,2,3])
n1 = Mynumber(100)
n2 = Mynumber(200)
# n3 = n1.__add__(n2)
# n3 = n1 + n2#等同于n3=n1.__add__(n2)
# print(n1,'+',n2,'=',n3)

n4 = n1 - n2
print(n1,'-',n2,'=',n4)
n5 = l1 * 2
print('n5=',n5)
l3 = 2*l1
print('l3=',l3)