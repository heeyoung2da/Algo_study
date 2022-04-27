# 스택 수열
N = int(input())
stack = []
cnt = 1
ans = []
avl = True

for i in range(N):
    inputNum = int(input())
    while cnt <= inputNum:
        stack.append(cnt)
        ans.append("+")
        cnt += 1
    
    if stack[-1] == inputNum:
        stack.pop()
        ans.append("-")
    else:
        avl = False

if(avl):
    for i in range(len(ans)):
        print(ans[i])
else:
    print("NO")
        
        