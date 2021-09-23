s = "AB"
n = 1

# 문자
def solution(s, n):
    answer =''
    for a in s:
        if 65<= ord(a) <= 90:
            if ( ord(a) + n ) >= 91:
                answer+=(chr(ord(a)+n-26))
            else:
                answer+=(chr(ord(a)+n))
        elif 97<= ord(a) <= 122:
            if ( ord(a) + n ) >= 123:
                answer+=(chr(ord(a)+n-26))
            else:
                answer+=(chr(ord(a)+n))
        else:
            answer+' '
    return answer

print(solution(s, n))

# 리스트
def solution(s, n):
    s = list(s)
    answer =[]
    for i in range(len(s)):
        if 65<= ord(s[i]) <= 90:
            if ( ord(s[i]) + n ) >= 91:
                answer.append(chr(ord(s[i])+n-26))
            else:
                answer.append(chr(ord(s[i])+n))
        elif 97<= ord(s[i]) <= 122:
            if ( ord(s[i]) + n ) >= 123:
                answer.append(chr(ord(s[i])+n-26))
            else:
                answer.append(chr(ord(s[i])+n))
        else:
            answer.append(" ")
    return "".join(answer)