arr = [4,3,2,1]

def solution(arr):
    answer = []
    arr.remove(min(arr))
    if len(arr) == 0:
        answer.append(-1)
    else:
        answer = arr
    return answer

print(solution(arr))