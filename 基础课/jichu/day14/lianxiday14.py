# lainxi写一个函数get_score()来获取学生输入的成绩（０～１００）的整数，如果输入的不是０～１００的整数，则此函数返回０．
#  如：
#  def get_score():
#     s = input('请输入成绩：')
#     ...#此处自己实现
#     score = get_score
#     print('学生的成绩是：',score)

# def get_score():
#     s = input('请输入成绩：')
#     try:
#         scr = int(s)
#     except ValueError:
#         print('值为：',0)
#         if 0 <= scr <= 100:
#             return scr
#         return 0
# score = get_score()
# print('学生的成绩是：',score)


# 写一个函数get_age()用来获取一个人的年龄信息
#  此函数规定用户只能输入1~140之间的整数，如果用户输入其他的数则直接触发ValueError类型的错误！
#  如：def get_age():
#          ...
#     try:
#         age = get_age()
#         print('用户输入的年龄是：',age)
#     except ValueError as err:
#         print('用户输入的不是1~140的整数,获取年龄失败!')

# def get_age():
#     n = int(input('请输入年龄：'))
#     assert 1 <= n <= 140,'获取年龄失败'
#     return n
#     # if 1 < n < 140:
#     #     return n
#     # else:
#     #     raise ValueError('年龄超出范围')


# try:
#     age = get_age()
#     print('用户输入的年龄是：',age)
# except ValueError as err:
#     print('用户输入的不是1~140的整数,获取年龄失败!')

# 1.有一个集合：
# 　s = {'唐僧','悟空','八戒','沙僧'}
#  用for 语句来遍历所有元素如下：
#  　for x in s :
#         print(x)
#    else :
#         print('遍历结束')
#     请将上面的for语句改写为while语句和迭代器实现

# s = {'唐僧','悟空','八戒','沙僧'}
# myit = iter(s)
# while True:
#     try:
#         x = next(myit)
#         print(x)
#     except StopAsyncIteration:
#         print('遍历结束')
#         break
# 2.一个球从100米高空落下，每次落地后反弹高度为原高度的一半，再落下
# 　1)写程序算出皮球在低10次落地后反弹多高
# 　2)打印出共经历多少米路程
# print('我自己做的－－－－－－－－－－－－－－－－－－－－－－－')
# try:
#     n = int(input('请输入要查询的落地次数：'))
# except ValueError:
#     print('输入错误！')
# def mybool():
#     global n
#     h = 100
#     L = [100]
#     for _ in range(n):
#         s = h
#         h *= 0.5
#         L.append(s)
#     print(L)
#     return L
# l = mybool()
# print(l[n]/2)
# print(sum(l))

# print('老师讲的－－－－－－－－－－－－－－－－－－－－－－－')
# def get_last_height(height,times):
#     '''
#     height 代表起始高度
#     times 代表弹跳的次数
#     返回值为：最终的高度
#     '''
#     for _ in range(times):
#         height /= 2
#     return height
# print('100米反弹１０次后的高度为：',get_last_height(100,10))
# def get_distance(height,times):
#     s = 0
#     for _ in range(times):
#         #计算下落的距离
#         s += height
#         #计算反弹的高度
#         height /= 2
#         #累加反弹的距离
#         s += height
#     return s
# print('小球从１００反弹１０次后的总路程为：',get_distance(100,10))
# 3.修改原学生信息管理程序，加入异常处理语句，让程序在任何情况下都能按逻辑正常执行，
# 　如：
# 　输入成绩和年龄时，如果输入非法字符也不会导致程序崩溃
