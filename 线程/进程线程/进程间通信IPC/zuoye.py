from multiprocessing import Process
from time import sleep
import os

# fr = open('/home/tarena/aid1901/基础课/基础课day02.txt','rb')
# fr_file = fr.read()
# fr_len = len(fr_file)
# a = fr_len//2
# def f1():
#     fr.seek(0)
#     fr_a = fr.read(a)
#     fw1 = open('123.txt','wb')
#     fw1.write(fr_a)
#     fw1.close()
# def f2():
#     fr.seek(a,0)
#     fr_b = fr.read()
#     fw2 = open('234.txt','wb')
#     fw2.write(fr_b)
#     fw2.close()


# s = []
# things = [f1,f2]
# for th in things:
#     p = Process(target=th)
#     s.append(p)
#     p.start()

# for i in s:
#     i.join()
# fr.close()

# ===========================================================
filename = './time.jpg'
#获取文件大小
size = os.path.getsize(filename)
#复制上半部分
def top():
    n = size // 2
    fr = open(filename,'rb')
    fw = open('top.jpg','wb')
    while True:
        if n < 1024:
            fw.write(fr.read(n))
            break
        fw.write(fr.read(1024))
        n -= 1024
    fr.close()
    fw.close()
#复制下半部分
def bot():
    fr = open(filename,'rb')
    fw = open('bottom.jpg','wb')
    fr.seek(size//2,0)
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()
t = Process(target=top)
b = Process(target=bot)
t.start()
b.start()
t.join()
b.join()