from collections import deque

def bfs(x, y):

        queue = deque([(x,y)])
        visited[x][y] = True
        
        while queue:

            x, y = queue.popleft()

            for i in range(4):
            
                nx = x + dx[i]
                ny = y + dy[i]

                if (0<=nx<m) and (0<=ny<n) and cabbage[nx][ny]==1 and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True

T = int(input())
for tc in range(T):

    m, n, k = map(int, input().split())
    cabbage = [[0] * n for _ in range(m)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False] * n for _ in range(m)]

    for i in range(k):
        a, b = map(int, input().split())
        cabbage[a][b] = 1

    cnt = 0
    for i in range(m):
        for j in range(n):
            if cabbage[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    print(cnt)