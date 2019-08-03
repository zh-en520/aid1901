
fw = open('myflush.txt','w')
fw.write('hello')
fw.flush()#立即将缓冲区的内容写入磁盘(即使缓冲区未满．也会立即写入磁盘，进行一次磁盘的ＩＯ操作)

while True:
    pass
# fw.write('hello')
# import time
# while True:
    # fw.write('1234567890')
    # time.sleep(0.01)
fw.close()