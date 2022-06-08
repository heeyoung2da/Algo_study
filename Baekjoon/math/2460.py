# 지능형 기차2
max = 0
tot = 0

for _ in range(10):
    outCnt, inCnt = map(int, input().split())
    tot -= outCnt
    tot += inCnt
    
    if max<tot:
        max = tot


print(max)
    