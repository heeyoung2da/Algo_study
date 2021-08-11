import sys
from collections import deque
read = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
queue = deque()

def bfs():
    global cnt

    while queue:
        size = len(queue)
        for i in range(size):
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if(0<=nx<N) and (0<=ny<M) and arr[nx][ny] == 0:
                    arr[nx][ny] = 1
                    queue.append((nx,ny))

        cnt += 1

M, N = map(int, input().split())

arr = []
for i in range(N):
    arr.append(list(map(int, read().split())))

cnt = 0
check = True
# 토마토 1 담기
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            queue.append((i,j))

bfs()

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            cnt = 0
print(cnt-1)




