str=input('请输入任意一个字符串')
n=0
for i in str:
    if i==' ':
        n+=1
else:
    print("一共有%d空格" % n)

i=0
n=0
while i<len(str):
    if str[i]==" ":
        i+=1
        n+=1
    else:
        i+=1
        continue
else:
    print("该字符串共有%d个空格" % n)