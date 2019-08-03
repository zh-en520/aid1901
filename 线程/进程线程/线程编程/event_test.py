from threading import Event

e = Event()

e.set() #设置e

e.clear() #清除e设置

e.wait(3)

print(e.is_set())

print('**********')