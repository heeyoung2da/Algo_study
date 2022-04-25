# 보물
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

tot = 0
for i in range(N):
    tot += A[i]*B[i]

print(tot)
