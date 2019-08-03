# n=int(input('请输入数字'))
# s=15000
# for i in range(1,n+1,1):
#     s *= 1.5   
#     s=s*(1+0.2)
#     # s_try=s*(1+.2)
#     # s_try+=1
# print('%d年后的工资是'%n,s)

# print('该矩形的周长为',str((6+4)*2),'cm')
# print('该矩形的面积为',str(6*4),'m**2')
# r=3
# l=2*r*3.1415
# s=3.1415*2*r**2
# print('这个圆fanweinei

# 中国古代的秤是fanweinei几两，
# n=216  #总重量fanweinei
# l=n//16  #地板除，换算成古代的斤数
# s=n%16   #求余，换算成古代的两数
# print('现代的２１６两是古代的%d斤%d两' % (l,s))


# 从凌晨0:0:0计时，到现在已经超过了63320秒，请问，现在是几时，几分，几秒
# n=63320 #以秒计，总时长
# h=n//3600 #地板除，换算时长
# s=n%3600%60  #取余，换算剩余秒数
# m=(n%3600)//60 #总量减去时长的取余，然后地板除，求得余下数额中的分钟数
# print('现在的时间是：%d:%d:%d' % (h,m,s))

# 摄氏温度=5.0/9.0*（华氏温度-32）
#     开氏温度=摄氏温度+273.15
# 摄氏温度＝a;华氏温度＝b;开氏温度＝c

# b=int(input('请输入华氏温度度数'))
# a=5.0/9.0*(b-32)
# c=a+273.15

# print('当华氏温度为%d度时，摄氏温度是%d度,转为开氏温度为%d度' % (b,a,c))
# h=float(input('身高是　'))
# # h=1.75#身高
# w=float(input('体重是　'))
# # w=80.5#体重
# bmi=w/h**2#公式
# if bmi<18.5:
#     print('bmi为%.2f,体重过轻' % bmi)
# elif 18.5<=bmi<=25:
#     print('bmi为%.2f,体重正常' % bmi)
# elif 25<bmi<28:
#     print('bmi为%.2f,体重过重' % bmi)
# elif 28<=bmi<=32:
#     print('bmi为%.2f,体重肥胖' % bmi)
# else:
#     print('bmi为%.2f,体重严重肥胖' % bmi)

# pi=3.14
# i=int(pi)
# fw=pi-i
# bool(fw=.14)

# x=input('请输入整数')
# y=input('请输入整数')
# s=int(x)+int(y)
# m=int(x)*int(y)
# print('这两个数的和为',s)
# print('这两个数的积为',m)

# time=input('请输入小明几岁了')
# z=int(time)*365//7
# day=int(time)*365%7
# print('小明已经活了%d个星期%d天啦'%(z,day))

# num=int(input('请输入一个整数'))

# if num%2==1:
#     print(num,'是奇数')
# else:
#     print(num,'是偶数')

# num=int(input('请输入任意一个整数，判断它的大小区间'))
# if num>100:
#     print('这个数大于１００')
# else:
#     print('这个数不太大哦')

# if num<0:
#     print('这个数小于０')
# else:
#     print('这个数不太小哦')

# if 50<num<150:
#     print('阁下真是慧眼如珠')
# else:
#     print('阁下怎么猜不对呢')

# num=int(input('请输入一个数'))
# if num>0:
#     print('您输入的是正数')
# elif num<0:
#     print('您输入的是负数')
# else:
#     print('您输入的是０')

# quar=int(input('查询每个季度包含的月份：请输入任意的季度数'))
# if 1==quar:
#     print('该季度包括１－３月份')
# elif 2==quar:
#     print('该季度包括４－６月份')    
# elif 3==quar:
#     print('该季度包括７－９月份')
# elif 4==quar:
#     print('该季度包括１０－１２月份')
# else:
#     print('您输错了')

# m=int(input('查询每个月份在哪个季度：请输入任意的月份'))
# if 1<=quar<=3:
#     print('该月份在第一季度')
# elif 4<=quar<=6:
#      print('该月份在第二季度')   
# elif 7<=quar<=9:
#      print('该月份在第三季度')
# elif 10<=quar<=12:
#      print('该月份在第四季度')
# else:
#     print('您输错了')

# def s():
#     print("aaaa")
#     return None
# if s():
#     print("asdf")
# else:
#     print("bbbbbb")

# if 1<=m<=12:
#     if m<=3:
#         print('春季')
#     elif m<=6:
#         print('夏季')
#     elif m<=9:
#         print('秋季')
#     elif m<=12:
#         print('冬季')
# else:
#     print('您输错了')

# #商场促销，满１００元减２０
# money=int(input('请输入商品金额：　'))
# pay=money-20 if money>=100 else money
# print('需要支付',pay,'元')

# #写绝对值
# num=int(input('请输入一个数：　'))
# if num>=0:
#     print(num)
# else:
#     print(-num)

#条件表达式写绝对值
# num=int(input('写一个数：　'))
# num_try=-(num) if num<0 else num
# print(num_try)

# # ＃写程序输入一个学生的成绩，如果成绩在０～１００之间为正常值，否则报错。
# score = int(input('请输入一个学生的成绩'))
# if 0<=score<=100:
#     # print('正常值')
#     pass
# else:
#     print('成绩不在合法的范围内！！！')

# #交换方法１
# a,b = b,a
# #交换方法２
# a=1000,b=2000
# c=a
# a=b
# b=c
# del c

# 北京出租车计价器
# 收费标准：３公平以内收费１３元；基本单价２．３/公里（超出３公里以外）；空驶费：超过１５公里后，每公里加收单价的５０％空驶费/
# （３．４５元/公里）
# 　　要求：
# 输入公里数，打印出费用的金额（以元为单位，精确到分，分以后四舍五入）
# s=int(input('本次行驶里程公里数为：　'))
# if 0<s<=3:
#     m1=13*s
#     print('pay=',round(m1,2),'元')
# elif 3<s<15:
#     m2=13+(s-3)*2.3
#     print('pay=',round(m2,2),'元')
# else:
#     m3=13+(s-3)*2.3+(s-15)*2.3*.5
#     print('pay=',round(m3,2),'元')

#方式２
# pay=13
# if s>3:
#     pay+=(s-3)*2.3
# if s>15:
#     pay+=(s-15)*2.3*.5　
# print('pay=',round(pay,2),'元')


# 写一个程序，输入三个数，打印出三个数中的最大数（思考：如果是四个数，五个数打印出最大数该如何做？）
# a=int(input('第一个数'))
# b=int(input('第二个数'))
# c=int(input('第三个数'))
# if a>b and a>c:
#     print('三个数中a最大')
# elif b>a and b>c:
#     print('三个数中b最大')
# else:
#     print('三个数中c最大')

# if a>b:
#     if a>c:
#         print(a)
#     else:
#         print(c)
# else:
#     if b>c:
#         print(b)
#     else:
#         print(c)

# zuida=a  #假设a最大
# if b>zuida:
#     zuida=b
# if c>zuida:
#     zuida=c
# print('最大值是：', zuida)

# 给出一个年份判断是否是闰年并打印出来结果。
# 　　　规则：每四年一闰，每百年不闰，四百年又闰。
#     如：２０１６年闰年，２１００年非闰年，２４００年闰年
# year=int(input('请输入任意年份：'))
# if year%4==0 and year%100!=0:
#     print('是闰年')
# elif year%400==0:
#     print('是闰年')
# else:
#     print('不是闰年')

# if year%400==0 or (year%4==0 and year%100!=0):
#     print(year,'是闰年')
# else:
#     print(year,'不是闰年')


