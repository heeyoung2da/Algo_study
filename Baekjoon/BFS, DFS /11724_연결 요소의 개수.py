from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

def bfs(start):
    queue = deque([(start)])

    while queue:
        this = queue.popleft()

        for i in graph[this]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return 1

cnt = 0
for i in range(1,n+1):
    if not visited[i]:
        cnt += bfs(i)

print(cnt)