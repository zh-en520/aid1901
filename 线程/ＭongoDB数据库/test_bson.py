from pymongo import MongoClient
import bson.binary

conn = MongoClient('localhost',27017)
db =conn.image
myset = db.mm

#存储图片
# f = open('girl.jpg','rb')
# data = f.read()

# #转换
# content = bson.binary.Binary(data)

# myset.insert_one({'filename':'mm.jpg','data':content})


img = myset.find_one({'filename':'mm.jpg'})
with open('mm.jpg','wb') as f:
    f.write(img['data'])
    

conn.close()