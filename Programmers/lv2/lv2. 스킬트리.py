skill = 'CBD'
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

def solution(skill, skill_trees):
    answer = 0

    for i in skill_trees:
        list = []
        fin = True

        for j in range(len(i)):
            if i[j] in skill:
                list.append(i[j])

        for k in range(len(list)):
            if list[k] != skill[k]:
                fin = False
                break

        if fin == True:
            answer += 1

    return answer

print(solution(skill, skill_trees))