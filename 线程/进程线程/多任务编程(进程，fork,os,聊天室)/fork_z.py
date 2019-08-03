import os
from time import sleep
import sys

# pid = os.fork()

# if pid == 0:
#     print('Child PID:',os.getpid())
#     os._exit('子进程...挂了')
# else:
#     while True:
#         sleep(2)
#         print('目送......')

pid = os.fork()

if pid < 0:
    print('Error')
elif pid == 0:
    sleep(2)
    print('Child %d process exit'%os.getpid())
    sys.exit(2)
else:
    pid,status = os.wait()
    print('pid:',pid)
    print('status:',os.WEXITSTATUS(status))
    while True:
        pass