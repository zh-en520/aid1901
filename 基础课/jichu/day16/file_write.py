try:
    fw = open('mynote.txt','w')
    fw.write('您好!\n')
    fw.write('ABC\n')
    fw.write('123\n')
    fw.writelines(['这是第一行\n','这是第二行\n'])
    fw.close()
except OSError:
    print('打开文件失败！')