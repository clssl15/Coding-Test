n, m = map(int, input().split())
dict = {}
check = {}
for _ in range(n):
    dict[input()] = 0

for j in range(m):
    check[j] = input()

count = 0
for value in check.values():
    if value in dict:
        count += 1

print(count)