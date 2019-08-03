import sys
sys.stdout.write('你好！！！')
sys.stdout.write('这是标准输入打印的文字')

print('hello',file=sys.stdout)
sys.stdout.close() #一旦关闭这个文件，所有的屏幕输出操作将不能使用
#
print('如果sys.stdout被关闭，这里将出现错误！！！+2




















')