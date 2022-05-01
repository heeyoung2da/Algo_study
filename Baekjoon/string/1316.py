# 그룹 단어 체커
N = int(input())
cnt = 0
for _ in range(N):
    word = list(input())
    error = 0
    
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            newWord = word[i+1:]
            if word[i] in newWord:
                error += 1
                
    if error == 0:
        cnt+= 1
print(cnt)