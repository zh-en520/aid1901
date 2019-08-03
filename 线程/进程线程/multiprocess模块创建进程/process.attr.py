#实验　　多进程　进程对象属性　示例
from multiprocessing import Process
from time import sleep,ctime

def tm():
    for i in range(3):
        sleep(2)
        print(ctime())

p = Process(target = tm,name = 'Tedu')

p. daemon = True

p.start()

print('Process name:',p.name)
print('Process PID:',p.pid)
print('Process alive:',p.is_alive())

p.join(3)
print('===============================')