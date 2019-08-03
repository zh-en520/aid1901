# try_except3.py
try:
    div_apple(10)
    print('分苹果结束')
except (ValueError,ZeroDivisionError):
    print('分苹果失败，苹果被收回')

print('程序结束')