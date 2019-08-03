# python_base_docs_html/随机模块random.html
# 猜数字游戏：
# 　随机生成一个０～１００之间的整数，用变量x绑定
# 　让用户输入一个数用y绑定，输入猜数字的结果
# 　　如果y等于生成的数x，则提示＇恭喜您猜对了＇
# 　　如果y大于x，则提示：＇您猜的数字大了＇
# 　　如果y小于x，则提示：＇您猜的数字小了＇
# 循环让用户输入，直到猜对为止，显示用户猜数字的次数后退出程序

# import random
# def myrandom():
#     n = 0
#     x = random.randint(0,100)
#     while True:
#         y = int(input('请随机输入整数：'))
#         n += 1
#         if y == x:
#             print('恭喜您猜对了')
#             print('共猜了%d次' % n)
#             break
#         elif y > x:
#             print('您猜的数字大了')
#         elif y < x:
#             print('您猜的数字小了')
#     return n
# myrandom()

#折半查找

import math
print(math.log(1000,2))

