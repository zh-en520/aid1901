# 此示例示意使用raise语句发送异常通知后进入异常流程，给调用者传递信息
# def make_except():
#     print('函数开始...')

#     # raise ValueError
#     error = ValueError('这是我故意制造的错误！')
#     raise error

#     print('函数结束！')
# try:
#     make_except()
#     print('make_except返回')
# except ValueError as err:
#     print('收到make_except 抛出错误信息！')
#     print('err=',err)


# print('程序结束')


def f1():
    print('f1开始')
    raise ValueError('f1里的错误')
    print('f1结束')

def f2():
    print('f2开始')
    try:
        f1()
    except ValueError as err:
        print('f1里发生了错误！err=',err)
        raise#等同于raise err
        print('f1结束')

try:
    f2()
except ValueError as err:
    print('f2里发生了错误，err=',err)
print('程序结束')