# 　　４、ＢＭＩ指数（body mass index）又称身体质量指数。
# 　　　ＢＭＩ公式：bmi＝体重（公斤）/身高的平方（米）
# 　　　　如：一个６９公斤的人，身高是１７３公斤
# 　　　　　ＢＭＩ=69/1.73**2=23.05
# 　　标准表：
# 　　　　 BMI<18.5  　　　 体重过轻
#      18.5<=BMI<=24　正常范围
#      BMI>24     　　　体重过重　　　　　
# 　　输入身高和体重，打印BMI的值，并打印体重状况。
# w=float(input('请输入体重（公斤）：'))
# h=float(input('请输入身高（米）：'))
# BMI=w/h**2
# BMI=round(BMI,2)
# if BMI<18.5:
#     print('BMI为',BMI,'体重过轻')
# elif 18.5<=BMI<=24:
#     print('BMI为',BMI,'体重正常')
# else:
#     print('BMI为',BMI,'体重过重')


# 打印一个高度为4行的矩形方框
#方式１
# w=int(input('请输入矩形的宽度'))
# h=4
# line1='#'*w
# print(line1)
# line2='#'+" "*(w-2)+"#"
# print(line2)
# print(line2)
# print(line1)
# ＃方式２
# print('#'*w)
# print('#'," "*(w-2),"#",sep="")
# print('#'," "*(w-2),"#",sep="")
# print('#'*w)

# 输入一个字符串，打印如下内容：
# 　１、打印这个字符串的第一个字符
# 　２、打印这个字符串的最后一个字符
# 　３、如果这个字符串的长度是奇数，打印中间这个字符
# 　注：求字符串的长度的函数是len(x)。
# s="123456"
# print(s[0])
# print(s[-1])
# n=len(s)
# if n%2==0:
#     n_1=n//2-1
# print('中间的数字是',s[n_1 : (n//2)])

# １、写一个程序，输入一个字符串，把字符串的第一个字符和最后一个字符去掉后，打印出这个字符串
# 　２、输入任意一个字符串，判断这个字符串是否是回文
# 　　回文是指中心对称的文字，如：
# 　　上海自来水来自海上
# s='abcbca123321'
# a=s[1:-1]
# print(a)
# s=input('请输入任意字符')
# n=len(s)
# if n%2==1:
#     if s[:n//2]==s[n:n//2:-1]:
#         print('是回文字符')
# else:
#     print('不是回文字符')＃缺点是，如果碰到偶数的回文，会判定失败
#     # 方法２　
# n=s[::-1]
# if n==s:
#     print(s,'是回文')
# else:
#     print(s,'不是回文')

# １、写一个程序输入一段字符串，如果字符串不为空，则把第一个字符的编码值打印出来
# ２、写一个程序，输入一个整数（０～６５５３５），打印出这个数所对应的字符。
# s=input('输入一段字符')
# n=len(s)#可省略不写
# if n!=0:#可直接写　　　if s:
#     print(ord(s[0]))

# s=int(input('输入０～６５５３５之间的数'))
# n=chr(s)
# print(n)

# １、输入一个字符串，把输入的字符串终端空格全部去掉，打印出去掉空格的字符串
# n=input('请输入一个字符串')
# num=n.replace(" ",'')
# print(num)
# ２、输入三行文字，让这三行文字在一个方框中居中显示，（注：不要输入中文）
# 　如：
# 　　请输入：hello!
# 　　请输入：I'm studing python!
# 　　请输入：I like python!
# 　显示如下：
# 　＋－－－－－－－－－－－ ＋
# 　｜      hello!       |
#   |I'm studing python!|
#   |   I like python!  |
#   +--------------------+
# n1=input('请输入字符串１')
# n2=input('请输入字符串２')
# n3=input('请输入字符串３')
# l1=len(n1)
# l2=len(n2)
# l3=len(n3)
# zuida=l1
# if l2>zuida:
#     zuida=l2
# if l3>zuida:
#     zuida=l3
# print('+'+'-'*zuida+'+')

# print("|"+n1.center(zuida)+'|')
# print("|"+n2.center(zuida)+'|')
# print("|"+n3.center(zuida)+'|')
# print('+'+'-'*zuida+'+')
#   3、输入一段字符串，写程序判断你输入的文字是否全是数字，如果是数字，将您输入的数字加１后打印出来。
# n=input('请输入一段字符串')
# if n.isdigit():
#     print(int(n)+1)
# else:
#     print('你输入的字符串不是全数字')

# a=input('输入语句1')
# b=input('输入语句2')
# c=input('输入语句3')
# max_len=max(len(a),len(b),len(c))
# print('语句最长的长度是',max_len)
# # 方式1
# print(' '*(max_len-len(a))+a)
# print(' '*(max_len-len(b))+b)
# print(' '*(max_len-len(c))+c)
# 方式2
# fmt='%'+str(max_len)+'s'
# print(fmt%a)
# print(fmt%b)
# print(fmt%c)

# n=int(input('输入一个整数'))
# i=1
# while i<=n:
#     print('这是第%d行' % i)
#     i+=1

# n=int(input('数字'))
# i=1
# while i<=n:
#     print(i,end=' ')
#     if i%5==0:
#         print()
#     i+=1

# 用while语句打印10~1之间的整数

# i=10
# while i>0:
#     print(i)
#     i-=1

# 1+2+3+4+5+6+7....+100的和
# s=0
# i=1
# while i<=100:
#     s+=i
#     i+=1
# print(s)

#真值表达式示例
#打印1~20的整数，打印在一行内
#打印以上的语句10行
# j=0
# while j<10:
#     print('1 2 3 4..20')
#     j+=1
# ===>>>
# i=1
# while i<=20:
#     print(i,end=" ")
#     i+=1
# print()
# ===>>>
# j=0  
# while j<10:
#     i=1
#     while i<=20:
#         print(i,end=" ")
#         i+=1
#     print()
#     j+=1

#     输入一个整数，打印指定宽度的正方形：
#  如：
#  输入：5
#  打印如下正方形
#  1  2  3  4  5
#  1  2  3  4  5
#  1  2  3  4  5
#  1  2  3  4  5
#  1  2  3  4  5
#  如：输入：3
#  打印如下：
#  1  2  3
#  1  2  3
#  1  2  3

# n=int(input('请输入一个整数'))
# s=1
# while s<=n:
#     i=1
#     while i<=n:
#         print(i,end=' ')
#         i+=1
#     print()
#     s+=1

# 示例说明break用法：
# i=1
# while i<=6:
#     print('循环开始时i='，i)


#     if i==3:
#         break
    
#     print('循环结束时i=',i)
#     i+=1
# else:
#     print('这是while语句中的else子句')
# print('程序结束')

# 示例说明死循环：
#写一个机器人程序
#问：你好    答：有什么可以帮到您的
#问：你叫什么名字 答：机器人
#问：再见    答：欢迎再来 #退出程序
# while 1<2:#或while true:
#     s=input('请问：')
#     if s=='你好':
#         print('有什么可以帮到您')
#     elif s=='你叫什么名字':
#         print('机器人')
#     elif s=='再见':
#         print('欢迎再来')
#         break

# 任意输入一些整数，当输入负数时，结束输入；
#  当输入完后，打印出输入的全部正整数的和。
#  如：
#   请输入：1
#   请输入：2
#   请输入：3
#   请输入：4
#   请输入：-1
# 打印：
#   您刚才输入的这些数的和是：10
# n1=0 #此变量用来累加所有正整数
# while True:
#     n=int(input('请输入：'))
#     if n<0:
#         break
#     n1=n1+n
# print(n1)

# 输入一个正整数n，打印一个宽度和高度都为n个字符的长方形
#  如：请输入：4
#  打印如下：
 ####
 #  #
 #  #
 ####
# n=int(input('请输入一个整数'))
# i=1
# while i<=n:
#     if 1<i<n:
#         print('#'+" "*(n-2)+'#')
#     else:
#         print('#'*n)
#     i+=1
# #方法2
# line1="#*n"
# print(line1)
# line2='#'+' '*(n-2)+'#'
# i=1
# while i<=n-2:
#     print(line2)
#     i+=1
# if n>=2:
#     print(line1)

