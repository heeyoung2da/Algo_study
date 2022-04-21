# 숫자카드
N = int(input())
sang = sorted(map(int, input().split()))
M = int(input())
cards = map(int, input().split())

def binary(target):
    left = 0
    right = N-1
    
    while left <= right: 
        mid = (left+right)//2
        
        if sang[mid] == target:
            return True
        
        if target < sang[mid]:
            right = mid-1
        elif target > sang[mid]:
            left = mid+1
            
for target in cards:
    if binary(target):
        print(1, end=' ')
    else:
        print(0, end=' ')
    