def solution(answers):
    answer = []
    ans = []
    c1 = 0
    c2 = 0
    c3 = 0
    first = [1, 2, 3, 4, 5] * int(len(answers))
    first = first[:len(answers)]
    second = [2, 1, 2, 3, 2, 4, 2, 5] * int(len(answers))
    second = second[:len(answers)]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * int(len(answers))
    third = third[:len(answers)]
    answer = [0, 0, 0]

    for i, j in zip(first, answers):
        if i == j:
            c1 = c1 + 1
            answer[0] = c1
    for i, j in zip(second, answers):
        if i == j:
            c2 = c2 + 1
            answer[1] = c2
    for i, j in zip(third, answers):
        if i == j:
            c3 = c3 + 1
            answer[2] = c3

    mx = max(answer)
    for x in range(3):
        if answer[x] == mx:
            ans.append(x + 1)

    return ans


print(solution(answers=[1,2,3,4,5]))