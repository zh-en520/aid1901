#带参数的多进程创建用法
from multiprocessing import Process
from time import sleep

#带参数进程函数：
def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("I'm %s"%name)
        print("I'm working...")
    
# p = Process(target = worker,args = (2,'Levi'))
# p = Process(target = worker,kwargs = {'name':'Abby','sec':2})
#或
p = Process(target = worker,args = (2,),kwargs = {'name':'Abby'})

p.start()
p.join()