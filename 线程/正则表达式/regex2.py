import re

pattern = r"(ab)cd(?P<pig>ef)"
s = 'abcdefghi'

#获取match对象
obj = re.search(pattern,s)

#属性变量
print(obj.pos)
print(obj.endpos)
print(obj.re)
print(obj.string)
print(obj.lastgroup)
print(obj.lastindex)


print('==================')
print(obj.span())
print(obj.start())
print(obj.end())
print(obj.groups())
print(obj.groupdict())
print(obj.group(0))