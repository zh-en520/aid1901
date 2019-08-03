#创建套接字对象

from socket import *

s = socket()

#设置端口立即重用
# s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
print(s.getsockopt(SOL_SOCKET,SO_REUSEADDR))

s.bind(('192.168.43.208',8888))
s.listen(3)


print(s.family)#地址类型
print(s.type)#套接字类型

print(s.getsockname())#获取绑定地址addr

print(s.fileno()) #文件描述符


c,addr = s.accept()
print(c.getpeername())#获取连接套接字客户端地址