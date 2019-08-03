from multiprocessing import Process,Array
import time

#创建共享内存
# shm = Array('i',[1,2,3,4,5])

#创建共享内存，指定开辟共享内存大小
# shm = Array('i',６)

#存入字符串
shm = Array('c',b'Hello')

def fun():
    for i in shm:
        print(i)
    shm[0] = b'h' #修改共享内存

p = Process(target = fun)
p.start()
p.join()

for i in shm:
    print(i,end=' ')
print(shm.value) #　打印字符串
