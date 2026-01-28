import sys
import math

N, K = map(int,sys.stdin.readline().split())

answer = math.factorial(N) / (math.factorial(K) * math.factorial(N-K))
print(int(answer))