s = 'try  hello world'
list = s.split()

def solution(s):
    list = s.split(" ")
    answer =[]
    for i in range(len(list)):
        for j in range(len(list[i])):
            if j % 2 == 0:
                answer.append(list[i][j].upper())
            else:
                answer.append(list[i][j].lower())
        answer.append(" ")
    result="".join(answer[:-1])

    return result

print(solution(s))

# 다른 사람 풀이
def solution(s):
    answer = ''
    lst = []
    dan = s.split(' ')
    for i in range(len(dan)) :
        ans = ''
        for j in range(len(dan[i])) :
            if j % 2 == 0 :
                ans += dan[i][j].upper()
            else :
                ans += dan[i][j].lower()
        lst.append(ans)
    answer = ' '.join(lst)
    return answer