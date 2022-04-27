# 중복 빼고 정렬하기
N = int(input())
arr = list(map(int, input().split()))
arr.sort()
arr= list(set(arr))

for i in range(len(arr)):
    print(arr[i], end=" ")