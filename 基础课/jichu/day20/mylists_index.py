class Mylist:
    def __init__(self,iterable=()):
        self.data = [x for x in iterable]
    
    def __repr__(self):
        return 'Mylist(%s)'%self.data

    def __setitem__(self,i,v):
        self.data[i] = v
        return self.data

    def __getitem__(self,i):
        print('i=',i)
        if type(i) is int:
            print('正在做索引操作')
        elif type(i) is slice:
            print('正在做切片操作')
            print('起始值',i.start)
            print('终止值',i.stop)
            print('步长',i.step)
        v = self.data[i]
        return v
    
    def __delitem__(self,i):
        self.data[i] = ''
        return self.data




L1 = Mylist([1,-2,3,-4,5])
x1 = L1[::2]
print('x1=',x1)
# L1[1] = 999
# print('L1=',L1)
# del L1[1]
# print('L1=',L1)
