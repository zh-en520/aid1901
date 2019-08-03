# 写一个生成器函数myeven(start,stop)用来生成从start开始到stop结束(不包含stop)区间内的一系列偶数
# 如：
# def myeven(start,stop):
#     for i in range(start,stop):
#         if i%2==0:
#             yield i
# events = list(myeven(10,20))
# print(events)#[10,12.14,16,18]
# for x in myeven(21,30):
#     print(x)#打印:22 24 26 28
# L = [x**2 for x in myeven(1,10)]
# print(L)#[4,16.36,64]  

# 已知有列表：
# L = [2,3,5,7]
# 1)写一个生成器函数，让此函数能够动态的提供数据，数据为原列表的数字的平方加１
# 2)写一个生成器表达式，让此表达式能够动态提供数据，数据为原列表的数字的平方加１
# 3)生成一个列表，此列表的数据为原列表的数字的平方加１
# 1)
# L = [2,3,5,7]
# def mynum(lst):
#     for i in L:
#         s = i**2+1
#         yield s
# for x in mynum(L):
#     print(x)


    
# 2)
# L = [2,3,5,7]
# s = (i**2+1 for i in L)
# for y in s:    
#     print(y)

# 3)
# L = [2,3,5,7]
# L2 = [x**2+1 for x in L]
# print(L2)

# 写一个程序，从键盘输入一段字符串，用变量s绑定
# 1.将此字符串转为字节串用变量b绑定，并打印出来
# s = input('请输入内容：')
# B = s.encode()
#B = bytes(s,'utf-8')
# print(B)
# 2.打印出字符串s的长度和字节串b的长度
# print(len(s))
# print(len(B))
# 3.将b字节串再转换为字符串用变量s2绑定，再判断s2与s是否相同
# s2 = B.decode()
# if s2 == s:
#     print(True)
# else:
#     print(False)

# 课后练习：
# 1.看下列函数的输出结果是什么？为什么？
#第一个程序:
# L = [2,3,5,7]
# A = [x*10 for x in L]
# it = iter(A)
# print(next(it)) #???
# L[1] = 333
# print(next(it)) #???
# # 第二个程序：
# L = [2,3,5,7]
# A = (x*10 for x in L)
# it = iter(A)
# print(next(it)) #???
# L[1] = 333
# print(next(it)) #???

# 2.试写一个myfilter函数，要求此函数与内建的filter函数的功能一致
# 如：
# def myfilter(func,seq):
#     L = []
#     for i in seq:
#         if func(i):
#             L.append(i)
#     return L
#或者
    # for x in seq:
    #     if func(x):
    #         yield x

# for x in myfilter(lambda x: x % 2 == 1,range(10)):
#     print(x)

# 3.写一个生成器函数myxrange([start,]stop[,step])来生成一系列整数
# 要求：
# myxrange功能与range功能完全相同
# 不允许调用range函数和列表

# --------------课堂讲的答案－－－－－－－－
# def myxrange(start,stop=None,step=None):
#     if stop is None:
#         stop = start
#         start = 0
#     if step is None:
#         step = 1
#     #正向
#     if step > 0:
#         while start < stop:
#             yield start
#             start += step
#     #反向
#     else:
#         while start > stop:
#             yield start
#             start += step
#     yield 1
# for x in range(3):
#     print(x)

# for x in myxrange(100,103):
#     print(x)

# for x in myxrange(1000,1010,3):
#     print(x)

# for x in maxrange(10,0,-3):
#     print(x)

# －－－－－－－－－我的答案－－－－－－－－－－－
# def myxrange(start,stop,step):
#     if start < 0 or start > stop:
#         print('输入的参数有误,请重新输入')
#     while start < stop:
#          yield start
#          start += step
#     return start

# def my_main(a,b=None,c=None):
#     if b is None:
#         start = 0
#         stop = a
#     else:
#         start = a
#         stop = b
#     if c is None:
#         step = 1
#     else:
#         step = c
#     print(start,stop,step)
#     L =[]
#     for i in myxrange(start,stop,step):
#         L.append(i)
#     return L
# try:
#     a = int(input())
# except ValueError:
#     a = 0
# try:
#     b = int(input())
# except ValueError:
#     b = None
# try:
#     c = int(input())
# except ValueError:
#     c = None
# print(my_main(a,b,c)) 



# 4.预习：
# 　文件　和　面向对象编程

# 5.分解质因数，输入一个正整数，分析质因数：
# 如：
# 输入：９０
# 打印：
# 90 = 2*3*3*5
# (质因数是指最小能被原数整除的系数(不包括1))

# －－－－－－－－－－－－－－课堂答案－－－－－－－－－－－－－
def get_zhiyinshu(x):
    L = []
    while x > 1:#一定至少有一个质因数
        for i in range(2,x+1):
            if x % i == 0:
                L.append(i)
                x = int(x / i)
                break

n = int(input('请输入一个整数：'))
L = get_zhiyinshu(n)
L2 = [str(x) for x in L]
s = str(n) + '=' + '*'.join(L2)
print(s)

# ---------------------我的答案－－－－－－－－－－－－
def zhishu(n):
    if n < 2:
        return False
    else:
        for i in range(2,n):
            if n % i == 0 :
                return False
                break
        else:
            return True

def xunhuan(n):
    yuanshu = n
    L = []
    a = 2
    while a<yuanshu:
        while True:
            if n % a == 0:
                n = n / a
                L.append(a)
            else:
                break
        a+=1
    return L

def main(n):
    if zhishu(n):
        print(n,'=',n,'*1')
    else:
        L2 = xunhuan(n)
        s = '%s='%n
        for i in L2:
            s += '%s*'%i
        print(s[:-1])
        # s.replace('*','')
        # print(s)
n = int(input('请输入正整数：'))
main(n)