# 3、写一个程序，输入一个开始的整数用变量begin绑定
#  输入一个结束的整数，用变量end绑定
#  打印从begin开始 到 end 结束（不包含and）的每个整数，打印在一行内
#  如：
#  请输入开始值：8
#  请输入结束值：15
#  打印：
#  8 9 10 11 12 13 14
#  附加思考：如何实现每5个数字打印在一行内，打印多行
#  提示：可以多加一个变量，用来记录打印的个数
# begin=int(input('请输入一个整数'))
# end=int(input('请输入一个整数'))
# i=begin
# s=1
# while i<end:
#     if s%5==0:
#         print()
#     s+=1
#     print(i,end=" ")
#     i+=1
# while i>end:
#     if s%5==0:
#         print()
#     s+=1
#     print(i,end=" ")
#     i-=1


#  4、写一个程序，输入一段字符串，判断这个字符串中有几个英文字母（英文字母是指a-z A-Z的英文）

#  5、用while语句实现打印三角形，输入一个整数，求三角形的宽度和高度，打印除相应的直角三角形。
#  如：
#  请输入三角形的宽度：4
#  *
#  **
#  ***
#  ****
#  或
#    *
#   **
#  ***
# ****
# 或
# ****
# ***
# **
# *
# 或
# ****
#  ***
#   **
#    *

#for示例：语法和用法
# s='abcde'
# for ch in s:
#     print('ch==>',ch)
# else:
#     print('这是for语句的else子句部分的语句')
# print('程序结束')

# 任意输入一段字符串
#  1）计算出这段字符串中空格的个数，并打印这个数
#  2）计算出字符串的全部ascii字符的个数并打印
#   注：ascii字符的编码在0~127范围内
#   思考：用while语句能实现上述功能？
# 1)
# n=input('输入字符串')
# s=0
# for i in n:
#     if i==" ": #if ord(i)==32:
#         s+=1
# print('字符串中空格的个数是：',s,'个')
# #2)
# ascii_count=0
# for i in n:
#     if ord(i)<=127:
#         ascii+=1
# print(ascii_count)
# 1)while
# n=input('输入字符串')
# i=0
# s=0 
# while i<len(n):
#     c=n[i]
#     if c==" ":
#         s+=1
#     i+=1
# print('字符串中空格的个数是：',s,'个')

# 输入一个字符串，从尾向头输出这个字符串的字符
#  如：
#  请输入：ABC中文
#  打印：
#  文
#  中
#  C
#  B
#  A
#方式1
# n=input('请输入字符串')
# for i in n[::-1]:
#     print(i)
#方式2
# n=input('请输入字符串')
# i=len(n)-1#i代表索引，i绑定最后一个元素的索引
# while i>=0:
#     print(n[i])
#     i-=1

# 用for 语句打印1-20的整数，打印在一行内
# for i in range(1,21):
#     print(i,end=" ")
# print()

# 求100以内哪些整数与自身+1的乘积再对11求余的结果等于8
# for i in range(100):
#     if i*(i+1)%11==8:
#         print(i)

# 输入一个正整数，代表正方形的宽度和高度，打印正方形：
#  如：
#  输入：5
#方式1
# n=int(input('输入一个整数'))
# for s in range(1,n+1):
#     for i in range(1,n+1):
#         print(i,end=" ")
#     print()
# #方式2
# n=int(input('输入一个整数'))
# for _ in range(n):
#     for i in range(1,n+1):
#         print(i,end=" ")
#     print()

#continue 用法
#for 语句
# for x in range(5):
#     if x==2:
#       continue
#     print(x)
#while 语句
# x=0
# while x<5:
#     if x==2:
#         x+=1
#         continue
#     print(x)
#     x+=1

#此示例示意用跳过奇数的方式打印10以内的偶数
# for x in range(10):
#     if x%2==1:
#         continue
#     print(x)

# 求1~100之间所有不能被2,3,5,7中任意一个数整除的数的和（用continue实现）
# s=0
# for i in range(1,101):
#     if i%2==0 or i%3==0 or i%5==0 or i%7==0:
#         continue
#     s+=i
# print(s)

# 输入一个整数,代表一棵圣诞节的树干高度
#     打印一棵圣诞树
#     如:
#       输入: 2或3
#     打印
#      *          *
#     ***        ***
#      *        *****
#      *          *
                #   *
                #   *
# n=int(input('请输入树干高度： '))
# # 方式1：生成星号字符串，然后再次字符串居中显示

# max_width=n*2-1#树冠最下层宽度
# for line in range(1,n+1):
#     star = line*2-1#计算每一行的星号个数
#     stars='*'*star#形成字符串
#     print(stars.center(max_width))
# #打印树干部分
# for _ in range(n):#循环n次
#     stars = '*'.center(max_width)#将一个星号居中显示
#     print(stars)
# #方式2 用左侧添加空格的方式

# for line in range(1,n+1):#代表树冠的行数
#     stars = '*'*(line*2-1)#计算星号字符串
#     blank = ' '*(n - line)#计算左侧空格的个数和字符串
#     print(blank + stars)

# for _ in range(n):
#     blank = n - 1#左侧空格个数
#     print(blank + '*')

# 写一个程序,任意输入一个整数,判断是否是素数(prime)
#     素数(也叫质数),是只能被1和自身整除的正整数
#       如:  2   3   5    7    11   13   17   19 ...
#     提示:
#       可以用排除法: 当判断x是否为素数时,只要让x分别除以 
#         2,3,4,5,6,...,x-1, 只要有一次整除了,则x不是素数
#       否则x是素数
# x=int(input('请任意输入一个正整数： '))
# if x<2:
#     print(x,'不是素数')
# else:
#     flag = True#flag标识，先假设x是素数,或者省略用else函数    
#     for i in range(2,x):
#         #让x除以i，只要被整除，则x不是整数
#         if x % i == 0:
#             print(x,'不是素数')
#             flag = False # 当不是素数时放倒旗子
#             break
#             # 走到此处，如果if 条件没有成立过，则x一定是素数
#     if flag:# 或者用else:
#         print(x,'是素数')
    
# 算出 100 ~ 999以内的水仙花数(Narcissistic number)
#     水仙花数是指百位数的3次方 加上 十位数的3次方 加 个位数的
#     3次方等于原数的整数
#       如:  153 等于 1**3 + 5**3 + 3**3 ,则153是水仙花数
#方式1
# for x in range(100,1000):
#     bai = x // 100#提取百位
#     shi = x % 100 //10#十位
#     ge = x %10#个位
#     if x == bai ** 3 + shi ** 3 + ge ** 3:
#         print(x)
# #方式2
# for x in range(100,1000):
#     s = str(x)#转为字符串
#     bai = int(s[0])
#     shi = int(s[1])
#     ge = int(s[2])
#     if x == bai ** 3 + shi ** 3 + ge ** 3:
#         print(x)

#方式3
# for bai in range(1,10):
#     for shi in range(10):
#         for ge in range(10):
#             x = bai * 100 + shi * 10 + ge
#             if x == bai ** 3 + shi ** 3 + ge ** 3:
#                 print(x)

# 输入三行文字，将这三行文字保存在一个列表L中，并打印如：
#  请输入：abc
#  请输入：1234
#  请输入：你好
# 生成如下列表：
#  ['abc','1234','你好']
# one = input('请输入： ')
# seconed = input('请输入： ')
# third = input('请输入： ')
# L = [] #方式1
# L += [one]
# L += [seconed]
# L += [third]
# # L = [one,seconed,third] #方式2
# print(L)

# 写一个程序，让用户输入很多个正整数，当输入负数时结束输入，将用户输入的数存在列表L中，
#   打印这个列表
#   如：
#   请输入：1
#   请输入：2
#   请输入：3
#   请输入：4 
#   请输入：-1
#   打印：[1,2,3,4] 
# L = []
# while True :
#     n = int(input('请输入正整数： '))
#     if n < 0 :
#         break
#     L += [n]

