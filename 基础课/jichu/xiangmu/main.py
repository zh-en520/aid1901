
from menu import show_menu
from student_info import *


def main():
    infos = []
    while True:
        show_menu()
        s = input('请选择：')
        if s == '1':
            infos += input_student()
        elif s == '2':
            output_student(infos)
        elif s == '3':
            delete_student(infos)
        elif s == '4':
            modify_students_score(infos)
        elif s == '5':
            print_student_by_score_asc(infos)#asc升序，desc降序
        elif s == '6':
            print_student_by_score_desc(infos)
        elif s == '7':
            print_student_by_age_asc(infos)
        elif s == '8':
            print_student_by_age_desc(infos)
        elif s == '9':
            read(func)
        elif s == '10':
            save(func)
        elif s == 'q':
            break
main()

# 修改原学生信息管理程序，加入异常处理语句，让程序在任何情况下都能按逻辑正常执行，
# 　如：
# 　输入成绩和年龄时，如果输入非法字符也不会导致程序崩溃

# ２．修改原学生信息管理程序，添加两个功能：
# ｜９）从文件中读取数据(si.txt)|
# ｜10)保存信息到文件(si.txt)  |
