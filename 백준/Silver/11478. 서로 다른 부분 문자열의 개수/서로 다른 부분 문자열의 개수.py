S = input()
dict = {}

for i in range(len(S)):
    for j in range(i + 1, len(S) + 1):
        sub = S[i:j]
        if sub not in dict:
            dict[sub] = 1

print(len(dict))