# print(L)

# 输入任意行文字，存于列表中，当不输入内容直接回车（即输入空行）时结束输入
#  1、打印列表中的内容
#  2、计算共输入了几行文字
# print('共输入了',len(L),'行字符')
#  3、计算共输入了多少个字符
# count = 0
# for x in L :
#     count += len(x)
#     print('共有',count,'个字符')
#  4、计算输入的字符中有没有“的”这个字符
# L = []
# n = 0
# while True :
#     a = input('请输入任意字符： ')
#     n += 1
#     if a == '':
#         break
#     L += [a]
# print(L)
# print('共输入了',(n-1),'行文字')
# print('共输入了',len(L),'个字符')
# for i in L[:] :#方法错误，需参考方法2
#     if '的' not in i :
#         continue``
#     else:
#         print('输入的字符中有“的”这个字')
#         break
# #方法2 
# find=False
# for i in L:
#     if '的' in i:
#         find=True
#         break
# if find:
#     print('有')
# else:
#     print('没有')
#方法3  #最简单的方法
# if '的' in str(L):
#     print('有')
# else:
#     print('没有')

# 已知有列表：
#  L = [3,5]
#  用索引和切片操作将原列表改为：
#  L = [1,2,3,4,5,6]
#  将列表反转后删除最后一个元素，再打印此列表
#  ...
#  print(L)  #[6,5,4,3,2]
# L[1:1] = [4]
# L[3:3] = [6]
# L[0:0] = [1,2]
# print(L)

# L = L[::-1]
# del L[-1]
# print(L)

# 写程序，让用户循环输入一些整数，当输入-1时结束输入，将这些整数存于列表L中
#  1、打印这个列表中所有的整数（不包括-1）
# L = []
# while True :
#     a = int(input('请输入： '))
#     if a == -1:
#         break
#     L += [a]
# print(L)
#  2、打印输入的最大数是多少
# print(max(L))
#  3、打印输入的平均数是多少
# print(sum(L)/len(L))

# 写一个程序，让用户输入两个以上的正整数，当输入小于零的数时候结束输入
#  （要求不允许输入重复的数）
# L = []
# while True:
#     a = int(input('请输入正整数： '))
#     if a < 0 :#如果L的个数大于等于2,则允许退出，否则继续输入
#         if len(L) >= 2:
#             break
#         else:
#             print('请至少再输入一个正整数')
#             continue
#     #如果a在L中不存在，则允许添加，否则打印一个未添加提示
    # if a not in L:
    #     L.append(a)  #追加5
    # else:
    #     print(a,'已经存在，请再次输入')

# #  1、打印这些数的和
# print(L)
# #  2、打印这些数中的最大数
# print('和是：',sum(L))
# #  3、打印这些数中的第二大的数
# print('最大数是：',max(L))
# L2 = L.copy() #复制一个副本
# L2.sort(reverse=True)
# print('第二大数是：',L2[1])
# del L2  #释放L2绑定的列表
# #  4、删除最小的一个数
# L.remove(min(L))
# print(L)  #最终结果

# 1、有一些数存于列表中，如：
#   L = [1,3,2,1,6,4,2,27,98,82]
#   1）将列表中出现的数字存入到另一个列表L2中，要求：
#    重复出现多次的数字只在L2列表中保留一份（去重）
# L = [1,3,2,1,6,4,2,27,98,82]
# L2 = []
# L3 = []
# for i in L[:]:
#     if i not in L2:
#         L2.append(i)
        
#     if L.count(i) == 2 and i not in L3:
#         L3.append(i)
       
# print('L2=',L2)
# print('L3=',L3)
#   2）将列表中出现两次的数字存于L3列表中，在L3列表中保留一份



# 2、计算出100以内的全部素数，将这些素数存于列表L中，最后打印出这些素数
# L = []
# for x in range(100):
#     if x<2:
#         continue
#     else:
#         for i in range(2,x):
#             if x%i==0:
#                 break
#         else:
#             L.append(x)
# print('全部的素数是：',L)

# 3、生成前40个斐波那契数（fibonacci）存于列表L中，最后打印出这些数字
#   斐波那契数：
#   1  1  2  3  5  8  13  21...
#   斐波那契数的前两个数是1,从第三个开始，为前两个数的和
# a = 1
# b = 1
# c = 0
# n = 3
# while True :
#     c = a + b
#     print(c)
#     a = b
#     b = c
#     n += 1
#     if n == 41:
#         break
#方式２，最简单的
# L = [1,1]
# while len(L) < 40:
#     #创建下一个这个函数，然后加入列表L中
#     L.append(L[-1]+L[-2])
# print(L)

# 有字符串'hello'，生成字符串‘h e l l o'和'h-e-l-l-o'
# a = 'hello'
# L = []# 或者用方式2
# for ch in a:
#     L.append(ch)  #以上
# print(L)
# b = '-'.join(L)
# c = ' '.join(L)
# print(c)
# print(b)
#方法2
# L = list(a)
#方式3
# a = 'hello'
# b = '-'.join(a)
# c = ' '.join(a)
# print(b)
# print(c)

# 用列表推导式生成1～100内奇数的平方的列表：
#   结果是：[1,9,25,49...9801]
# L = [i**2 for i in range(1,101,2)]
# 等同于
# L = []
# for i in range(1,101,2):
#     L.append(i)
# print(L)
#可改写为：
# L = []
# for i in range(1,101):
#     if i%2 == 1:
#         L.append(i**2)
#推导式示例为：
# L = [i**2 for i in range(1,101) if i % 2 == 1]
# print(L)

# 用字符串'ABC'和'123'生成如下列表：
#  ['A1','A2','A3','B1','B2','B3','C1','C2','C3']
# L = [x+y for x in 'ABC' for y in '123']
# print(L)

# 任意输入一个字符串，将次字符串中的空格全部去掉，生成反转后的字符串
#  如：请输入：abc  def  g
#  生成如下字符串：
#   s2 = 'gfedvba'
#   print(s2)  #gfedvba
#   提示：可以用reversed进行反转
# s = input('请输入：')
# s2 = s.replace(' ','')
# s2 = s2[::-1]
# #方式２
# s2 = ''
# for ch in reversed(s):
#     if ch !=" ":
#         s2 += ch
#         print(s2)

# 将如下数据形成一个字典seasons
#   ‘键'　　　　　　　　　　’值‘
#   １　　　　　－－－－－>'春季有１，２，３月’
#   ２　　　　　－－－－－>'夏季有４，５，６月‘
#   ３　　　　　－－－－－>'秋季有７，８，９月’
#   ４　　　　　－－－－－>'冬季有10,11,12月’

#方式１
# seasons = {}
# seasons[1] = '春季有１，２，３月'
# seasons[2] = '夏季有４，５，６月'
# seasons[3] = '秋季有７，８，９月'
# seasons[4] = '冬季有１０，１１，１２月'
# #方式２
# seasons = {
#     1:...,
#     2:...,
#     3:...,
#     4:...,
# }
# print('seasons=',seasons)


#  2、让用户输入一个整数代表这季度，打印这个季度的信息，
#  　　如果用户输入的信息不存在与字典中，则打印信息不存在
# n = int(input('请输入季度：'))
# if n in seasons:
#     print(seasons[n])
# else:
#     print('信息不存在')

# 输入一行字符串，打印出这个字符串中出现过的字符及出现过的次数
# 　如：请输入：ＡＢＣＤＡＢＣＡＢＡ
# 　打印：
#  A:4次
#  B:3
#  D:1
#  C:2
#  注：不要求打印的顺序
#方式１
# s = {}
# n = input('任意输入一行字符：　')
# for i in str(n):
#     if  i not in s:   
#         s[i] = n.count(i)
# print(s)
# for k in s.keys():
#     print(k,':',s[k],'次')

