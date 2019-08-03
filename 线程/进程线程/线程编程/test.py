#计算密集型程序　x,y传入
def count(x,y):
    c = 0
    while c < 7000000:
        c += 1
        x += 1
        y += 1

#用单线程和多线程计算运行时间time.time
#用单进程和多进程
#10个


#IO密集型

def io():
    write()
    read()

def write():
    f = open('test','w')
    for i in range(1200000):
        f.write('Hello world\n')
    f.close()
def read():
    f = open('test')
    lines = f.readlines()
    f.close()

# Single cpu: 10.376167297363281
# Single io: 4.235895395278931