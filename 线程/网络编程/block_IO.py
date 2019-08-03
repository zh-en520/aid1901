from socket import *
from time import ctime,sleep
sockfd = socket()
sockfd.bind(('127.0.0.1',8888))
sockfd.listen(5)


#设置非阻塞IO
# sockfd.setblocking(False)
sockfd.settimeout(5)

while True:
    print('Waiting for connect...')
    try:
        connfd,addr = sockfd.accept()
    except BlockingIOError:
        sleep(2)
        print(ctime())
    except timeout:
        print('timed out...')
    else:
        print('Connect from',addr)
        data = connfd.recv(1024)
        print(data)