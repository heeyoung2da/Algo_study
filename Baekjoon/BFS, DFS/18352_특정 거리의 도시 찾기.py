### 특정 거리의 도시 찾기
from collections import deque

# 입력
n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [False] * (n+1)
ans = []
def bfs(start):
    # [출발도시, 거리] 
    # queue = deque([(start, 0)])
    queue = deque()
    queue.append((start, 0))
    visited[start] = True

    while queue:
        now, dist = queue.popleft()

        # 최단 거리 k에 도달하면
        if dist == k:
            ans.append(now)
        elif dist > k:
            return ans

        for i in graph[now]:
            if not visited[i]:
                next, ndist = [i, dist+1]
                queue.append((next, ndist))
                # queue.append((i, dist+1))
                
                visited[i] = True

    if len(ans) < 1:
        ans.append(-1)
    
    return ans

res = bfs(x)
res.sort()
print('\n'.join(map(str, res)))

# if ans:
#     ans.sort()
#     print(*ans, sep='\n')
# else:
#     print(-1)