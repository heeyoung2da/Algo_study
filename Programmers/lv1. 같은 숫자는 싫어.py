arr = [1,1,3,3,0,1,1]

def solution(arr):
    answer = []
    answer.append(arr[0])
    j = 0
    for i in range(1,len(arr)):
        if answer[j] == arr[i]:
            continue
        else:
            j = j + 1
            answer.append(arr[i])
    return answer

print(solution(arr))