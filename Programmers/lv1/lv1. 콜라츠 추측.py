num = 626331

def solution(num):
    answer = 0
    while True:
        print("num:", num)
        print("answer:", answer)
        if answer >= 500:
            answer = -1
            break
        elif num % 2 == 0:
            num =int(num / 2)
            answer += 1
        elif num == 1:
            break
        elif num % 2 == 1:
            num = num * 3 + 1
            answer += 1

    return answer

print(solution(num))