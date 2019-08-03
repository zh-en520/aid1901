from test import *
import time

t = time.time()

# for i in range(10):
#     count(1,1)

# print('Single cpu:',time.time()-t)

for i in range(10):
    write()
    read()

print('Single io:',time.time()-t)