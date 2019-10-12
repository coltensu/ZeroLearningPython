"""
range(start, stop[, step])
start: 从 start 开始
stop: 到 stop 介绍，但是不包括 stop
"""
import random

answer = random.randint(1, 100)
print(answer)

for i in range(3, 10):
    if i % 2 == 0:
        print(i)
else:
    print('wtf', i)
