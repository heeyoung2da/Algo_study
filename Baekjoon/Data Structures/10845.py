# 큐
from collections import deque
import sys
read = sys.stdin.readline

N = int(read())
queue = deque()
    
for _ in range(N):
    val = read().split()
    
    if val[0] == "push":
        queue.append(val[1])
    elif val[0] == "pop":
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()
    elif val[0] == "size":
        print(len(queue))
    elif val[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif val[0]=="front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif val[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
