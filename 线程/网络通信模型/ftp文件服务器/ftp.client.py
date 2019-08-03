from socket import *
import sys,time
#全局变量
server_addr = ('127.0.0.1',8888)

#具体功能
class FtpClient(object):
    def __init__(self,s):
        self.s = s
    
    def do_list(self):
        self.s.send(b'L') #发送请求
        #等待回复
        data = self.s.recv(4096).decode()
        if data == 'OK':
            data = self.s.recv(8192).decode()
            files = data.split('#')
            for i in files:
                print(i)
        else:
            #无法完成
            print(data)

    def do_quit(self):
        self.s.send(b'Q')
        self.s.close()
        sys.exit('谢谢使用')

    def do_get(self,filename):
        self.s.send(('G '+filename).encode())
        data = self.s.recv(128).decode()
        if data == 'OK':
            fd = open(filename,'wb')
            while True:
                data = self.s.recv(1024)
                if data == b'##':
                    break
                fd.write(data)
            fd.close()

    def do_put(self,filename):
        try:
            f = open(filename,'rb')
        except IOError:
            print('没有该文件')
            return
        #获取文件名称去除可能的路径
        filename = filename.split('/')[-1]
        self.s.send(('P '+filename).encode())
        data = self.s.recv(128).decode()
        if data == 'OK':
            while True:
                data = f.read(1024)
                if not data:
                    time.sleep(0.1)
                    self.s.send(b'##')
                    break
                self.s.send(data)
            f.close()
        else:
            print(data)


#网络连接
def main():
    try:
        s = socket()
        s.connect(server_addr)
    except Exception as e:
        print('Error:',e)
        return
    
    #创建实例化对象
    ftp = FtpClient(s)

    while True:
        print('\n-------命令选项--------')
        print('***      list      ***')
        print('***    get file    ***')
        print('***    put file    ***')
        print('***      quit      ***')
        print('------------------------')
        
        cmd = input('输入命令>>')
        if cmd.strip() == 'list':
            ftp.do_list()
        elif cmd.strip() == 'quit':
            ftp.do_quit()
        elif cmd[:3] == 'get':
            filename = cmd.split(' ')[-1]
            ftp.do_get(filename)
        elif cmd[:3] == 'put':
            filename = cmd.split(' ')[-1]
            ftp.do_put(filename)
        else:
            print('请输入正确命令')

main()