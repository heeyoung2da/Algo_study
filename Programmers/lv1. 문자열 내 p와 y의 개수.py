from collections import Counter

s = 'pPoooyY'

def solution(s):
    answer = True
    count = Counter(s.lower())
    if count['p'] != count['y']:
        answer = False
    return answer

print(solution(s))