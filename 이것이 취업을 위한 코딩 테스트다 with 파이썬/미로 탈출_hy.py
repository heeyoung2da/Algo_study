from collections import deque

n, m = map(int, input().split())

miroArr = [[0] for _ in range(n)]

for i in range(n):
    miroArr[i] = list(map(int, input()))

# 방향 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def miro(x, y):

    queue = deque([[x, y]])

    while queue:
        
        x, y = queue.popleft() 

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:

                if miroArr[nx][ny] == 1:
                    queue.append([nx, ny])
                    miroArr[nx][ny] = miroArr[x][y]+1

    return miroArr[n-1][m-1]                


print(miro(0,0))