# 책 답안 예시

import sys

read = sys.stdin.readline

n, m = map(int, read().rstrip().split())

iceArr = []
for i in range(n):
    iceArr.append(list(map(int, read().rstrip())))

def dfs(x, y):

    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 현재 노드를 아직 방문하지 않았다면
    if iceArr[x][y] == 0:
        # 해당 노드 방문 처리
        iceArr[x][y] = 1

        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

    # 주변에 0이 있는지 보고 방문
    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                result += 1

print(result)

