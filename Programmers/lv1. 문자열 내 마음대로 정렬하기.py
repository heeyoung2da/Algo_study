strings = ['sun', 'bed', 'car']
n = 1


def solution(strings, n):
    strings.sort()
    tmp=[]
    for i in range(len(strings)):
        tmp.append(strings[i][n])
    new = dict(x for x in zip(strings, tmp))
    result = dict(sorted(new.items(), key=lambda x: x[1]))
    result = list(result.keys())


    return result

print(solution(strings, n))