# myyield.py
# 此示例示意生成器函数的定义和调用方式

def myyield():
    print('即将生成２')
    yield 2
    print('即将生成３')
    yield 3     #这些都不执行
    print('生成器函数调用结束')

for x in myyield():
    print(x)

# g = myyield()  #g绑定的是一个生成器，生成器是可迭代对象
# print('g绑定的是：',g)

# it = iter(g) #it绑定g的迭代器
# v = next(it)
# print('v=',v)  # v = 2
# v2 = next(it)
# print('v2=',v2)


说明：
　生成器函数的调用将返回一个生成器对象，生成器对象是一个可迭代对象
　生成器函数调用return会触发一个StopTteration异常，(即生成数据结合)
示例２：
　myinteger.py