def output_student(L):

    # '''以表格形式打印学生信息＇＇＇
    print('+'+'-'*(15)+'+'+'-'*10+'+'+'-'*10+'+')
    print('|'+'姓名'.center(13)+'|'+'年龄'.center(8)+'|'+'成绩'.center(8)+'|')
    print('+'+'-'*(15)+'+'+'-'*10+'+'+'-'*10+'+')
    for i in L:
        print('|'+i['name'].center(15)+'|'+i['age'].center(10)+'|'+i['score'].center(10)+'|')
    print('+'+'-'*(15)+'+'+'-'*10+'+'+'--'*7+'+')

def read():
    try:
        filename = open('si.txt','r')
        b = filename.readlines()
        s = {}
        while True:
            if not b:
                print('该文件里没有信息')
                break
            else:
                for i in b:
                    s += i
        return s
    finally:
        filename.close()



def save(infos):
    pass


def input_student():
    # '''此函数录入学生信息，最后返回学生信息的字典的列表＇＇＇
    L = []
    
    while True:
        d = {}
        while True:
            name = input('请输入姓名：')
            print('姓名输入错误')
            if not name:
                break
            try:
                age = int(input('请输入年龄：'))
                score = int(input('请输入成绩：'))
            except ValueError:
                print('您的输入有误，请重新输入！')
                continue
        d['name'] = name
        d['age'] = age
        d['score'] = score
        L.append(d)
    return L


def modify_students_score(L):
    name = input('请输入要修改学生成绩的姓名：')
    for i in range(len(L)):
        d = L[i]
        if d['name'] == name:
            score = int(input('请输入要修改学生的成绩：'))
            d['score'] = score
            print('修改成功')
            return
    print('修改失败')


def delete_student(L):
    name = input('请输入删除的姓名：')
    for i in range(len(L)):
        d = L[i]
        if d['name'] == name:
            del L[i]
            print('成功删除了：',name)
        else:
            print('删除失败')


def print_student_by_score_asc(L):
    def get_score(d):
        return d['score']
    L2 = sorted(L,key=get_score,reverse=True)
    output_student(L2)

def print_student_by_score_desc(L):
    def get_score(d):
        return d['score']
    L2 = sorted(L,key=get_score)
    output_student(L2)

def print_student_by_age_asc(L):
    L2 = sorted(L,key=lambda d:d['age'],reverse=True)
    output_student(L2)

def print_student_by_age_desc(L):
    L2 = sorted(L,key=lambda d:d['age'])
    output_student(L2)