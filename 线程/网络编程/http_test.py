from socket import *

#创建套接字
s = socket()
s.bind(('0.0.0.0',8800))
s.listen(5)

#接收浏览器请求
c,addr = s.accept()
print('Connect from',addr)
data = c.recv(4096)
print(data)

data = '''HTTP/1.1 200 OK
# Content-Encodeing:gzip
Content-Type:text/html

<h1>Hello world</h1>
'''
c.send(data.encode())

c.close()
s.close()