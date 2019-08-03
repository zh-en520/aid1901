# myinteger.py
# 写一个生成器函数myinteger,此生成器函数可以生成从0开始的一系列整数，到n结束(不包含)
def myinteger(n):
    i = 0
    while i < n:
        yield i
        i += 1

for x in myinteger(3):
    print(x)  #打印０，１，２


# L = []
# for x in myinteger(3000000000000000):
#     print(x)

