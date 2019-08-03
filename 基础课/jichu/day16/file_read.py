# 此示例示意打开和读取myfile.txt文件的文字内容
try:
    file = open('myfile.txt')
    print('文件打开成功！！！')
    s = file.readline()
    print('共读到',len(s),'个字符')
    print('读到的内容是：',s)
    file.close()

except OSError:
    print('文件打开失败！！！')