import math

n = 121

def solution(n):
    answer = 0
    if math.sqrt(n) == int(math.sqrt(n)):
        answer = (int(math.sqrt(n))+1)*(int(math.sqrt(n))+1)
    else:
        answer = -1
    return answer

print(solution(n))