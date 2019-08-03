# 练习：
#     扑克牌５４，只取红桃色牌１３张，用１－１３来表示．洗牌，反面朝上排成一排，找出红桃６．用顺序查找方式来进行，使用python代码实现该过程．

# import random
# L = []
# for i in range(1,14):
#     L.append(i)
# random.shuffle(L)
# for a in L:
#     print(a)
#     if a == 6:
#         print('找到了')
#         break


# #原始数据value
# #待查找内容key
# def linear(value,key):
#     for i in range(len(value)):
#         if value[i] == key:
#             #查找成功
#             return i
#     else:
#         return -1

# if __name__ == "__main__":
#     value = [12,3,4,6,7,5,8,9,10,11,1,2,13]
#     key = 6
#     res = linear(value,key)
#     #调用查找函数
#     res = linear(value,key)
#     if res == -1:
#         print('查找失败')
#     else:
#         print('查找成功',res)
# --------------------------------------------------------------------------------------------------
#二分法递归
#扑克牌５４，只取黑色方块牌１３张，用１－１３来表示．将牌从小到大排序，反面朝上，找出７，使用二分查找，使用python代码实现该过程．
# def func(value,key,left,right):
#     if left > right:
#         return -1
#     while True:
#     #找出中间值
#         middle = (left+right) // 2
#         #对比数据
#         if value[middle] == key:
#             return middle
#         elif value[middle] > key:
#             return func(value,key,left,middle-1)
#         else:
#             return func(value,key,middle+1,right)

# if __name__ == "__main__":
#     value = [1,2,3,4,5,6,7,8,9,10,11,12,13]
#     key = 7
#     res = func(value,key,0,len(value)-1)
#     if res == -1:
#         print('查找失败')
#     else:
#         print('查找成功',res)
# --------------------------------------------------------------------------------------------------

# 循环法
# 扑克牌５４，只取黑色方块牌１３张，用１－１３来表示．将牌从小到大排序，反面朝上，找出７，使用二分查找，使用python代码实现该过程．
# def func(value,key):
#     #左侧下标／右侧下标值
#     left = 0
#     right = len(value) - 1
#     #存在有效数据时继续查找
#     while (left <= right):
#         #中间元素下标
#         middle = (left +right) // 2
#         if value[middle] == key:
#             return middle
#         elif value[middle] > key:
#             right = middle - 1
#         else:
#             left = middle + 1
#     return -1

# if __name__ == "__main__":
#     value = [1,2,3,4,5,6,7,8,9,10,11,12,13]
#     key = 7
#     res = func(value,key)
#     if res == -1:
#         print('查找失败')
#     else:
#         print('查找成功',res)
# --------------------------------------------------------------------------------------------------




# def bubble(value):
#     #外层循环：对应数据走访次数
#     for i in range(len(value)-1):
#         #尚未进行数据交换时，将标记为false
#         flag = False
#     #内层循环：对应走访时相邻数据对比次数
#         for j in range(len(value)-1-i):
#             if value[j] > value[j+1]:
#                 value[j+1],value[j] = value[j],value[j+1]
#                 #若已经进行数据交换，则标志为true
#                 flag = True
#         #若当前走访数据时，未进行数据交换，则证明剩余数据有序，无须继续走访数据
#         if flag is False:
#             break
#     print('遍历次数：',i+1)


# if __name__ == '__main__':
#     L = [12,3,4,6,7,5,8,9,10,11,1,2,13]
#     bubble(L)
#     print(L)
# --------------------------------------------------------------------------------------------------

# 插入排序
# 练习：下午３：３０幼儿园小朋友放学了，要求他们站成一排，模拟插入排序，先是随意排成一排，使小朋友按照身高从低到高排序，使用
# python代码实现该过程．１０名小朋友身高，单位厘米．
# value = [100,50,30,70,60,78,66,88,99,80]
# def insert(value):
#     #外层循环：遍历对应所有无序数据
#     #从第一个无序数据开始，即第二个数据开始
#     for i in range(1,len(value)):
#     #内层循环：从后扫描比较所有有序数据
#     #开始位置：从最后一个有序数据开始，即当前无序数据的前一
#     # 结束位置：下标为０的位置，包含０
#     # 从后向前：－１
#         temp = value[i]
#         pos = 0
#         for j in range(i-1,-1,-1):
#             #比较有序数据和取出的无序数据
#             if value[j] > temp:
#                 #当前有序数据后移
#                 value[j+1] = value[j]
#                 #更新数据插入位置
#                 #对应当前有序数据
#                 pos = j
#             else:
#                 #有序数据小于等于取出数据
#                 #在当前数据的后一位置插入取出数据
#                 pos = j+1
#                 #已经确认数据插入位置
#                 break
#         #确认数据位置后插入数据
#         value[pos] = temp

# if __name__ == "__main__":
#     value = [100,50,30,70,60,78,66,88,99,80]
#     insert(value)
#     print('排序后：',value)

# －－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
#快速排序
def quick(value):
    if len(value) < 2:
        return value
    mark = value[0]
    small = [x for x in value if x < mark]
    big = [x for x in value if x > mark]
    equal = [x for x in value if x == mark]
    return quick(small) + quick(equal) + quick(big)



if __name__ == "__main__":
    value = [100,50,30,70,60,78,66,88,99,80]
    L = quick(value)
    print(L)