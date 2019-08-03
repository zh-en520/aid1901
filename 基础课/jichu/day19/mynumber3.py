class Mynumber:
    def __init__(self,v):
        self.data = v

    def __float__(self):
        '''此方法必须返回浮点数'''
        return float(self.data)
n1 = Mynumber('100')
f1 = float(n1)
print(f1)