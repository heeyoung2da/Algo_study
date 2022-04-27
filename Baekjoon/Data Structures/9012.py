#괄호
N = int(input())
ans = []
for _ in range(N):
    string = list(input())
    
    stack = []
    for i in range(len(string)):
        if string[i] == '(':
            stack.append('(')
        elif string[i]==')' and len(stack)>0:
            if stack.pop() != '(':
                stack.append(')')
        else:
            stack.append(')')
        # print(stack)

    if len(stack)>0:
        print("NO")
    else:
        print("YES")