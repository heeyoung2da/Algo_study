# from itertools import combinations
import sys

read = sys.stdin.readline

n, m = map(int, read().rstrip().split())

# c = combinations(range(1, n+1), m)
# for i in c:
#     print(" ".join(map(str, i)))


### DFS
out=[0] * m

def solution(cnt, k):
    #기저 조건
    if cnt == m:
        print(' '.join(map(str, out)))
        return


    #유도 파트
    for i in range(k, n+1):
        out[cnt] = i
        solution(cnt+1, i+1)

solution(0, 1)