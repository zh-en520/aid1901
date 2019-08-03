from pymongo import MongoClient

#创建数据库连接
conn = MongoClient('localhost',27017)

#创建数据库对象
db = conn.stu

#创建集合对象
# myset = db.class4

# print(dir(myset))
# －－－－－－－－－－－－insert-----------------------------
# myset.insert_one({'name':'张铁林','king':'乾隆'})
# myset.insert_many([{'name':'张国立','king':'康熙'},{'name':'陈道明','king':'康熙'}])
# myset.insert({'name':'唐国强','king':'雍正'})
# myset.insert([{'name':'陈健斌','king':'雍正'},\
#     {'_id':1,'name':'吴奇隆','king':'四爷'}])
# myset.save({'_id':1,'name':'聂远','king':'乾隆'})
# －－－－－－－－－－find-------------------------------

# cursor = myset.find({},{'_id':0})
# cursor = myset.find({'name':{'$exists':True}},{'_id':0})
# print(cursor)
# for i in cursor:
#     print(i['name'],'---',i['king'])

# print(cursor.next())
# print(cursor.limit(3)) #会报错

# for i in cursor.skip(2).limit(3):
#     print(i)

# for i in cursor.sort([('name',1),('king',-1)]):
#     print(i)

# query = {'$or':[{'name':'陈道明'},{'king':'乾隆'}]},{'_id':0}
# d = myset.find_one({'$or':[{'name':'陈道明'},{'king':'乾隆'}]},{'_id':0})
# print(d)
# ----------------------------update---------------------------------------

# myset.update_one({'king':'康熙'},{'$set':{'king_name':'玄烨'}})

# myset.update_many({'king':'雍正'},{'$set':{'king_name':'胤禛'}})

# myset.update({'king':'乾隆'},{'$set':{'king_name':'弘历'}},multi=True)

# myset.update_one({'name':'郑少秋'},{'$set':{'king':'乾隆'}},upsert=True)

# －－－－－－－－－－－－－－－delete------------------------------------------

# myset.delete_one({'king':'康熙'})
# myset.delete_many({'king':'雍正'})
# myset.remove({'king_name':None})

# ---------------------------复合操作------------------------------------------
# date = myset.find_one_and_delete({'name':'张铁林'})
# print(date)

# －－－－－－－－－－－－－－－－index----------------------------------
myset = db.class0 #切换使用集合
# index_name = myset.create_index([('name',-1)])
# print(index_name)

# index_name = myset.create_index([('age',-1)])
# print(index_name)

# index_name = myset.create_index('name',name='NAME',sparse=True)
# print(index_name)

#查看索引
for i in myset.list_indexes():
    print(i)

# myset.drop_index('NAME')         #索引名称删除
# myset.drop_index([('name',－1)])　#键值对删除
# myset.drop_indexes()              #删除所有索引

# －－－－－－－－－－－－－－－－－聚合操作---------------------------------
l = [
    {'$group':{'_id':'$sex','num':{'$sum':1}}}
]
cursor = myset.aggregate(l)
for i in cursor:
    print(i)

#关闭数据连接
conn.close()