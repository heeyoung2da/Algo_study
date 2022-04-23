# 스택 > 출력초과
import sys

N = int(sys.stdin.readline())

stack = []
for _ in range(N):
    val = sys.stdin.readline().split()
    if val[0] == "push":
        stack.append(val[1])
    
    elif val[0] == "pop":
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
        
    elif val[0] == "size":
        print(len(stack))
    
    elif val[0] == "top":
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
            
    elif val[0] == "empty":
        if len(stack)==0:
            print(1)
        else:
            print(0)    