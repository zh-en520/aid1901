#实例属性不能直接对取值和赋值加以控制
class Student:
    def __init__(self,s):
        self.score = s

s1 = Student(59)
scr = s1.score#取值
print('成绩是:',scr)
s1.score = 99999#赋值
print('成绩是:',s1.score)