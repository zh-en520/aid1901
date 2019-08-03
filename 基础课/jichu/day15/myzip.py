# 此示例示意自己定义生成器myzip来替代zip函数




# def myzip(iter1,iter2):
#     it1 = iter(iter1)
#     it2 = iter(iter2)#拿到两个迭代器
#     while True:
#         try:
#             x = next(it1)#取出元组的第一个元素
#             y = next(it2)#取出元组的第二个元素
#             yield (x,y)
#         except StopIteration:
#             return

# numbers = [10086,10000,10010,95588]
# names = ['中国移动','中国电信','中国联通']
# for t in myzip(numbers,names):
#     print(t)



def my_enumerate(iterable,start=0):
    it = iter(iterable)
    # n = 0
    while True:#或while n < len(iterable):
        try:    
            x = next(it)
        except StopAsyncIteration:
            return
        L = (start,x)
        yield L
        start += 1
        # n += 1
    return L
#方法３
def my_enumerate(iterable,start=0):
    for x in iterable:
        yield (start,x)
        start += 1

names = ['中国移动','中国电信','中国联通']
for t in my_enumerate(names,100):
    print(t) #(0,'中国移动'),(1,'中国电信'),(...)