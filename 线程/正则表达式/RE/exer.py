# import re

# f = open('Test')
# data = f.read()

# # 大写字母开头单词
# # pattern = r'\b[A-Z]\S*\b'

# # 数字，字符，小数
# # pattern = r'\d+\.?/?\d*%?'

# # 日期替换
# pattern = r'\d{4}\.\d{1,2}\.\d{1,2}'

# regex = re.compile(pattern)
# for i in regex.finditer(data):
#     # print(i.group())
#     s = i.group()
#     print(re.sub(r'\.','-',s))

#     # 将目标内容在文档中替换
#     date = re.sub(r'\.','-',s)
#     data = re.sub(pattern,date,data)
# f = open('Test','w')
# f.write(data)
# f.close()

# ----=====-----+++++------******----------=====-----+++++------******------
# BVI100 is down, line protocol is down
#   Interface state transitions: 6
#   Hardware is Bridge-Group Virtual Interface, address is 10f3.116c.e6a7
#   Internet address is 192.168.1.100/24
 
import re
import sys

port = sys.argv[1]

# 找到端口所在段落
f = open('1.txt')
while True:
    data = ''
    for line in f:
        if line != '\n':
            data += line
        else:
            break
    if not data:
        print('No PORT')
        break
    # print(data)

    # 获取每一段首单词
    try:
        PORT = re.match(r'\S+',data).group()
    except Exception:
        continue
    if PORT == port:
        # pattern = r'[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}'
        pattern = r'([0-9]{1,3}\.){3}[0-9]{1,3}/\d+|Unknown'
        address = re.search(pattern,data).group()
        print(address)
        break
f.close()

59.9+90+120+150+180``
# pattern = r'\n\n'
# regex = re.compile(pattern)
# for i in regex.finditer(data):
#     print(i.group())