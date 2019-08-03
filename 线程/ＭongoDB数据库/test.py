'''
使用class0集合，为集合中的每个文档添加一个域，结构如下：
score:{'Chinese':78,'Math':95,'English':80}
*注，分数为６０－１００的随机整数
然后使用聚合完成：打印所有男生成绩，按照英语降序排序，不显示_id
'''

from pymongo import MongoClient
from random import randint

#创建数据库连接
conn = MongoClient('localhost',27017)

#创建数据库对象
db = conn.stu
myset = db.class0

cursor = myset.find()
for i in cursor:
    a = randint(60,100)
    b = randint(60,100)
    c = randint(60,100)
    dic = {'Chinese':a,'Math':b,'English':c}
    myset.update_one({'_id':i['_id']},{'$set':{'score':dic}}) 

l = [
    {'$match':{'sex':'m'}},
    {'$sort':{'score.English':-1}},
    {'$project':{'_id':0}}
]
cursor1 = myset.aggregate(l)
for i in cursor1:
    print(i)



#创建集合对象
# myset = db.class0
# l = []
# date = myset.find({},{'_id':0,'name':1})
# for i in date:
#     l.append(i)
# for age in l:
#     a = randint(60,100)
#     b = randint(60,100)
#     c = randint(60,100)
#     myset.update_one({'name':age},{'$set':{'score':{'Chinese':a,'Math':b,'English':c}}},upsert=True)

conn.close()

# { "_id" : ObjectId("5c95d88f2523c19e5351d1ab"), "name" : "li", "age" : 21 }
# { "_id" : ObjectId("5c95f4275802bfc807e58a3e"), "name" : "Lucy", "age" : 18, "sex" : "w" }
# { "_id" : 1, "name" : "Dail", "age" : 17, "sex" : "m" }
# { "_id" : ObjectId("5c95f5e25802bfc807e58a3f"), "name" : "Abby", "age" : 18, "sex" : "w" }
# { "_id" : ObjectId("5c95f5e25802bfc807e58a40"), "name" : "Tom", "age" : 21, "sex" : "m" }
# { "_id" : ObjectId("5c95f75c5802bfc807e58a41"), "name" : "Jame", "age" : 21 }
# { "_id" : ObjectId("5c95f7995802bfc807e58a42"), "name" : "Joy", "age" : 21 }
# { "_id" : ObjectId("5c95f7995802bfc807e58a43"), "name" : "Levi", "age" : 17, "sex" : "m" }
# { "_id" : ObjectId("5c95f8a55802bfc807e58a44"), "name" : "Emma", "age" : 18, "sex" : "w" }
# { "_id" : ObjectId("5c95f8fb5802bfc807e58a46"), "name" : "Sunny", "age" : 17, "sex" : "m" }
# { "_id" : ObjectId("5c95f8fb5802bfc807e58a47"), "name" : "Han", "age" : 18, "sex" : "w" }
