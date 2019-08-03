#创建多个子进程

from multiprocessing import Process
from time import sleep
import os

def th1():
    sleep(3)
    print('吃饭')
    print(os.getppid(),'...',os.getpid())

def th2():
    sleep(4)
    print('睡觉')
    print(os.getppid(),'...',os.getpid())

def th3():
    sleep(2)
    print('打豆豆')
    print(os.getppid(),'...',os.getpid())

processes = []
things = [th1,th2,th3]
for th in things:
    p = Process(target = th)
    processes.append(p) #用列表保存进程对象
    p.start()

for i in processes:
    i.join()