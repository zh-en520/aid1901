from socketserver import *

# 创建tcp多进程并发
class Server(ForkingMixIn,UDPServer):
    pass

#创建请求处理类
class Handle(DatagramRequestHandler):
    #重写具体处理方法
    def handle(self):
        print('Connect from',self.client_address)
        while True:
            data = self.rfile.readline()
            if not data:
                break
            print(data)
            self.wfile.write(b'OK')
           
server_addr = ('0.0.0.0',8888) 
#创建服务器对象
server = Server(server_addr,Handle)
server.serve_forever() #启动服务