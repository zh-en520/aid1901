import socket
#创建tcp套接字
sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定地址
sockfd.bind(('0.0.0.0',8800))
#设置监听
sockfd.listen(5)
#等待处理客户端连接
while True:
    print('Waiting for connect...')
    try:
        connfd,addr = sockfd.accept()
    except KeyboardInterrupt:
        print('Server exit')
        break
    print('connect from',addr)#客户端地址
#收发消息
    while True:
        data = connfd.recv(10)
        if not data:
            break
        print('Receive message:',data.decode())
        #发消息
        n = connfd.send(b'I Love You to')
        print('send %d bytes'%n )

#关 闭套接字
    connfd.close()
sockfd.close()