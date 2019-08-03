from test import *
import multiprocessing as mp
import time

jobs = []
t = time.time()
for i in range(10):
    p = mp.Process(target = count,args = (1,1))
    # p = mp.Process(target = io)
    time.sleep(1)
    jobs.append(p)
    p.start()

for i in jobs:
    i.join()
print('Process cpu:',time.time() - t)


# from test import *
# import threading as th
# import time

# jobs = []
# t = time.time()
# for i in range(10):
#     p = th.Thread(target = count,args = (1,1))
#     # p = th.Thread(target = io)
#     time.sleep(1)
#     jobs.append(p)
#     p.start()

# for i in jobs:
#     i.join()
# print('thread cpu:',time.time() - t)