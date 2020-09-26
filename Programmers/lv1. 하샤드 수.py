x = 11

def solution(x):
    answer = True
    arr = list(str(x))
    result = 0
    for i in range(len(arr)):
        result += int(arr[i])

    if int(x) % result == 0:
        answer = True
    else:
        answer = False

    return answer

print(solution(x))