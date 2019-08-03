from socket import *
import os,sys
import signal

def client_handle(c):
    print('客户端：',c.getpeername())
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'Receive message')
    c.close()

#创建套接字
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)

#处理僵尸进程
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

print('Listen to the port 8888....')
#循环等待客户端连接
while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        sys.exit('服务器退出')
    except Exception as e:
        print('Error:',e)
        continue
    
    #创建子进程处理客户端请求
    pid = os.fork()
    if pid == o:
        s.close()
        client_handle(c) #处理具体请求
        os._exit(0) #子进程退出
        #无论创建进程失败还是父进程都回去继续等待新的客户端连接
    else:
        pass