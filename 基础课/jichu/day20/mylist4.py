class Mylist:
    def __init__(self,iterable=()):
        self.data = [x for x in iterable]
    
    def __repr__(self):
        return 'Mylist(%s)'%self.data

    def __neg__(self):
        lst = [-x for x in self.data]
        return Mylist(lst)

    def __contains__(self,e):
        # print('__contains__')
        return e in self.data


L1 = Mylist([1,-2,3,-4,5])
print(3 in L1) #???
print(3 not in L1)
print(100 in L1)
print(100 not in L1)