# 现有一个用户已经设置好登录名和密码的系统，
# 现有一个用户忘记登录帐号以及密码，
# 此登录系统只有三次尝试机会，请编写一个用户登录系统，
# 如果在３次之内，当用户输入帐号密码和帐号密码匹配，
# 则登录成功
# 否则登录失败，并且当你在输错的情况下提示还剩几次机会．
# name=tarena
# passwd="123"
# name="tarena"
# passwd="123"
n=3
while n > 0:
    name=input("请输入帐号：")
    passwd=input("请输入密码：")
    if passwd!="123" or name!="tarena":
        print('输入错误，您还有%d次输入机会' % int(n-1))
        n-=1
    else:
        print("恭喜您！登录成功")
        break


name=input("请设置登录名：")
passwd=input("请设置密码: ")

for i in range(1,4):
    name_try=input("请输入登录帐号")
    passwd_try=input("请输入登录密码")
    if name_try==name and passwd_try==passwd:
        print("\n登录成功，欢迎%s，您共用了%d次登录机会" % (name,i))
        break
    print("登录失败，已使用%d次登录机会，共３次．\n" % i)
else:
    print("\n登录次数已用尽，请刷新系统")



