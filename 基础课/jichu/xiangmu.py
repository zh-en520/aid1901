# ＜＜学生信息管理项目＞＞
# 　输入任意个学生的姓名，年龄，成绩，每个学生的信息存入字典，然后放入到列表中，每个学生需要手动输入
# 　如：
# 　请输入姓名：tarena
# 　请输入年龄：17
# 　请输入成绩：99
# 　请输入姓名：name2
# 　请输入年龄：20
# 　请输入成绩：88
# 　请输入姓名：<回车结束输入>
# 内部存储格式如下：
# 　[{'name':'tarena','age':17,'score':99},
# 　 {'name':'name2','age':20,'score':88}]
# 输入完毕后，以表格形式打印上述信息：
# ＋－－－－－－－－－＋－－－－－－－－＋－－－－－－－－＋
# ｜　　　姓名　　　　｜　　　年龄　　　｜　　　成绩　　　｜
# ＋－－－－－－－－－＋－－－－－－－－＋－－－－－－－－＋
# ｜　 　tarena     |      17      |      99      |
# ｜     name 　　  |      20      |      99      |
# ＋－－－－－－－－－＋－－－－－－－－＋－－－－－－－－＋
#创建字典，列入信息
# L = []
# n = 0
# while True:
#     d = {}
#     name = input('请输入姓名：')
#     if not name:
#         break
#     age = input('请输入年龄：')
#     score = input('请输入成绩：')
#     d['name'] = name
#     d['age'] = age
#     d['score'] = score
#     L.append(d)
#     n += 1
# print(L)
#将列表打印成表格形式 
# max = 0
# for ch in L :# 遍历列表，ch就是列表里的每一个字典
#     name_len = ch['name']  #从每个字典中取出姓名，定义变量为name_len
#     if max < len(name_len):#如果这个姓名长度最长
#         max = len(name_len)
# print('+'+'-'*(15)+'+'+'-'*10+'+'+'-'*10+'+')
# print('|'+'姓名'.center(13)+'|'+'年龄'.center(8)+'|'+'成绩'.center(8)+'|')
# print('+'+'-'*(15)+'+'+'-'*10+'+'+'-'*10+'+')
# for i in range(n):
#     print('|'+L[i]['name'].center(15)+'|'+L[i]['age'].center(10)+'|'+L[i]['score'].center(10)+'|')
# print('+'+'-'*(15)+'+'+'-'*10+'+'+'-'*10+'+')

#---------------------------------------------------------------
# 修改原＜＜学生信息管理程序＞＞将程序的整体功能封装为两个函数
# 　１）编写函数input_student()获取学生信息，以学生姓名为空结束输入，返回学生信息的字典的列表，列表同之前列表
# 　如：
# 　L = input_student()
# 　print(L) #[{'name':'xiaozhang',...},{...}]
#-------------------------------------------------------------
# L = []
# def input_student(a,b,c):
#     while true:
#         d = {}
#         a=input('请输入姓名：')
#         if not name:
#             break
#         b=input('请输入年龄：')
#         c=input('请输入成绩：')
#         d['name'] = a
#         d['age'] = b
#         d['score'] = c
#         L.append(d)
#     return L
# input_student(**d)

# def input_student():
#     # '''此函数录入学生信息，最后返回学生信息的字典的列表＇＇＇
#     L = []
    
#     while True:
#         d = {}
#         name = input('请输入姓名：')
#         if not name:
#             break
#         age = input('请输入年龄：')
#         score = input('请输入成绩：')
#         d['name'] = name
#         d['age'] = age
#         d['score'] = score
#         L.append(d)
#     return L
    


        

    
# 　2)编写函数output_student(L)　以表格的形式打印L列表中的学生信息
# 　如：
# 　output_student(L)  #打印表格
# def output_student(L):
#     # '''以表格形式打印学生信息＇＇＇
#     print('+'+'-'*(15)+'+'+'-'*10+'+'+'-'*10+'+')
#     print('|'+'姓名'.center(13)+'|'+'年龄'.center(8)+'|'+'成绩'.center(8)+'|')
#     print('+'+'-'*(15)+'+'+'-'*10+'+'+'-'*10+'+')
#     for i in L:
#         print('|'+i['name'].center(15)+'|'+i['age'].center(10)+'|'+i['score'].center(10)+'|')
#     print('+'+'-'*(15)+'+'+'-'*10+'+'+'--'*10+'+')

# L = input_student()
# print(L)
# output_student(L)

# ５，实现带界面的＜＜学生信息管理程序＞＞
# 操作界面如下：
# ＋－－－－－－－－－－－－－－－－－－－－＋
# ｜１）添加学生信息　　　　　　　　　　　　｜
# ｜２）显示学生信息　　　　　　　　　　　　｜
# ｜３）删除学生信息　　　　　　　　　　　　｜
# ｜４）修改学生成绩　                 　|
# ｜q）退出　　　　  　　　　　　　　　　　｜
# ＋－－－－－－－－－－－－－－－－－－－－＋
# 请选择：１＜回车＞
# 要求：每个功能写一个函数与之对应


def del_student():
    a = input('请输入删除的姓名：')
    for i in L:
        i['name'] = a
        del i
    return i


def output_student(L):
    # '''以表格形式打印学生信息＇＇＇
    print('+'+'-'*(15)+'+'+'-'*10+'+'+'-'*10+'+')
    print('|'+'姓名'.center(13)+'|'+'年龄'.center(8)+'|'+'成绩'.center(8)+'|')
    print('+'+'-'*(15)+'+'+'-'*10+'+'+'-'*10+'+')
    for i in L:
        print('|'+i['name'].center(15)+'|'+i['age'].center(10)+'|'+i['score'].center(10)+'|')
    print('+'+'-'*(15)+'+'+'-'*10+'+'+'--'*10+'+')


def input_student():
    # '''此函数录入学生信息，最后返回学生信息的字典的列表＇＇＇
    L = []
    
    while True:
        d = {}
        name = input('请输入姓名：')
        if not name:
            break
        age = input('请输入年龄：')
        score = input('请输入成绩：')
        d['name'] = name
        d['age'] = age
        d['score'] = score
        L.append(d)
    return L

def main():
    ku = []
    while True:
        print('+'+'---------------'+'+')
        print('|'+'1)添加学生信息 '+'|')
        print('|'+'2)显示学生信息 '+'|')
        print('|'+'3)删除学生信息 '+'|')
        print('|'+'q)退出 　      '+'|')
        print('+'+'---------------'+'+')
        s = input('请选择：')
        if s == '1':
            ku += input_student()
        elif s == '2':
            ku += output_student()
        elif s == '3':
            ku += del_student()
        elif s == 'q':
            break
main()