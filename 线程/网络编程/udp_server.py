from socket import *

#创建数据报套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

#绑定地址
server_addr = ('192.168.43.208',8888)
sockfd.bind(server_addr)

#消息收发
while True:
    data,addr = sockfd.recvfrom(1024)
    print('Receive from %s:%s'%(addr,data.decode()))

    sockfd.sendto(b'Thank you',addr)

#关闭套接字
sockfd.close()