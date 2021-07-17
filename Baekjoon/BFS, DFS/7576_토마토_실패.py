# 상자의 크기 m, n
# 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토 X
# 어려웠던 점? 하나의 기준으로 나아가는 것이 아니라 동시에 여러 지점에서 시작
# 시간 초과

import sys
from collections import deque
read = sys.stdin.readline

m, n = map(int, input().split())

tomaBox =[]
for _ in range(n):
    tomaBox.append(list(map(int, read().rstrip().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * m for _ in range(n)]

def bfs(x,y):

    print('x=',x,' y=',y)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue

        # 익지 않은 토마토일 때
        if tomaBox[nx][ny] == 0:
            tomaBox[nx][ny] = 1

cnt = 0
chk = False
while 1:
    oneToma = []    
    # 1. 전체 토마토 상자에서 익은 토마토(1)를 찾아 oneToma 리스트에 넣는다.
    for i in range(n):
        for j in range(m):
            if tomaBox[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                oneToma.append((i,j))
    if len(oneToma) < 1:
        if tomaBox[i][j] == 0:
            chk = True
        break
            
    # 2. 리스트에 있는 값 bfs
    print(oneToma)
    for i in range(len(oneToma)):
        bfs(oneToma[i][0], oneToma[i][1])
    
    cnt += 1
    print('cnt= ', cnt)

# 토마토가 다 익지 못하면
# for i in range(n):
#     for j in range(m):
#         if tomaBox[i][j] == 0:
#             cnt = 0    
if chk:
    cnt = 0
print(cnt-1)    
