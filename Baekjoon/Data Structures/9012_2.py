#괄호 -> 다른 사람 풀이
N = int(input())

for _ in range(N):
    string = list(input())
    sum = 0
    for s in string:
        if s == '(':
            sum += 1
        elif s == ')':
            sum -= 1
        if sum < 0:
            print("NO")
            break
    
    if sum>0:
        print("NO")
    elif sum == 0:
        print("YES")
    