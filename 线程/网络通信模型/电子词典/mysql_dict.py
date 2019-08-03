import pymysql

f = open('/home/tarena/aid1901/线程/网络通信模型/电子词典/dict.txt')

db = pymysql.connect('localhost','root','123456','dict')
#获取游标
cursor = db.cursor()
for line in f:
    tmp = line.split(' ')
    word = tmp[0]
    mean = ' '.join(tmp[1:]).strip()
    sql = 'insert into words (word,mean) values \
          ("%s","%s")'%(word,mean)
    
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        db.rollback()
f.close()