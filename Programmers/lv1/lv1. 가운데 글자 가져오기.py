s = 'abcdef'

def solution(s):
    answer = ''
    length = int(len(s) / 2)
    if len(s)%2 == 0:
        answer = s[length - 1:length + 1]
    else:
        answer = s[length]

    return answer

print(solution(s))