#方式２
# s=input('请输入：　')
# d = {}
# for ch in s:
    #如果i已经在字典中，说明之前出现过，将个数加１
    #否则，这是第一次出现，用i创建一个键，将个数设置为１
#     if ch in d:
#         d[ch]+=1
#     else:
#         d[ch]=1
# print(d)
# for k,v in d.items():
#     print(k,':',v,'次')

# 有字符串列表如下：
# 　　L =　['tarena','xiaozhang','hello']
#  用上述列表生成如下字典：
#  　d = {'tarena':6,'xiaozhang':9,'hello':6}
#   注：字典的值为键的长度
# L=['tarena','xiaozhang','hello']
# d = {}
# for ch in L:
#     d[ch] = len(ch)
# print(d)
#方式２
# L=['tarena','xiaozhang','hello']
# d = {s:len(s) for s in L}
# print(d)

# 1、输入一些单词和解释，将单词作为键，将解释作为值，将这些数据存入到字典中，
# 　　　打印这个字典
# 　　　然后，循环　输入要查询的单词，给出单词相关的解释，如果字典中不存在这些词
# 　　　则显示查无此词
# s = {}
# a=input('请输入单词')
# a1=input('请输入解释')
# b=input('请输入单词')
# b1=input('请输入解释')
# c=input('请输入单词')
# c1=input('请输入解释')
# s[a] = a1
# s[b] = b1
# s[c] = c1
# print(s)
# while True:
#     d = input('请输入要查询的单词：')
#     if d in s:
#         print(s[d])
#         break
#     else:
#         print('查无此词')
#方式２　
# mydict = {}
# while True:
#     words = input('请输入单词：')
#     if words == "":
#         break
#     trans = input('请输入解释：')
#     if not trans:
#         break
#     mydict[words] = trans
# print('词库是：',mydict)
# while True:
#     words = input('请输入要查询的单词：')
#     if words in mydict:
#         print('解释：',mydict[words])
#     else:
#         print('查无此词')

# ２、已知有两个等长度的列表：
# 　　list = [1001,1003,1008,1006]
# 　　list = ['Tom','Jerry','Spike','Tyke']
#   生成如下字典：
#   　{'Tom':1001,'Jerry':1003,'Spike':1008,'Tyke':1006}
# a = [1001,1003,1008,1006]
# b = ['Tom','Jerry','Spike','Tyke']
# c = {}
# c ={b[i]:a[i] for i in range(len(a))}
# print(c)
# ＃方式２　
# for i in range(len(a)):
#     c[b[i]] = a[i]
# print(c)
#方式３
# d = {}
# for x in a:
#     i = a.index(x)
#     k = b[i]
#     d[k] = x
# print(d)

# 经理有：曹操，刘备，孙权
# 　技术员有：曹操，孙权，张飞，关羽
# 　用集合求：
# 　１，既是经理又是技术员的有：
# 　２，是经理，但不是技术员的有：
# 　３，是技术员，不是经理的都有：
# 　４，张飞是经理吗？
# 　５，身兼一职的人都有：
# 　６，经理和技术员共有几人？
# a = {'曹操','刘备','孙权'}
# b = {'曹操','孙权','张飞','关羽'}
# print('既是经理又是技术员的有：',a & b)
# print('是经理，但不是技术员的有:',a - b)
# print('是技术员，不是经理的都有：',b - a)
# if '张飞' in a:
#     print('张飞是经理')
# else:
#     print('张飞不是经理')
# print('身兼一职的人都有：',a ^ b)
# print('经理和技术员共有:',len(a | b),'人')

# 写程序，任意输入多个正整数，当输入小于零的数时结束输入
# 　１，打印出输入的这些数的种类有多少种？（去重）
# 　２，去掉重复的整数，把剩余的这些数的和打印出来．
# s = set()
# a = []
# while True:
#     n = int(input('请输入任意整数：　'))
#     if n < 0 :
#         break
#     a.append(n)
#     if n >= 0 :
#         for i in a:
#             s.add(i)
# print('这些数的种类有',len(s),'种')
# print(sum(s))

# def 函数
# def say_hello():
    # print('hello world1!')
    # print('hello china!')
    # print('hello tarena!')
# say_hello()

#此示例示意自定义带有两个参数的函数
# ＃此函数用来打印用户调用的两个实参数字的最大值
# def mymax(a,b):#(a,b)代表形参，需要实参
#     print('a =',a)
#     print('b =',b)
#     if a > b :
#         print(a,'大于',b)
#     else :
#         print(a,'小于等于',b)
# mymax(5,10)#代表实参
# mymax('ABC','abc')

# 写一个函数myadd,此函数中的参数列表里有两个参数x,y
# 　此函数的功能是打印两个实参的和（即x+y的和）
# 如：
# 　def myadd(...):
#    myadd(100,200)  #打印３００
#    myadd('ABC','123') ＃打印ABC123
# def myadd(x,y):
#     print('和是',x + y)
# myadd(100,200)
# myadd('ABC','123')

# 写一个函数print_even,传入一个参数n，代表终止的整数
# 打印０　２　４　６　８...以内的所有偶数，打印在一行内
# 函数定义如下：
# 　def print.even(n) :
#    ，，，
#    ＃测试调用
#    　print_even(10)
# def print_even(n):
#     for i in range(0,n+1,2):
#         print(i,end=" ")
#     print()
# print_even(10)

# 写一个函数mymax,实现返回两个数的最大值
# 　如：
# 　def mymax(a,b):
# 　...
# 　print(mymax(100,200))  #200
# 　print(mymax('ABC','123'))  #ABC
# def mymax(a,b):
    # return max(a,b)

#
# def mymax(a,b):
    # if a>b:
    #     return a
    # else :
    #     return b
# mymax(100,200)
# mymax('ABC','123')
# 2,定义两个函数：
# 　def sum3(a,b,c):
#   ...  #此函数用于返回三个数的和
#   def pow3(x):
#   ...   #此函数用于返回x的三次方（立方）
#   用以上两个函数计算：
#   1)计算１的立方＋２的立方＋３的立方
#   2)计算１＋２＋３的和的立方
#   （即：１**3+2**3+3**3和(1+2+3)**3)
# def sum3(a,b,c):
#     return a+b+c
# def pow3(x):
#     return x**3
# print(pow3(1)+pow3(2)+pow3(3))
# print(pow3(sum3(1,2,3)))
# 3,＜＜学生信息管理项目＞＞
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
# print('+'+'-'*(max+10)+'+'+'-'*5+'+'+'-'*5+'+')
# print('|'+'姓名'.center(max+10)+'|'+'年龄'.center(5)+'|'+'成绩'.center(5)+'|')
# print('+'+'-'*(max+10)+'+'+'-'*5+'+'+'-'*5+'+')
# for i in range(n):
#     print('|'+L[i]['name'].center(max+10)+'|'+L[i]['age'].center(5)+'|'+L[i]['score'].center(5)+'|')
# print('+'+'-'*(max+10)+'+'+'-'*5+'+'+'-'*5+'+')

# 此示例示意函数的位置传参和序列传参
# def myfun1(a,b,c):
    # print('a绑定的是：',a)
    # print('b绑定的是：',b)
    # print('c绑定的是：',c)
# myfun1(1,2,3)
# s1 = [11,22,33]
# s2 = (44,55,66)
# s3 = 'ABC'
# myfun1(s1[0],s1[1],s1[2]) 或 
# myfun1(*s1)
# myfun1(*s2)
# myfun1(*s3)

# 关键字传参
# myfun1(a = 11,c = 33,b = 22)
# #字典关键字传参
# d1 = {'c':33,'b':22,'a':11}
# myfun1(c=d1['c'],b=d1['b'],a=d1['a']) 或
# myfun1(**d1)

