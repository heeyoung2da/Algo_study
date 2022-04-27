# 숫자 카드 2
# Counter는 리스트를 값으로 주게 되면 해당 원소들이 몇 번 등장했는지 딕셔너리 형태로 반환
import sys
from collections import Counter
read = sys.stdin.readline

N = int(read())
sang = list(read().split())
M = int(read())
cards = list(read().split())

count = Counter(sang)
# print(count)

for card in cards:
    if card in count:
        print(count[card], end=" ")
    else:
        print(0, end=" ")