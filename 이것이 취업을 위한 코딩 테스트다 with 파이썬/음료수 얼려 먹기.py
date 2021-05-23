# NxM
from collections import deque
import sys
read = sys.stdin.readline

dy = [-1, 0, 0, 1] # 상 좌 우 하
dx = [0, -1, 1, 0] # 상 좌 우 하
n, m = map(int, input().split())

iceArr = [0] * n
visited = [[False] * m for _ in range(n)]
for i in range(n):
    iceArr[i] = list(map(int, read().rstrip()))

def BFS(a, b):
    queue = deque([[a, b]])
    while queue: 
        nowa, nowb = queue.popleft()
        visited[nowa][nowb] = True
        for k in range(4):
            nexta = nowa + dy[k]
            nextb = nowb + dx[k]
            if 0 <= nexta < n and 0 <= nextb < m:
                if iceArr[nexta][nextb] == 0 and not visited[nexta][nextb]:
                    queue.append([nexta,nextb])


cnt = 0
for i in range(n):
    for j in range(m):
        
        if iceArr[i][j] == 0 and not visited[i][j]: 
            BFS(i,j)
            cnt += 1
        
print(f'답은요 : {cnt}')