#此示例示意函数的缺省参数的定义及调用方式------------------------------------------------------
# def info(name,age=1,address='不详'):
#     print(name,'今年',age,'岁，家庭住址：',address)

# info('魏名则',30,'北京市')
# info('tarena',17)
# info('小张')

# 写一个函数Myadd,此函数可以计算两个数，三个数及四个数的和，如：
# 　def myadd(...):
#  ...
# 　print(myadd(10,20)) #30
# 　print(myadd(100,200,300)) #600
# 　print(myadd(1,2,3,4)) #10
# def myadd(a,b,c=0,d=0):
#     return print(a+b+c+d)
# myadd(10,20)
# myadd(100,200,300)
# myadd(1,2,3,4)

# ＃此示例示意星号元组形参＿＿＿＿＿＿-------------------------------------------------
# def func(*args):
#     print('实参的个数是：',len(args))
#     print('args=',args)
# func()　　#无参
# func(1,2,3,4)

# 写一个函数，mysum可以传入任意个实参的数字，返回所有实参的和，如：
# 　def mysum(*args)
#    ...
#   print(mysum(1,2,3,4))
#   print(mysum(100,200,300))
#方式１
# def mysum(*args):
#     n = args
#     print('和是：',sum(n))
# #方式２
# def mysum(*args):
#     s = 0
#     for i in args:
#         s += i
#     return s
# #方式３

#     s = 0
#     i = 0
#     while i < len(args):
#         s += args[i]
#         i += 1
#     return s
# mysum(1,2,3,4)
# mysum(100,200,300)

#此示例示意命名关键字传参＿＿＿＿＿＿＿＿＿－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
# def func(a,b,c,d):
#     print(a,b,c,d)
# func(1,2,3,4)    True
# func(1,2,c=30,d=40)  True
# func(a=1,b=2,c=3,d=4) True
# #现在，需要让c和d必须用关键字传参
# def func(a,b,*,c,d)
# func(1,2,3,4)  False
# func(1,2,c=30,d=40)  True
# func(a=1,b=2,c=3,d=4) True
# d = {'c':300,'d':400}
# func(1,2,**d)  # true,等同于func(1,2,c=300,d=400)

# def func(a,b,*args,c,d)
# func(1,2,3,4,5,6,7,8)  False
# func(1,2,3,4,c=5,d=6)  True

#此示例示意双星号关键字传参＿＿＿＿－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
# def func(**kwargs):
#     print('实参个数是：',len(kwargs))
#     print('关键字参数是：',kwargs)
# func(a=1,b=2,c=3)
# func(x=100,name='tarena',age=17,z = 999)
# func(1,2,c=3,d=4) #false,１和２无法定量

# 写一个函数，已知内建函数max的帮助文档为：
# max(iterable, *[, default=obj, key=func]) -> value
#     max(arg1, arg2, *args, *[, key=func]) -> value
#     仿造max,写一个mymax函数，功能与max完全相同，（要求：不允许调用max函数）
#     如：
# def mymax(...):
#     ...
# print(mumax([6,8,3,5]))
# print(mumax(100,200))
# print(mumax(1,3,5,9,7))

# def mymax(a,*args):
#     if not args:#当args绑定空元组时，a绑定可迭代对象
#         zuida = a[0]  #先假设第一个最大
#         for x in a :
#             if x > zuida:
#                 zuida = x
#         return zuida
#     else:#当mymax输入两个或两个以上的参数，走这个模块
#         zuida = a
#         for x in args:
#             if x > zuida:
#                 zuida = x
#         return zuida
# ＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋
#局部变量及全局变量的示例
# a = 100#创建全局变量a绑定１００
# b = 200
# def fx(c):#c是形参，c也是局部变量，当函数调用结束后，c将被销毁
#     d = ４00#创建局部变量绑定４００
#     print(a,b,c,d)
# fx(300)
# print('a=',a)
# print('b=',b)
# －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
#此示例示意globals和locals函数的作用
# a = 1
# b = 2
# c = 3
# def fn(c,d):
#     e = 300
#     #此时有几个全局变量，几个局部变量？４个全局，fn也算，３个局部
#     print('locals返回：'locals())#locals
#     print('----------------------')
#     print('globals()返回：',globals)
#     print(c)#100 是否可以访问c = 3?
#     mydict = globals()
#     print('全局的c＝',mydict('c'))#c=3
#     print(globals()['c'])#c = 3
# fn (100,200)
# print('程序结束')

# 　１，写一个函数isprime()判断x是否是素数，如果是素数返回true，否则返回false
# def isprime(a):
#     if a < 2:
#         return False
#     else:
#         for i in range(2,a):
#             if a % i == 0:
#                 return False
#         else:
#             return True
# print(isprime(2))
# print(isprime(11))

# 　２，写一个函数prime_m2n(m,n)返回从m开始，到n结束(不包含n)范围内的素数的列表，并打印这些整数
# 　如：
# 　L = prime_m2n(10,20)
# 　print(L) #[11,13,17,19]
# m = int(input('请输入起始值：'))
# n = int(input('请输入结束值：'))
# L = []
# def prime_m2n(m,n):
#     for i in range(m,n):
#         if isprime(i):
#             L.append(i)
#     return L
# print(prime_m2n(10,20))

    
# 　３，写一个函数primes(n),返回指定范围n以内（不包含n)的素数的列表，并打印
# 　如：
# 　L = primes(10)
# 　print(L) #[2,3,5,7]
# 　1)打印１００以内的全部素数
# L = []
# def primes(a):
#     for i in range(a):
#         if isprime(i):
#             L.append(i)
#     return L
# print(primes(100))
# 　2)打印２００以内的全部素数的和
# l1 = primes(200)
# print(sum(l1))

# 　４，写一个函数myrange,可以传入１～３个参数，实际意义与range函数完全相同，返回符合range函数规则的列表
# 　如：
# 　L = myrange(4)
# 　print(L) #[0,1,2,3]
# 　L = myrange(4,6)
# 　print(L) #[4,5]
# 　L = myrange(1,10,3)
# 　print(L) #[1,4,7]
# 　（可以调用range函数）
# def myrange(start,stop_high=0,step=1):
#     L = []
#     if stop_high == 0:
#         for s in range(stop_high,start,step):
#             L.append(s)
#         return L
#     while start <= stop_high:
#         if start == stop_high:
#             print('range(',start,',',stop_high,')')
#         else:
#             for i in range(start,stop_high,step):
#                 L.append(i)
#             return L
# print(myrange(4))
# print(myrange(4,6))
# print(myrange(1,10,3))
#方式２
# def myrange(a,b=None,c=None):
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
#     for i in range(start,stop,step):
#         L.append(i)
#     return L


# －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
# 一个函数可以作为另一个函数的实参传递
# def f1():
#     print('f1被调用')
# def f2():
#     print('f2被调用')
# def fx(fn):
#     print(fn)#＜function f1 at 1xXXXXXXX＞
#     fn()#通过形参fn间接调用了fn绑定的函数
# fx(f1)

# def myinput(fn):
#     L = [1,3,5,6,2,8]
#     r = fn(L)
#     return r
# print(myinput(max))
# print(myinput(min))
# print(myinput(sum))
# # －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
# # 函数可以作为另一个函数的返回值
# def get_function():
#     s = input('请输入您要做的操作：')
#     if s == '求最大'：
#         return max
#     elif s == '求最小':
#         return min
#     elif s == '求和':
#         return sum

# L = [2,4,8,6,10]
# f = get_function
# r = f(L)
# print(r)

