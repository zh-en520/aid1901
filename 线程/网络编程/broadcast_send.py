from socket import *
from time import sleep

#目标地址
dest = ('192.168.43.255',9999)
s = socket(AF_INET,SOCK_DGRAM)#数据报套接字
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

data = '''
    *****************
    张晨是个大帅比
    *****************
    '''
while True:
    sleep(2)
    s.sendto(data.encode(),dest)

# 接收端：broadcast_recv.py