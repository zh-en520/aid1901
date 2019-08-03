from threading import Thread
from socket import *
import sys

class HTTPServer(object):
    def __init__(self,server_addr,static_dir):
        self.server_addr = server_addr
        self.static_dir = static_dir
        self.create_socket()
        self.bind()
    
    def create_socket():
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    
    def bind(self):
        self.sockfd.bind(self.server_addr)
        self.ip = self.server_addr[0]
        self.port = self.server_addr[1]
    
    def serve_forever(self):
        self.sockfd.listen(5)
        print("Http server listen port %d"%self.port)
        while True:
            try:
                connfd,addr = self.sockfd.accept()
            except KeyboardInterrupt:
                self.sockfd.close()
                sys.exit('退出服务器')
            except Exception as e:
                print('Error',e)
                continue
        clientThread = Thread(target = self.handle,args = (connfd,))
        clientThread.setDaemon(True)
        clientThread.start()

    def handle(self,connfd):
        request = connfd.recv(4096)

        if not request:
            connfd.close()
            return
        
        requestlines = request.splitlines()
        print(connfd.getpeername(),':',requestlines[0])

        getRequest = str(requestlines[0]).split(' ')[1]

        if getRequest == '/' or getRequest[-5:] == '.html':
            self.get_html(connfd,getRequest)
        else:
            self.get_data(connfd,getRequest)

if __name__ == '__main__':
    server_addr = ('0.0.0.0',8000)
    static_dir = './home/tarena/aid1901/线程/算法/概述'
    #创建服务器对象
    httpd = HTTPServer(server_addr,static_dir)
    #启动服务
    httpd.serve_forever()
