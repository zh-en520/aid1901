# 1.修改原学生信息管理系统的Student类,封装学生类对象的姓名,年龄,成绩,不让除此对象的方法之外
# 的语句来访问学生类的实例属性

# 2.实现一个与系统内建的range类相同功能的类
class MyRange:
    def __init__(self,start,stop=None,step=None):
        if stop is None:
            self.start = 0
            self.stop = start
        else:
            self.start = start
            self.stop = stop
        if step is None:
            self.step = 1
        else:
            self.step = step
    
    def __repr__(self):
        return 'MyRange(%d,%d,%d)'%(self.start,self.stop,self.step)
    def __iter__(self):
        return MyRangeIterator(self.start,self.stop,self.step)

class MyRangeIterator:
    def __init__(self,start,stop,step):
        self.start = start
        self.stop = stop
        self.step = step
        self.cur_value = start#这是第一次要生成的值
    
    def __next__(self):
        if self.step > 0 :
            if self.cur_value >= self.stop:
                raise StopIteration
            r = self.cur_value
            self.cur_value += self.step
            return r
        if self.step < 0:
            if self.cur_value <= self.stop:
                raise StopIteration
            r = self.cur_value
            self.cur_value += self.step
            return r
#测试调用如下:
L = list(MyRange(5))
print(L) #[0,1,2,3,4]
print(sum(MyRange(1,101)))#5050
L2 = [x**2 for x in MyRange(1,10,3)]
print(L2)#[1,16,49]
for x in MyRange(10,0,-3):
    print(x) #打印10,7,4,1