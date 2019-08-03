# 此示例示意在自定义的类内添加__len__方法和__bool__方法
# 能让自定义的类用内建函数len和bool进行操作
class MyList:
    def __init__(self,iterable=()):
        self.data = [x for x in iterable]

    def __repr__(self):
        s =  'MyList(%s)' % self.data
        return s
    
    # def __len__(self):
    #     '''此方法必须返回整数'''
    #     return len(self.data)
    def __bool__(self):
        return len(self.data) != 0
        
    
    
myl1 =  MyList([1,-2,3,-4])
myl2 = MyList()
print(bool(myl1))
print(bool(myl2))
