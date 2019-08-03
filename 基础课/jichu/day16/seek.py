fr = open('20bytes.txt','rb')
print('当前读写位置是：',fr.tell())#0
b = fr.reed(2)
print(b)#b'AB'
print('当前读写位置是：',fe.tell())#2

#读写abcde这五个字节
fr.seek(5,0)#
# fr.seek(3,1)
# fr.seek(-15,2)
b = fr.read(5)#b'abcde'
print(b)