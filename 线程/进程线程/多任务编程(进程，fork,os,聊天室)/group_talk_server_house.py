# 七．群聊聊天室
# １．功能：类似qq群聊功能
# 　[1] 有人进入聊天室需要输入姓名，姓名不能重复
# 　[1] 有人进入聊天室，其他人会收到通知
# 　　　　xxx　进入了聊天室
# 　[1] 一个人发消息，其他人会收到消息
# 　　　xxx : xxxxxxxx
# 　[1] 有人退出了聊天群，其他人也会收到通知
# 　　　xxx 退出了聊天室
# 　[1] 扩展功能：服务端消息公告，服务端发送消息所有人都能收到

# ２．确定技术模型
# 　[1] 服务端和客户端，服务端处理请求，发送管理员消息，客户端执行各种功能；
# 　[1] 套接字选择：UDP套接字
# 　[1] 消息发送模型：转发
# 　　　客户端－－＞服务端－－＞其他客户端
# 　[1] 存储用户信息　{姓名：addr}
# 　[1] 处理收发关系：多进程分别处理收发

# ３．注意事项
# 　[1] 设计封装方法
# 　[1] 写一个功能模块，测试一个模块
# 　[1] 注意注释的添加

# ４．具体实现流程
# 　[1] 搭建网络模型
# 　[1] 进入聊天室
# 　[1] 聊天
# 　[1] 退出聊天室
# 　[1] 管理员消息

'''
Chat room
env:python3.5
exc:socket and fork
name:mr.zhang
email:1207072203@qq.com
'''
from socket import *
import os,sys

#存储用户 {name:addr}
user = {}


def do_quit(s,name):
    msg = '\n%s 退出了聊天室'%name
    for i in user:
        if i != name :
            s.sendto(msg.encode(),user[i])
        else:
            s.sendto(b'EXIT',user[i])
    #删除用户
    del user[name]

def do_chat(s,name,text):
    msg = '\n%s : %s'%(name,text)
    for i in user:
        if i != name:
            s.sendto(msg.encode(),user[i])

def do_request(s):
    while True:
        data,addr = s.recvfrom(1024)
        # print(data.decode())#请求内容
        msglist = data.decode().split(' ')
        #区分请求类型
        if msglist[0] == 'L':
            do_login(s,msglist[1],addr)
        elif msglist[0] == 'C':
            text = ' '.join(msglist[2:])
            do_chat(s,msglist[1],text)
        elif msglist[0] == 'Q ':
            do_quit(s,msglist[1])


def do_login(s,name,addr):
    if (name in user) or ('管理员' in name):
        s.sendto('该用户存在'.encode(),addr)
        return
    s.sendto(b'OK',addr)

    #通知其他人
    msg = '\n欢迎 %s 进入聊天室'%name
    for i in user:
        s.sendto(msg.encode(),user[i])
    
    #添加用户
    user[name] = addr


def main():
    ADDR = ("0.0.0.0",8888)
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind(ADDR)

    #创建单独进程用于发送管理员消息
    pid = os.fork()

    if pid < 0:
        print('Create process failed')
        return
    elif pid == 0:
        while True:
            msg = input('管理员消息：')
            msg = 'C 管理员消息 ' + msg
            s.sendto(msg.encode(),ADDR)
    else:
        #处理各种客户端请求
        do_request(s)

main()