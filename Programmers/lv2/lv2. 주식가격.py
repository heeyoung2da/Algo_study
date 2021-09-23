prices = [1,2,3,2,3]

def solution(prices):
    result = [0] * len(prices)

    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            if prices[i]>prices[j]:
                result[i] = j-i
                break
            else:
                result[i] = len(prices)-1-i
    return result


print(solution(prices))
