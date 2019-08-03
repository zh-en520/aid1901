# import socket

# sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sockfd.bind(('192.168.43.208',8888))
# sockfd.listen(5)


# print('Witing for connect....')
# # try:
# connfd,addr = sockfd.accept()
# # except KeyboardInterrupt:
# #     print('Server exit')
# #     break
# print('Connect from',addr)
# s = connfd.recv(1024).decode()

# with open(s,'w') as myfile:
#     print('新建文件并成功打开成功')

#     while True:
#         data = connfd.recv(4096)
#         if data == b'##':
#             break
#         myfile.write(data.decode())
    
#     n = connfd.send(b'Thank you')
#     print('send %d bytes'%n)
        

# connfd.close()
# sockfd.close()


# -------------------------------------------------------------------------------------------------------------------
from select import select
from socket import *

sockfd = socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(('127.0.0.1',8888))
sockfd.listen(5)

rlist = [sockfd]
wlist = []
xlist = []

fw = open('select_file.txt','w')
while True:
    rs,ws,xs = select(rlist,wlist,xlist)
    for r in rs:
        if r is sockfd:
            c,addr = r.accept()
            print('Connect from',addr)
            rlist.append(c)
            print(list(rlist))
            fw.write(rlist,end='\n')
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print(data.decode())
            fw.write(data.decode(),end='\n')
            wlist.append(r)
            fw.write(wlist,end='\n')
    
    for w in ws:
        a = w.send(b'OK')
        fw.write(a.decode(),end='\n')
        wlist.remove(w)
    
    for x in xs:
        if x is sockfd:
            x.close() 

fw.close()


    