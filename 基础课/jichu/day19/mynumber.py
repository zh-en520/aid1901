class Mynumber:
    def __init__(self,v):
        self.data = v
    
    def __str__(self):
        print('__str__方法被调用')
        s = '数字:'+str(self.data)
        return s

    def __repr__(self):
        '''此方法必须返回能让eval执行的字符串'''
        s = 'Mynumber(%d)'%self.data
        return s
n1 = Mynumber(100)
print('repr(n1)=',repr(n1))
print('str(n1)=',str(n1))