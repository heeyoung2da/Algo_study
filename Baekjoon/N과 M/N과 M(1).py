from itertools import permutations
import sys

read = sys.stdin.readline

# n, m = map(int, read().rstrip().split())

# arr=[]
# for i in range(1, n+1):
#     arr.append(i)

# a = "\n".join(list(map(" ".join, permutations(map(str, arr),m))))
# print(a)

# a = list(permutations(map(str,arr), m))
# for i in a:
#     print(" ".join(i))

### permutations 다른 풀이
# n , m = map(int, read().rstrip().split())
# p = permutations(range(1, n+1), m)  # iter(tuple)
# for i in p:
#     print(' '.join(map(str, i)))    # tuple -> str


### DFS 풀이
n, m = map(int, read().rstrip().split())
visited = [False] * (n+1)
out = []

def solve(count, n, m):
    # 기저 조건 ( 종료 조건 )
    if count == m:
        print(' '.join(map(str, out)))
        return
    
    # 유도 파트
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            out.append(i)
            solve(count+1, n, m)
            
            visited[i] = False
            print(f'out : {out.pop()}')

solve(0, n, m)

