# 요세푸스 문제
from collections import deque
N, K = map(int, input().split())
queue = deque()
for i in range(1, N+1):
    queue.append(i)

stack = []
while len(queue)>0:
    for _ in range(K-1):
        queue.append(queue.popleft())
    
    stack.append(queue.popleft())
    
print("<", end="")
for i in range(len(stack)):
    if i == len(stack)-1:
        print(stack[i], end="")
    else:
        print(stack[i], end=", ")    
print(">")
