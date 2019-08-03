frpm select import select

from sockrt import *

import sys

s = socket()
s.bind(('127.0.0.1',8888))
s.listen(5)

rs,wa,xs = select([s,sys.stdin],[],[],3)
print(rs)