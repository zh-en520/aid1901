try:
    fw = open('mybin.txt','wb')#w写，b二进制

    b = bytes(range(256))
    count = fw.write(b)#write返回一个值
    print('字节串成功写入了',count,'个字节')

    fw.close()
except OSError:
    print('打开mybin.txt出错')