# 此示例示意文件的打开关闭过程
# 读取文件
try:
    myf = open('myfile.txt')
    print('打开文件成功')

# 读写文件
    for i in myf:
    print(i)

# 关闭文件
    myf.close()
    print('关闭文件成功')
except OSError:
    print('打开文件失败')