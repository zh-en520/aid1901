# 自己写一个文件'info.txt'内部存一些文字信息
# 　张三,20,100
# 　李四,21,96
# 　小王,19,98
# 写程序将这些数据读取出来，并以如下格式打印在终端屏幕上：
# 　张三 今年　20　岁，成绩是：　100
# 　李四 今年　21　岁，成绩是：　96
# 　小王 今年　19　岁，成绩是：　98
# fileline = open('info.txt')
# print('文件已成功打开')
# L = []
# s = fileline.readline()
# L.append(s)
# print('%s今年%d岁，成绩是：%d' % L)
# fileline.close()
# try:
#     filename = 'info.txt'
#     with open(filename) as file_object:
#         while True:
#             line = file_object.readline()
#             if not line:
#                 break
#             s = line.strip()
#             L = s.split(',')
#             name,age,score = L
#             age = int(age)
#             score = int(score)
#             print('%s今年%d岁，成绩是：%d' % (name,age,score))
#         # file_object.close()
# except OSError:
#     print('打开Info.txt失败')


# 写一个程序，输入联系人的电话号码和姓名，把这些姓名和电话号码记录在文件中，
# 存储，如：
# 请输入姓名：
# 请输入电话：
# 格式为：
# 张三　ｘｘｘ
# 李四　ｘｘｘ
# def mywrite():
#     filename = open('contract','w')
#     s = {}
#     while True:
#         name = input('请输入姓名：')
#         if name == '':
#             break
#         phonenumber = input('请输入电话号码：')
#         s['name'] = name
#         s['phonenumber'] = phonenumber
#     filename.close()
#     print(s)
# mywrite()

# try:
#     fw = open('phone.txt','w')
#     while True:
#         name = input('请输入姓名：')
#         number = input('请输入电话：')
#         fw.write(name)
#         fw,write(' ')
#         fw.write(number)
#         fw.write('\n')
#     fw.close()
# except OSError:
#     print('操作失败！')


# 课后练习：
# 写程序，实现复制文件的功能
# 要求：
# １．要考虑关闭文件的问题
# close()
# ２．要考虑超大文件的问题
# flush()
# ３．要能复制二进制文件
# try:
#     filename = open('20bytes.txt','rb')
#     fw = open('mycopy.txt','wb')
#     a = filename.read()
#     fw.write(a)
#     fw.flush(4096)
#     filename.close()
#     fw.close()
def mycopy(inp,oup):
    try:
        input_file = open('inp.txt','rb')
        try:
            output_file = open('oup.txt','wb')
            try:
                while True:
                    a = input_file.read(4096)
                    if a not in input_file:
                        return False
                    output_file.write(a)
                return True
            except OSError:
                return False
                print('操作错误！')
        finally:
            output_file.close()
    finally:
        input_file.close()   

inp = input('请输入源文件：')
oup = input('请输入目标文件：')

if mycopy(inp,oup):
    print('文件复制成功！')
else:
    print('文件复制失败！')




# ２．修改原学生信息管理程序，添加两个功能：
# ｜９）从文件中读取数据(si.txt)|
# ｜10)保存信息到文件(si.txt)  |