# 写一个公式计算器的解释执行器
# 　已知有如下一些函数：
# 　def myadd(x,y)
#     return x+y
#   def mysub(x,y):
#     return x-y
#   def mysum(x,y):
#     return x*y
#-------------------------------------------------------------------
#  再自己写一个函数
# 　def get_func(s):
# ......#此处自己实现
#   此函数传入一个字符串＇加＇或＇＋＇则返回myadd函数
#   此函数传入一个字符串＇乘＇或＇*'则返回mymul函数
#   在程序主函数中的程序如下：
#   def main():
#     while True:
#         s = input('请输入计算公式：＇)＃如１０加２０
#         L = s.split() #L = ['10','加','20']
#         a = int(L[0])
#         b = int(L[2])
#         fn = get_func(L[1])
#         print('结果是：',fn(a,b)) #结果是：３０

# def myadd(x,y):
#     return x+y
# def mysub(x,y):
#     return x-y
# def mysum(x,y):
#     return x*y
# def get_func(s):
#     if s == '+' or s == '加':
#         return myadd
#     if s == '*' or s == '乘':
#         return mysum
#     if s in ('-' , '减'):
#         return mysub
# def main():
#     while True:
#         s = input('请输入计算公式：')#如１０加２０
#         L = s.split()#L = ['10','加','20']
#         a = int(L[0])
#         b = int(L[2])
#         fn = get_func(L[1])
#         print('结果是：',fn(a,b))#结果是：３０
# main()
# -----------------------------------------------------------------

# 函数的嵌套定义
# def fn_outer():
#     print('fn_outer被调用')
#     #在此处...
#     def fn_inner():
#         print('fn_inner被调用')
#     fn_inner()
#     fn_inner()
#     print('fn_outer调用结束')
#     return fn_inner#返回内嵌函数
# # fn_outer()
# fx = fn_outer()#fx 绑定谁？
# fx()
# # fn_inner()　#错误
# print('程序结束')
# ----------------------------------------------------------------------
# 函数作用域
# v = 100
# def fun1():
#     v = 200
#     print('fun1.v=',v)
#     def fun2():
#         v = 300
#         print('fun2.v=',v)
#     fun2()

# fun1()
# print('v=',v)
# --------------------------------------------------------------------------
# golobal语句全局声明
# v = 100

# def f1():
#     global v
#     v = 200#想让此语句来操作全局作用域的变量，怎么办，在前面加声明语句
#     print(v)
# f1()
# print('v = ',v)
# －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
# nonlocal函数声明
# v = 100
# def f1():
#     v = 200
#     print('f1开始时v=',v)

#     def f2():
#         v = 300

#         def f3():
#             nonlocal v
#             v = 400
#             print('f3结束时v=',v)
#         f3()
#         print('f2结束时v=',v) 
#     f2()
    

#     print('f1结束时v=',v)

# f1()
# print('全局的v=',v)# 100
# -------------------------------------------------------------------
# lambda表达式
# def myadd(x,y):
#     return x+y
#以上函数可以改为用lambda实现
# myadd = lambda x,y:x+y

# print('20+30=',myadd(20,30))#50
# print('40+50=',myadd(40,50))#90
# －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
# lambda练习
# 写一个lambda表达式
# 　fx = lambda n:...
# 　此表达式创建的函数判断n这个数的２次方＋１能否被５整除，如果能整除返回true,否则返回false
# print(fx(3)) #True
# print(fx(4)) #False
# fx = lambda a : (a**2 + 1) % 5 == 0
# print(fx(3))
# print(fx(4))

#  2,写一个lambda表达式来创建函数，此函数返回两个形参的最大值
#  如：
#  def mymax(x,y):
#  ......
#  改写后
#  mymax = lambda...
#  测试代码：
#  print(mymax(100,200)) #200
# def mymax(x,y):
#     x = max_num
#     if y >= max_num
#         y = max_num
#     return max_num
#     或
#     return x if x>y else y
# mymax()

# mymax = lambda x,y:x if x>y else y
# mymax = lambda x,y:max(x,y)

# -----------------------------------------------------------
# 看懂程序在做什么？
# def fx(f,x,y):
#    print(f(x,y))

# fx((lambda a,b:a+b),100,200)

# fx((lambda a,b:a**b),3,4)

# ---------------------------------------------------------------------++++++++++
# 课后作业：
# 1,　写一个函数mysum(x)来计算
# １＋２＋３+4+...+x的和
# 要求：不允许调用sum函数
# 如：
# 　print(mysum(100)) #5050
# def mysum(x):
#     s = 0
#     for i in range(x+1):
#         s += i
#     return s
# print(mysum(100))
#用递归求和
# def mysum_recursion(n):
#     if n == 1:
#         return 1
#     else:
#         s = n + mysum_recursion(n-1)
#         return s
# print(mysum_recursion(100))

# 2,写一个函数myfac(n)来计算n!(n的阶乘)
# 　n! = 1*2*3*4*...*n
#  如：
#  　print(myfac(5))#120
# def myfac(n):
#     a = 1
#     for i in range(1,n+1):
#         a *= i
#     return a
# print(myfac(5))
#递归求阶乘
# def myfac(n):
#     if n == 0:
#         return 1
#     else:
#         r = n * myfac(n-1)
#         return r
# 3,写一个函数myfun(n)计算：
# １＋２＊＊２＋３＊＊３＋．．．＋n**n的和
# 如：
# print(myfun(3))  #32
# def myfun(n):
#     s = 0
#     for i in range(1,n+1):
#         s += i**i
#     return s
# print(myfun(3))
#递归方式
# def myfundigui(n):
#     if n == 1:
#         return 1
#     else:
#         s = n**n + myfundigui(n-1)
#         return s
# print(myfundigui(3))
# 使用map函数
# def myfun(n):
    # return sum(map(lambda x: x**x,range(1,n+1)))
# 4,写程序打印杨辉三解（只打印６层）
# def mylove():
#     L = [1]
#     while True:
#         yield L
#         L = [1]+[L[n]+L[n-1] for n in range(1,len(L))] + [1]
    
# n = 0
# for t in mylove():
#     print(t)
#     n = n + 1
#     if n == 6:
#         break
# －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
# eval函数的示意
# s = '1+2*3'
# v = eval(s)
# print('v=',v)

# globals and locals
# s = 'x + y'
# v = eval(s)
# print('v=',v)#目前不能执行
# －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
# exec 函数示意
# －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
# map
# 求1**2+2**2+3**2+...+9**2的和
# a = 0
# for x in range(1,10):
#     a += x**2
#     print(a)
# #fangfa2
# s = 0
# for x in map(pow,range(1,10),[2]*9):
#     s += x
# print(s)
# #fangfa3
# def power2(x):
#     return x**2
# print(sum(map(power2,range(1,10))))
# #fangfa4
# print(sum(map(lambda x:x**2,range(1,10))))

# 求1**９+2**８+3**７+...+9**１的和
# print(sum(map(pow,range(1,10),range(9,0,-1))))

# －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
# 创建一个列表，１－１００之间的　奇数
# def is_odd(x):
#     return x%2==1
# L = [x for x in filter(is_odd,range(1,100))]
# print(L)

# １，用filter函数生成１～２０之间的全部偶数：
# 　将这些数字存于列表中，再打印这个列表
# def is_ou(x):
#     return x%2==0
# L = [x for x in filter(is_ou,range(1,20))]
# print(L)
# ２，用filter函数将１～１００之间所有的素数放到Ｌ列表中，再打印出这个列表
# def is_sushu(x):
#     if x<2:
#         return False
#     else:
#         for i in range(2,x):
#             if x%i == 0:
#                 return False
#                 break
#         else:  
#             return True
# L = [x for x in filter(is_sushu,range(1,100))]
# print(L)

# names = ['Tom',Jerry','Spike','Tyke']
# 排序的依据是最后一个字符的编码值大小，如果最后一个，依次向前对比，即依据为：
# ．．．
# 排序后结果为：
# def getkeys(x):
#     r = x[::-1]
#     return r
# result = sorted(names,key=getkey)
# print(result)
# 
# def story():
#     print('在讲故事')
#     story()
# story()

