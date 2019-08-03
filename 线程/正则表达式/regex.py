import re

# s = 'zhang:1994 li:1995'
# pattern = r'(\w+):(\d+)'
# －－－－－－－－－－－－－－－－－－－－－－－－
# l = re.findall(pattern,s)
# print(l) 
# －－－－－－－－－－－－－－－－－－－－－－－－－
# regex = re.compile(pattern)
# l = regex.findall(s,0,10)
# －－－－－－－－－－－－－－－－－－－－－－－－－
# l = re.split(r'\s+','Hello     word')
# print(l)
# -----------------------------------------
# s = re.sub(r'垃圾,垃圾','**','张三，垃圾,垃圾,垃圾,垃圾',3)
# print(s)
# -------------------------------------------



# s = '2019年4月28日'
# pattern = r'\d+'

# it = re.finditer(pattern,s)

# print(dir(next(it)))

# for i in it:
#     print(i.group()) #获取match对象匹配到的内容
# －－－－－－－－－－－－－－－－－－－－－－－－－－－－
# obj = re.fullmatch(r'\w+','hello_word')
# print(obj.group())

# －－－－－－－－－－－－－－－－－－－－－－－－－－－－
# obj = re.match(r'[A-Z]\w+','Hello Jame')
# print(obj.group())
# --------------------------------------------------
#匹配第一处
obj = re.search(r'\d+','今天2018-1-19')
print(obj.group())