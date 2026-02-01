import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().split())

dict = {}

for _ in range(N):
    word = sys.stdin.readline().rstrip()

    if len(word) < M : continue

    if word not in dict:
        dict[word] = 1
    else:
        dict[word] = dict[word] + 1

sorted_items = sorted(
    dict.items(),
    key=lambda x: (-x[1], -len(x[0]), x[0])
)

for key, value in sorted_items:
    print(key)