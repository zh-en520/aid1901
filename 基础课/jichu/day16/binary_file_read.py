
fr = open('myfile.txt','rb')#二进制方式读取文件
b = fr.read()#b绑定的是字节串
fr.close()
print('读取的内容是：',b)
print('字节串的长度是：',len(b))
s = b.decode()
print('字符串的长度是：',len(s))
print('字符串的内容是：',s)