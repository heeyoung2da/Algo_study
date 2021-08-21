import sys
from collections import deque

read = sys.stdin.readline

def bfs():

    # 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    days = -1

    while oneToma:
        days += 1
        for _ in range(len(oneToma)):
            x, y = oneToma.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if(0<= nx < n) and (0<= ny < m) and (tomaBox[nx][ny]==0):
                    tomaBox[nx][ny] = tomaBox[x][y] + 1
                    oneToma.append([nx, ny])
    
    for toma in tomaBox:
        if 0 in toma:
            return -1
    return days
    
m, n = map(int, input().split())
tomaBox, oneToma =[], deque()
for i in range(n):
    row = list(map(int, read().rstrip().split()))
    for j in range(m):
        if row[j] == 1:
            oneToma.append([i, j])
    tomaBox.append(row)

print(bfs())