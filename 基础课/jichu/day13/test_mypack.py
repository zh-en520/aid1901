import mypack.menu#导入mypack包里的menu模块
mypack.menu.show.menu()#调用mypack里的menu模块
　　　　　　　　　　　　　　#里的show_menu函数
import mypack.menu as m
m.show_menu()

from mypack.menu import show_menu
show_menu()

from mypack.menu import *
show_menu()