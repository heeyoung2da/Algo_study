n = 5
lost = [2,4]
reserve = [3]

def solution(n, lost, reserve):
    n_lost = []
    n_reserve=[]
    n_lost = list(set(lost)-set(reserve))
    n_reserve = list(set(reserve)-set(lost))
    
    for i in n_reserve:
        if i-1 in n_lost:
            n_lost.remove(i-1)
        elif i+1 in n_lost:
            n_lost.remove(i+1)

    return n-len(n_lost)


print(solution(n,lost,reserve))