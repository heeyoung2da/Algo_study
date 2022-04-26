# 좌표 정렬하기 2
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x: (x[1], x[0]))

for i in range(N):
    print(arr[i][0], end=" ")
    print(arr[i][1])