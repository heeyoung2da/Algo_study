from collections import deque
import sys
read = sys.stdin.readline

# 입력
n, m = map(int, input().split())
miro = []
for i in range(n):
    miro.append(list(map(int, read().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque([(x,y)])

    while queue:
        
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            # 미로 1일 때 이동
            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y]+1
                queue.append((nx, ny))

    return miro[n-1][m-1]

print(bfs(0,0))


