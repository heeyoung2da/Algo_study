# 1은 집이 있는 곳 0은 집이 없는 곳
# 대각선 X
from collections import deque
import sys

read = sys.stdin.readline

# 입력
n = int(input())

mapArr=[]
for _ in range(n):
    mapArr.append(list(map(int, read().rstrip())))

visited = [[False] * (n+1) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x,y):
    queue = deque([(x,y)])
    visited[x][y] = True
    cnt = 1
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if mapArr[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                cnt += 1
                queue.append((nx,ny))

    return cnt      # 집의 수

ans = []
cnt = 0
for i in range(n):
    for j in range(n):
        if mapArr[i][j] == 1 and not visited[i][j]:
            ans.append(dfs(i,j))
            cnt += 1    #단지수
ans.sort()
ans.insert(0,cnt)
print('\n'.join(map(str, ans)))
