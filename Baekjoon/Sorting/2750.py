# 수 정렬하기

# N 입력 -> N개의 수 입력
N = int(input())
nums = [0 for i in range(N)]
for i in range(N):
    nums[i] = int(input())

nums.sort()

for i in range(N):
    print(nums[i])