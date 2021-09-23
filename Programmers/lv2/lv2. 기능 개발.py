progresses = [93, 30, 55]
speeds = [1,30,5]

def solution(progresses,speeds):
    result =[]
    arr=[]

    while len(progresses) != 0:
        if progresses[0] >= 100:
            arr.append(progresses.pop(0))
            speeds.pop(0)

        else:
            progresses = [x+y for x,y in zip(progresses,speeds)]
            if len(arr) != 0:
                result.append(len(arr))
                arr=[]

    result.append(len(arr))
    return result

print(solution(progresses,speeds))