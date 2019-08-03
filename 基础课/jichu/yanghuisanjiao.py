# 4,写程序打印杨辉三解（只打印６层）
#杨辉三角真正的教程
# def get_next_line(L):
#     '''用传入的一行L返回下一行
#     如：L = [1,2,1]
#     则返回[1,3,3,1]
#     '''
#     #给出最左侧的1
#     RL = [1]#RL要返回的列表，[1]为最左侧的1
#     #算出中间的len(L)-1个数字
#     for i in range(len(L)-1):#i代表上一行L的索引
#         RL.append(L[i]+L[i+1])
#     #添加最后一个1
#     RL.append(1)
#     return RL
# print(get_next_line([1]))#[1,1]
# print(get_next_line([1,1]))#[1,2,1]
# print(get_next_line([1,2,1]))#[1,3,3,1]

# def get_yanghui_list(n):#n代表最大层数
#     '''如n为３时，返回：
#     [[1],[1,1],[1,2,1]]
#     '''
#     R = []#将要返回的列表
#     line = [1]#先让line绑定第一行数据
#     for _ in range(n):#循环n次
#         R.append(line)#加入一行
#         line = get_next_line(line)#再让Line绑定新的一行
#     return R


# def list_to_string(L):
#     '''此函数给出一个列表，返回列表对应的字符串
#     如：L = [1,3,3,1]
#     返回：'1 3 3 1'
#     '''
#     L2 = [str(x) for x in L]#['1','2','3','1']
#     return' '.join(L2)#return '1 3 3 1'

# def get_yanghui_string_list(L):
#     '''此列表返回字符串列表，如：
#     L = [[1],[1,1],[1,2,1]]
#     返回：['1','1 1','1 2 1']
#     '''
#     RL = [list_to_string(line) for line in L]
#     return RL

# def print_yanghui_triangle(L):
#     '''如果L = ['1','1 1','1 2 1']
#     则居中打印
#     　　１
#     　１　１
#     １　２　１
#     '''
#     max_len = len(L[-1])#最后一行最长
#     for s in L:
#         print(s.center(max_len))
#     return

# L = get_yanghui_list(6)
# print(L)
# SL = get_yanghui_string_list(L)
# print(SL)
# print(print_yanghui_triangle(SL))