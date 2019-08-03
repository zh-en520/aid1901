from threading import Thread,Event
from time import sleep

s = None #全局变量，用于通信
e = Event()

def foo():
    sleep(0.1)
    print('Foo 前来拜山头')
    global s
    s = '天王盖地虎'
    print(s)
    e.set() #接触阻塞

f = Thread(target=foo)
f.start()

#主线程接收口令
print('说对口令就是自己人')
e.wait() #添加阻塞
if s == '天王盖地虎':
    print('小鸡炖蘑菇')
else:
    print('他是二百五')
f.join()