from select import *
from socket import *

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(3)

p = epoll()

#建立查找字典
fdmap = {s.fileno():s}

#关注套接字
p.register(s,EPOLLIN|EPOLLERR)

#循环监控关注IO
while True:
    events = p.poll() #阻塞等待IO发生
    print('亲，您有新的IO要处理哦')
    #遍历列表处理IO
    for fd,event in events:
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print('Connect from',addr)
            #注册新的IO
            p.register(c,EPOLLIN|EPOLLERR|EPOLLET)
            fdmap[c.fileno()] = c
        elif event & EPOLLIN:
            data = fdmap[fd].recv(1024)
            if not data:
                p.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]
            print(data.decode())
            fdmap[fd].send(b'OK')