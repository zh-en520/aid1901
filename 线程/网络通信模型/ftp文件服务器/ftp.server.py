'''
ftp 文件服务器
fork server训练
socket 使用
'''
from socket import *
import os,sys
import signal
import time

#全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)
#文件库目录
FILE_PATH = '/home/tarena/aid1901/linux常用命令大全/'

#功能类
class FtpServer(object):
    def __init__(self,c):
        self.c = c
    
    def do_list(self):
        #获取文件列表
        file_list = os.listdir(FILE_PATH)
        if not file_list:
            self.c.send('文件库为空'.encode())
            return
        else:
            self.c.send(b'OK')
            time.sleep(0.1)
        
        files = ''
        for file in file_list:
            if file[0] != '.' and os.path.isfile(FILE_PATH+file):
                files += file + '#'
        
        #将拼接的字符串发送
        self.c.send(files.encode())

    def do_get(self,filename):
        try:
            fd = open(FILE_PATH+filename,'rb')
        except IOError:
            self.c.send('文件不存在'.encode())
            return
        else:
            self.c.send(b'OK')
            time.sleep(0.1)
        #发送文件
        while True:
            data = fd.read(1024)
            if not data:
                time.sleep(0.1)
                self.c.send(b'##')
                break
            self.c.send(data)
        fd.close()
    
    def do_put(self,filename):
        if os.path.exists(FILE_PATH+filename):
            self.c.send('文件已存在'.encode())
            return
        fd = open(FILE_PATH+filename,'wb')
        self.c.send(b'OK')
        #接收文件
        while True:
            data = self.c.recv(1024)
            if data == b'##':
                break
            fd.write(data)
        fd.close()

#处理请求
def do_request(c):
    ftp = FtpServer(c)
    while True:
        data = c.recv(1024).decode()
        if not data or data[0] == 'Q':
            c.close()
            return
        elif data[0] == 'L':
            ftp.do_list()
        elif data[0] == 'G':
            filename = data.split(' ')[-1]
            ftp.do_get(filename)
        elif data[0] == 'P':
            filename = data.split(' ')[-1]
            ftp.do_put(filename)


#网络通信
def main():
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)

    #处理僵尸进程
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    print('Listen the port 8888....')
    #建立连接
    while True:
        try:
            c,addr = s.accept()
        except KeyboardInterrupt:
            s.close()
            sys.exit('服务器退出')
        except Exception as e:
            print('Error:',e)
            continue
        print('连接上客户端',addr)
        #创建子进程处理客户端请求
        pid = os.fork()
        if pid == 0:
            s.close()
            do_request(c) #处理请求
            os._exit(0)
        else:
            pass
main()