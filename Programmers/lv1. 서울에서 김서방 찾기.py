seoul = ['Jane', 'Kim']

def solution(seoul):
    answer = ''
    answer = '김서방은 '+ str(seoul.index("Kim")) +'에 있다'
    return answer


print(solution(seoul))