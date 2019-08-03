# 写一个程序，求１－１００之间所内不能被５，７，１１整除的数
# for循环＋continue
s=0
n=range(1,101,1)
for i in n:
    if i%5==0 or i%7==0 or i%11==0:
         continue
    s=s+i
print(s)

