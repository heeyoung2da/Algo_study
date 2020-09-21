participant = ['mislav', 'stanko', 'mislav', 'ana']
completion = ['stanko', 'ana', 'mislav']

participant.sort()
completion.sort()

def solution(participant, completion):
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[-1]

print(solution(participant, completion))