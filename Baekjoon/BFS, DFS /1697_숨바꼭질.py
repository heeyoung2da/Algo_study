from collections import deque

n, k = map(int, input().split())

def bfs():
    queue = deque([n])

    while queue:
        x = queue.popleft()

        if x == k:
            print(dist[x])
            break

        for nx in(x-1, x+1, x*2):
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[x]+1
                # print(f'dist[{nx}]: {dist[nx]}')
                queue.append(nx)

# 시간초과 안나게 수 제한
MAX = 10 ** 5 

# 이동하는 거리
dist = [0] * (MAX+1)

bfs()