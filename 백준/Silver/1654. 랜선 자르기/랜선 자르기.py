def cuting(value, l):
    count = sum(k // value for k in L)
    return count

def get_max_length_of_LAN(start, end, target, l):
    if (start > end):
        return end
    
    mid = (start + end) // 2
    count = cuting(mid, l)
    
    if count >= target:
        return get_max_length_of_LAN(mid+1, end, target, l)
    elif count < target:
        return get_max_length_of_LAN(start, mid-1, target, l);

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
L = [int(input()) for _ in range(N)]

max_length_of_LAN = get_max_length_of_LAN(1, max(L), K, L)

print(max_length_of_LAN);