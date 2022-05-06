t = int(input())

# 유클리드 호제법
def uc(x, y):
    while(y):
        x, y = y, x%y
    
    return x

for _ in range(t):
    a, b = map(int, input().split())
    
    # 최소공배수
    print((a*b)//uc(a,b))