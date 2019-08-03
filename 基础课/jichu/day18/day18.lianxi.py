# class 用类来描述一个学生的信息(可以修改之前的Student类)
#   class Student:
#       ...此处自己实现
# 学生信息有:姓名,年龄,成绩
# 将这些学生对象存于列表中,可以任意添加和删除学生信息
# 1.打印学生的总个数
# 2.打印出所有学生的平均成绩
# (建议用类来封装学生信息,用函数或类方法对学生数据进行操作)


# 思考:
# list 类里只有append向末尾追加数据的方法,但没有向列表头部添加元素的方法,
# 试想能否为列表在不改变原有功能的基础上添加一个insert_head(n)方法来实现向头部插入数据?
# 即:
# class Mylist(list):
#     def insert_head(self,n):
#         self.insert(0,n)
#         self[0:0] = [n]#用切片头插
        
        

# myl = Mylist(range(3,6))
# print(myl)#[3,4,5]
# myl.insert_head(2)
# print(myl)#[2,3,4,5]
# myl.append(6)
# print(myl)#[2,3,4,5,6] 

# 课后练习:
# 写一个类Bicyble类(自行车类),有run方法,调用时显示骑行里程class Bicycle:
# class Bicycle:
#     def run(self,km):
#         print('自行车骑行了',km,'公里')
# 再写一个类EBicycle(电动自行车类),在Bicycle类的基础上添加电池电量volume属性,
# 有两个方法:
# 1.fill_char(vol) 用来充电,vol为电量(度)
# 2.run(km)方法每骑行10km消耗电量1度,同时显示当前电量,当电量耗尽时,则调用Bicycle的run方法(人力骑行)
# class EBicycle(Bicycle):
#     ...#此处自己实现,逻辑要符合现实
# b = EBicycle(5) #新买的电动车内有5度电
# b.run(10) #电动车骑行了10公里,还剩4度电
# b.run(100) #电动骑行了40公里,还剩0度电,人力骑行60km
# b.fill_charge(10) #电动自行车充电10度
# b.run(50) #电动骑行了50公里,还剩5度电

# class Bicycle:
#     def __init__(self,km=0):
#         self.km = km
    
#     def run(self,km):
#         self.km = km
#         print('自行车骑了',self.km,'公里')
# class EBicycle(Bicycle):
#     def __init__(self,v):
#         self.vol = v
#         print('新买的电动自行车内有',self.vol,'度电!')
#     def run(self,km=0):
#         self.km = km
#         total_km = self.vol*10
#         if km <= total_km:
#             self.vol -= self.km/10
#             print('电动车骑行了',self.km,'公里,还剩',self.vol,'度电')
#         else:
#             self.vol = 0
#             last_km = km - total_km
#             super().run(last_km)
#             print('电动车骑行了',total_km,'公里,还剩',self.vol,'度电,人力骑行',last_km,'公里')
#         return self.vol
        
#     def fill_charge(self,vol):
#         self.vol += vol
#         print('电动自行车充电',self.vol,'度')
    


# a = Bicycle()
# a.run(5)
# b = EBicycle(5)
# b.run(10)
# b.run(100)
# b.fill_charge(10)
# b.run(50)