n = 15
arr = []
total = 0
cnt = 0

def solution(n):
    arr = []
    total = 0
    cnt = 0

    for i in range(1, n + 1):
        arr.append(i)

    first = 0

    while (first <= n):
        for i in range(first, len(arr)):
            total += int(arr[i])
            if total > n:
                break
            elif total == n:
                cnt += 1
                break

        first += 1
        total = 0

    return cnt

print(solution(n))