# ----------------------------------------------------------------------
# 已知有５位朋友在一起
# 第五位朋友比第四位朋友大２岁
# 第四位朋友比第三位朋友大２岁
# 第三位朋友比第二位朋友大２岁
# 第二位朋友比第一位朋友大２岁
# 第一位朋友说他１０岁了
# 编写函数，算出第五位朋友几岁，第三位朋友几岁
# def friends(n):
#     if n == 1:
#         return 10
#     else:
#         years = friends(n-1) + 2
#         return years
# print(friends(5))
# print(friends(3))

# １，写程序算出１～２０的阶乘的和
# 　即：
# 　１！＋２！＋３！＋４！．．＋２０！
# def myfactorial(n):
#     if n == 0:
#         return 1
#     else:
#         s = n * myfactorial(n-1)
#         return s
# s = 0
# for i in range(1,21):
#     s += myfactorial(i)
# print('和是：',s)
#方法２
# print(sum(map(myfactorial,range(1,21))))

# ２，已知有列表：
# 　L = [[3,5,8],10,[[13,14],15,18],20]
# 1)写一个函数print_list(list)打印出所有的数据
# 　print_list(L)#打印　３　５　８　１０　１３　１４．．．
# 　注：不要求打印在一行内

# def print_list(lst):
#     for x in lst:
#         if type(x) is int:
#             print(x)
#         else:
#             print_list(x)
# print_list(L)???排序

# def sum_list(lst):
#     s = 0
#     for x in lst:
#         if type(x) is int:
#             s += x
#         else:
#             s += sum(list(x))
#     return s

# 2)写一个函数sum_list(lst)返回这个列表中所有数字的和
# 　print(sum_list(L))#106
#  注：
#  　type(x) 可以返回一个对象的类型
#  如：
#  　>>>type(10) is int #true
#    >>>type([3,5,8])is list #true
# 3)改写之前的学生信息管理程序，要求添加四个功能：
# 　|5)按学生成绩高－低显示学生信息｜
# 　|6)按学生成绩低－高显示学生信息｜
# 　|7)按学生年龄高－低显示学生信息｜
# 　|8)按学生年龄低－高显示学生信息｜

# －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
# 此示例示意用装饰器来改变函数mufunc的功能

# def mydeco(fn):
#     def fx():
#         print('++++++++++++')
#         fn()
#         print('------------')
#     return fx
# @mydeco
# def myfunc():
#     print('myfunc被调用')

# myfunc = mydeco(myfunc)#开启＼关闭装饰器，此行作用等同于在myfunc上加＠mydeco
# myfunc()
# myfunc()
# myfunc()
# -----------------
# 装饰器示例３
# 此示例示意用装饰器的语法来改变银行业务的需求
# ------------以下是小钱写的装饰器－－－－－－－－－－－－－
# def privileged_check(fn):
#     def fx(n,x):
#         print('正在验证权限．．．')
#         fn(n,x)
#     return fx

# # ------------------
# def send_message(fn):
#     def fy(n,x):
#         fn(n,x)
#         print('正在发短信给',n,'...')
#     return fy
# # －－－－－－－－－－以下是魏老师写的程序－－－－－－－－－－－

# @privileged_check
# def savemoney(name,x):
#     print(name,'存钱',x,'元')

# @send_message
# @privileged_check
# def withdraw(name,x):
#     print(name,'取钱',x,'元')
#     print('发送短信给',name,)
# # ------------以下是调用者小张写的程序－－－－－－－－－－－
# savemoney('小王',200)
# savemoney('小赵',400)
# withdraw('小李',500)

# L = [1,2,3]
# def f(n=0,lst=[]):#缺省参数[]在def语句执行时创建该列表，并此列表一直被f函数绑定
#     lst.append(n)
# f(4,L)
# f(5,L)
# f(100)
# f(200) 
# # 解决方法：
# def f(n=0,lst=None):
#     if lst is None:#说明没有传第二个实参
#         lst = []#创建一个空列表，然后再绑定
#     lst.append(n)
#     print(lst)
# －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
# 1,输入一个圆的半径，打印出这个圆的面积
# import math
# r = int(input('输入圆的半径:'))
# s = math.pi*r**2
# print('面积是：%.2f' % s)
# # 2,输入一个圆的面积，打印出这个圆的半径（要求用math模块内的函数和数据）
# s = int(input('输入圆的面积:'))
# r = math.sqrt(s/math.pi)
# print('半径是：%.2f' % r)

# 　写一个程序，输入你的出生年月日，计算：
# 1)你已经出生多少天？
# 2)你出生那天是星期几？

# import time
# year = int(input('请输入出生的年：'))
# month = int(input('请输入出生的月：'))
# day = int(input('请输入出生的日：'))
# birth_tuple = (year,month,day,0,0,0,0,0,0)
# birth_time = time.mktime(birth_tuple)
# lift_time = time.time()-birth_time
# life_days = lift_time/3600//24
# print('已出生',life_days,'天')

# t = time.localtime(birth_time)
# week = {
#     0:'一'
#     1:'二'
#     2:'三'
#     3:'四'
#     4:'五'
#     5:'六'
#     6:'日'
# }
# print('您出生那天是星期',week[t[6]])

# 写一个程序，以电子时钟的格式打印时间
# 格式为：
# HH:MM:SS

# import time
# now_local
#     if n == 0:
#         return 1
#     else:
#         s = n*fun(n-1)
#     return s

#     s = 0
#     for i in range(n+1):
#         s += 1/fun(n)
#     return s
# n = int(input('请输入数字：') = time.localtime(time.time())#一个当地时间的列表
# print('当前时间是：%d:%d:%d' % (now_local[3],now_local[4],now_local[5]))

# 编写一个闹钟程序，启动时设定时间，到时间后打印一句话：
# 时间到，然后退出程序
# def time_shezhi(fn):
#     def fy(m,n):
#         print('闹钟启动中...')
#         print('设定响铃时间是：%d:%d:00' % (m,n))
#         fn(m,n)
#     return fy

# @time_shezhi
# def myalarm(m,n):
#     # print('闹钟启动中...')
#     import time
#     while True:
#         now_local = time.localtime(time.time())#一个当地时间的列表
#         print('当前时间是：%d:%d:%d' % (now_local[3],now_local[4],now_local[5]),end='\r')
#         time.sleep(0.1)
#         if now_local[3:5] == (m,n):
#             print('时间到!!!')
#             break
#     return
# m = int(input('请输入小时：'))
# n = int(input('请输入分钟：'))
# myalarm(m,n)

# print('闹钟启动中...')
# def myalarm(m,n):
#     import time
#     while True:
#         now_local = time.localtime(time.time())#一个当地时间的列表
#         print('当前时间是：%d:%d:%d' % (now_local[3:6]),end='\r')
#         time.sleep(1)
#         # if now_local[3]=m and now_local[4]=n:
#         if now_local[3:5] == (m,n):
#             print('时间到!!!')
#             break
#     return
# m = int(input('请输入小时：'))
# n = int(input('请输入分钟：'))
# myalarm(m,n)



# 编写函数fun(n)　返回下列多项式的和
# Sn = 1+1/1!+1/2!+1/3!+...+1/n!
# 求n为10时，Sn的值．
# def fun(n):
#     if n == 0:
#         return 1
#     else:
#         s = n*fun(n-1)
#         return s
import math
n = int(input('请输入数字：'))
s = 0
for i in range(n+1):
print(s)

# －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
# 此示例示意自定义模块的编码方法
# def myfac(n):
#     print('正在求%d的阶乘' % n)

# def mysum(n):
#     print('正在计算%d的和' % n)
# name1 = 'audi'
# name2 = 'tesla'
# print('mymod模块已成功加载')

# test.mymod.py
# 此示例示意导入自定义的模块mymod,然后调用mymod内部的函数和数据
# import mymod
# mumod.myfac(5)#调用同mymod里的myfac函数

# from mumod import mysum
# mysum(100)
# from 