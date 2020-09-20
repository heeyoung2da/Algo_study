arr = [1,2,3,4]

def solution(arr):
    answer = 0
    answer += sum(arr) / len(arr)
    return answer

print(solution(arr))