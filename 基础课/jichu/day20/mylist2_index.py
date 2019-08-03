class Mylist:
    def __init__(self,iterable=()):
        self.data = [x for x in iterable]
    
    def __repr__(self):
        return 'Mylist(%s)'%self.data

    def __setitem__(self,i,v):
        self.data[i] = v
        return self.data

    def __getitem__(self,i):
        v = self.data[i]
        return v
    
    def __delitem__(self,i):
        self.data[i] = ''
        return self.data




L1 = Mylist([1,-2,3,-4,5])
x1 = L1[1]
print('x1=',x1)
L1[1] = 999
print('L1=',L1)
L2 = L1[::2]#L2.__getitem__(slice(None,None,2))
print('L2=',L2)