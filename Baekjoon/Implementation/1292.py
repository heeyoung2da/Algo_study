# 쉽게 푸는 문제
tot = 0
cnt = 0
check = False
n = 1
A, B = map(int, input().split())

while True:
    if check:
        break

    for i in range(n):
        cnt += 1        
        if A<=cnt<=B:
            tot += n
        
        if cnt>B:
            check = True
    
    n+=1

print(tot)