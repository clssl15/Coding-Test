import sys
import math

N, M = map(int, sys.stdin.readline().split())

ls = list(map(int,sys.stdin.readline().split()))

cnt = 0
ls_n = [0] * (M)

j = 0
for i in range(len(ls)):
    j = (j + ls[i]) % M
    ls_n[j] += 1

cnt += ls_n[0]

for i in range(M):
    cnt += math.comb(ls_n[i], 2)

print(cnt)