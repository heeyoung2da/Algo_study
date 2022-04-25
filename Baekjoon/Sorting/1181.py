import sys
read = sys.stdin.readline
N = int(read())
words = []
for _ in range(N):
    word = read().rstrip()
    if word not in words:
        words.append(word)

words.sort()
words.sort(key=len)

for i in range(len(words)):
    print(words[i])