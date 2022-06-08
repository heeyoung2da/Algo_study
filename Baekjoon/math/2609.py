# 최대공약수와 최소공배수
# 유클리드 호제법
# a와 b의 최대공약수 G는 b와 a%b의 최대공약수 G'와 서로 같다.
# gcd(24, 18) = gcd (18, 6) = gcd(6,0)
# 최소공배수는 A*B / gcd(a,b)

a, b = map(int, input().split())

def gcd(a, b):
    while b>0:
        a, b = b, a%b
    
    return a

def lcm(a, b):
    return a*b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))