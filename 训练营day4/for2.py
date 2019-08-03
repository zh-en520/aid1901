# 输入任意一个数n，打印１到n之间的奇数
n=int(input("请输入任意一个整数"))
print("结果是",end=" ")
for i in range(1,n+1,1):
    if i%2==0:
        continue
    print(i,end=" ")
else:
    print()

for i in range(1,n+1,2):
    print(i,end=" ")
