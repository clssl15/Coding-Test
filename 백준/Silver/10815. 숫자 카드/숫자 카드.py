n= int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
arr3 = []

dict = {}
for i in arr1:
    dict[i] = 0

for j in arr2:
    if j in dict:
        print(1, end=' ')
    else:
        print(0, end=' ')