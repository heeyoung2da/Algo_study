import sys
from collections import deque

read = sys.stdin.readline

# 입력
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, read().rstrip().split())
    graph[a].append(b)
    graph[b].append(a) ### 양방향!!!!!

visited = [False] * (n+1)
def bfs(start):
    queue =deque([(start)])
    cnt = 0

    #현재 노드를 방문 처리
    visited[start] = True

    while queue:
        this = queue.popleft()

        for i in graph[this]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                cnt += 1
    
    return cnt

print(bfs(1))