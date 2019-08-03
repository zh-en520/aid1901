# 此示例示意with语句的用法和语法

# 打开../day20.txt 读出文件的第一行
try:
    with open('./day20.txt') as fr:
    # try:
        s = fr.readline()
        print('第一行是:',s)
    # finally:
    #     fr.close()
        print('关闭成功')
except OSError:
    print('打开文件失败')


