# mymod3.py
此示例示意模块内__all__列表的用法和作用
__all__ = ['f','name1']#此列表限制from mymod2 import *只导入f 和 name1
def f1():
    pass

def f2():
    pass

def f():
    f1()
    f2()

name1 = 'aaaa'
name2 = 'bbbb'