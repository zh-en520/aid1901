# 1.定义一个＂人＂类，
# class Human:
#     def set_info(self,name,age,address='不详'):
#         '''此方法用来给人对象添加'姓名','年龄','家庭住址'属性
#         '''
#         # print(name+'今年'+str(age)+'岁'+',','家庭住址'+':'+address)
#         self.last_name = name
#         self.last_age = age
#         self.last_address = address
#         # print(self.set_info)
    
#     def show_infos(self):
#     #     '此处显示此人self的信息'
#         print(self.last_name,'今年',self.last_age,'岁',',','家庭住址',':'
#             ,self.last_address)
    
# h1 = Human()
# h1.set_info('小张',20,'北京市东城区')
# h2 = Human()
# h2.set_info('小李',18)
# h1.show_infos()#小张　今年　20　岁，家庭住址：北京市东城区
# h2.show_infos()#小李　今年　18　岁，家庭住址：不详

# 写一个学生类　Student 类，此类用于描述学生信息，学生信息有：
# 姓名，年龄，成绩（默认为0）
# 1)为该类添加初始化方法，实现在创建对象时自动创建'姓名'，'年龄','成绩'属性
# 2)添加set_score方法能为对象修改成绩信息
# 3)添加shoe_info方法打印学生对象的信息
# 如：
# class Student:
#     def __init__(..):
#         ..
#     def set_score(self,score):
#         ..
#     def show_info(self):
#         ..

# L = []
# L.append(Student('小张',20,100))
# L.append(Student('小李',18,95))
# L.append(Student('小赵',19))
# L[-1].set_score(70)#为小赵修改成绩
# for s in L:
#     s.show_info()#显示所有学生信息





# 练习：
# 有两个人：
# 1)姓名：张三，年龄：３５
# 2)姓名：李四，年龄：１５
# 行为：
# 1)教别人学东西　teach
# 2)赚钱　work
# 3)借钱　borrow
# 4)显示自己的信息　show_info
# 事情描述：
# 张三　教　李四　学　python
# 李四　教　张三　学　王者荣耀
# 张三　上班赚了　１０００　元钱
# 李四　向　张三　借了　２００　元钱
# ３５岁　的张三　有钱　８００元，它学会的技能：王者荣耀
# １５岁　的李四　有钱　２００元，它学会的技能：python
# 如：
# class Human:
#     def __init__(self,name,age=1,money=0,skill=None):
#         self.name = name
#         self.age = age
#         self.money = money
#         self.skill = skill
#         print('初始化被调用！')

#     def teach(*name,skill):
#         self.skill = skill
#         self.name = name
    
#     def work(money):
#         self.money = money
    
#     def borrow(*name,money):
#         self.name1 = name
#         self.name2 = name
#         self.money = money
    
#     def show_info():
#         print(self.name1,'教',self.name2,'学',self.skill)
#         print(self.name2,'教',self.name1,'学',self.skill)
#         print(self.name,'上班赚了',self.money,'元')
#         print(self.name1,'向',self.name2,'借了',self.money,'元')
# L = []
# L.append(Human('张三',35))
# L.append(Human('李四',15))
# L.teach('张三','李四','python')
# L.teach('李四','张三','王者荣耀')
# L[0].work(1000)





# class Human:
#     def __init__(self,n,a):
#         self.name = n
#         self.age = a
#         self.money = 0
#         self.skill = []
    
#     def teach(self,other,skill):
#         print(self.name,'教',other.name,'学',skill)
#         other.skill.append(skill)

#     def work(self,money):
#         print(self.name,'上班赚了',money,'元钱')
#         self.money += money
    
#     def borrow(self,other,money):
#         print(self.name,'向',other.name,'借了',money,'元钱')
#         other.money -= money
#         self.money += money

#     def show_info(self):
#         print(self.age,'岁的',self.name,'有钱',self.money,'元,它学会的技能：',
#             ','.join(self.skill))
        
        
# zhang3 = Human('张三',35)
# li4 = Human('李四',15)
# zhang3.teach(li4,'python')
# li4.teach(zhang3,'王者荣耀')
# zhang3.work(1000)
# li4.borrow(zhang3,200)
# zhang3.show_info()
# li4.show_info()

修改原学生管理程序，将原来用字典来保存学生信息，先将字典改变为用Student类型的对象代替．
要求：
Student类写在一个模块内，模块名为student.py
再使用时用import语句导入
原功能不变