import os
from time import sleep

pid = os.fork()

if pid < 0:
    print('Create process faild')
elif pid == 0:
    print('Child process')
else:
    sleep(0.1)
    print('Parent process')