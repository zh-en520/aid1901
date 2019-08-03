from socket import *
import sys
import getpass

if len(sys.argv) < 3:
    print('''Start app as:
    python3 dict_server.py 127.0.0.1 8000
    ''')
    sys.exit()
HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST,PORT)

#创建网络连接
def main():
    s = socket()
    try:
        s.connect(ADDR)
    except Exception as e:
        print(e)
        return
    
    while True:
        print('''
        ===========welcome==========
        --1.注册　　2.登录　　3.退出--
        ''')
        cmd = input('请输入选项：')
        if cmd not in ['1','2','3']:
            print('请输入正确命令')
            continue
        elif cmd == '1':
            do_register(s)
        elif cmd == '2':
            do_login(s)
        elif cmd == '3':
            s.send(b'E')
            sys.exit('谢谢使用')

def do_register(s):
    while True:
        name = input('User:')
        passwd = getpass.getpass()
        passwd1 = getpass.getpass('Again:')
        if (' 'in name) or (' ' in passwd):
            print('用户名密码不许有空格')
            continue
        if passwd != passwd1:
            print('密码不一致')
            continue
        msg = 'R %s %s'%(name,passwd)
        #发送请求
        s.send(msg.encode())
        #等待回复
        data = s.recv(128).decode()
        print(data)
        if data == 'OK':
            print('注册成功')
            login(s,name)
        elif data == 'EXISTS':
            print('该用户已存在')
        else:
            print('注册失败')
        return

def do_login(s):
    name = input('User:')
    passwd = getpass.getpass()
    msg = "L %s %s"%(name,passwd)
    s.send(msg.encode())
    data = s.recv(128).decode()
    if data == 'OK':
        print('登录成功')
        login(s,name)
    else:
        print('登录失败')

def login(s,name):
    while True:
        print('''
        ============welcome===========
        --1.查单词　2.查历史记录　3.退出--
        ''')
        cmd = input('请输入选项：')
        if cmd not in ['1','2','3']:
            print('请输入正确命令')
            continue
        elif cmd == '1':
            do_query(s,name)
        elif cmd == '2':
            do_hist(s,name)
        elif cmd == '3':
            return

def do_query(s,name):
    while True:
        word = input('单词：')
        if word == '##':
            break
        msg = 'Q %s %s'%(name,word)
        s.send(msg.encode())
        #可能是单词解释也可能是找不到
        data = s.recv(2048).decode()
        print(data)

def do_hist(s,name):
    msg = "H %s"%name
    s.send(msg.encode())
    data = s.recv(128).decode()
    if data == 'OK':
        while True:
            data = s.recv(1024).decode()
            if data == '##':
                break
            print(data)
    else:
        print('您还没有查询记录')
            
main()