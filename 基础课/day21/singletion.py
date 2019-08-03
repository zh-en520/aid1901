class Singleton:
    '''单例模式'''
    __instance = None #用于绑定实例
    def __new__(cls,*args):
        if cls.__instance is None: #说明没有实例

            cls.__instance = object.__new__(cls)
            print('正在创建新的实例',cls.__instance)
        return cls.__instance
    def __init__(self,*args):
        print('初始化方法被调用')

s1 = Singleton()
print('s1=',s1)
s2 = Singleton()
print('s1=',s2)