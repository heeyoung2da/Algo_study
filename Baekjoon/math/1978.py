# 소수 찾기
N = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in range(N):
    if arr[i] == 1:
        continue
    
    isSosu = True
    
    for j in range(2, arr[i]):
        if arr[i] % j == 0:
            isSosu = False
    
    if isSosu:
        cnt+=1

print(cnt)