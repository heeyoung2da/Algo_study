# 에디터 > 시간초과: 스택사용!
import sys
read = sys.stdin.readline

stack1 = list(read().rstrip())
stack2=[]
N = int(read())

for _ in range(N):
    val = read().split()
    # 커서를 왼쪽으로 한 칸
    if val[0] == "L":
        if stack1:
            stack2.append(stack1.pop())
    # 커서를 오른쪽으로 한 칸
    elif val[0] == "D":
        if stack2:
            stack1.append(stack2.pop())
            
    elif val[0] == "B":
        if stack1:
            stack1.pop()
        
    elif val[0] == "P":
        stack1.append(val[1])
        
    # print(sentence)
stack1.extend(reversed(stack2))
print("".join(stack1))