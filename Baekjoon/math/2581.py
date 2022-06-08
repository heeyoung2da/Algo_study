# 소수
# 1보다 큰 자연수 중 1과 자기 자신만을 약수로 가지는 수

M = int(input())
N = int(input())
min = 10001
tot = 0

for i in range(M, N+1):
    check = True
    if i>1:
        for j in range(2, i):
            if i % j == 0:
                check = False
                break
        if check:
            tot += i
            if min > i:
                min = i

if tot == 0:
    print(-1)
else:
    print(tot)
    print(min)