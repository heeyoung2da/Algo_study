# 달팽이는 올라가고 싶다 -- 시간초과

A, B, V = map(int, input().split())
day = 0
while V>0:
    day += 1
    V = V-A
    if V<=0:
        break
    
    V = V+B
    # print(V, day)

print(day)
    
