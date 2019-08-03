# from socket import *
# import time
# sockfd = socket()

# server_addr = ('192.168.43.208',8888)
# sockfd.connect(server_addr)

# with open('udp套接字编程','rb') as fr:
#     print('文件打开成功')
#     s = input('请输入指定文件名：')
#     data = sockfd.send(s.encode())
#     time.sleep(0.1)
#     while True:
#         s = fr.read()
#         if not s:
#             time.sleep(0.1)
#             sockfd.send(b'##')
#             break
#         sockfd.send(s)
#     data = sockfd.recv(4096)
#     print('From server',data.decode())

# sockfd.close()



# ---------------------------------------------------------------------------------------------------

