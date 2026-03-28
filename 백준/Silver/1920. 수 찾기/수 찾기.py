import sys

def binary_search(k, L , start, end):
    mid = (start + end) // 2

    if L[mid] == k:
        return 1
    
    if start >= end:
        return 0
    
    if k < L[mid]:
        return binary_search(k, L, start, mid - 1)
    else:
        return binary_search(k, L, mid + 1, end)

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))

A.sort()

for value in T:
    result = binary_search(value, A, 0, len(A) - 1)
    print(result)