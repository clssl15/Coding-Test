import sys

def cantor_set(S,p,r):
    if (p >= r-1): return

    gap = (r - p) // 3
    i = p + gap
    j = p + (gap * 2)

    for k in range(i, j):
        S[k] = " "

    cantor_set(S, p, i)
    cantor_set(S, j, r)

for line in sys.stdin:
    n = int(line)
    S = ["-" for _ in range(3**n)]
    cantor_set(S, 0, 3**n)
    print("".join(S))