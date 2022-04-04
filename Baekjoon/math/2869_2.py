# 달팽이는 올라가고 싶다 
# 낮에 올라간 높이가 그 날의 최대 높이가 됨

import math

A, B, V = map(int, input().split())
print(math.ceil((V-B)/(A-B)))