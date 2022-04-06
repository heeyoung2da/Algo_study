# 수 찾기
import sys
read = sys.stdin.readline
N = int(input())
A = sorted(map(int, read().rstrip().split(" ")))
M = int(input())
B = map(int, read().rstrip().split(" "))

def binary(target):
    left = 0
    right = N-1
    
    while left <= right:
        mid = (left+right)//2
        if A[mid] == target:
            return True
        
        if target < A[mid]:
            right = mid-1
        elif target > A[mid]:
            left = mid +1
            
for target in B:
    if binary(target):
        print(1)
    else:
        print(0)