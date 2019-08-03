#以下为正常流程
def div_apple(n):
    print(n,'个苹果你想分给几个人？'')
    s = input('请输入人数：')
    cnt = int(s)   #可能引发程序ValueError错误
    result = n / cnt  #可能触发ZeroDivisionError错误
    print('每个人分了',result,'个苹果')
div_apple(10)#如果打印的是10O呢？
print('分苹果结束')

print('程序结束')


def div_apple(n):
    print(n,'个苹果你想分给几个人？'')
    s = input('请输入人数：')
    cnt = int(s)   #可能引发程序ValueError错误
    result = n / cnt  #可能触发ZeroDivisionError错误
    print('每个人分了',result,'个苹果')
try:
    div_apple(10)
    print('分苹果结束')
except ValueError as err:
    print('分苹果失败，苹果被收回')
    print('出错的原因是',err)

print('程序结束')

try:
    div_apple(10)
    print('分苹果结束')
except (ValueError,ZeroDivisionError):
    print('分苹果失败，苹果被收回')

print('程序结束')

练习：
 try_except.py
 try_except_as.py
 try_except3.py
 try_except4.py
 