class Mylist:
    def __init__(self,iterable=()):
        self.data = [x for x in iterable]
    
    def __repr__(self):
        return 'Mylist(%s)'%self.data

    def __neg__(self):
        lst = [-x for x in self.data]
        return Mylist(lst)

    def __pos__(self):
        lst = [abs(x) for x in self.data]
        return Mylist(lst)

L1 = Mylist([1,-2,3,-4,5])
L2 = -L1
L3 = +L1
print('L2=',L2)
print('L3=',L3)