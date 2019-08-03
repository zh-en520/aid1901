from multiprocessing import Semaphore,Process
from time import sleep
import os

#创建信号量
sem = Semaphore(3)

def fun():
    sem.acquire() #消耗一个信号量
    print('%d 执行事件'%os.getpid())
    sleep(2)
    print('%d 执行事件完毕'%os.getpid())
    sleep(0.1)
    sem.release() #增加一个信号量

jobs = []
for i in range(5):
    p = Process(target=fun)
    jobs.append(p)
    p.start()

for i in jobs:
    i.join()
print(sem.get_value())