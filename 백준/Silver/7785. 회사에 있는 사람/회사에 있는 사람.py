n = int(input())

log = dict()
for i in range(n):
    name, status = input().split()
    if status == "enter":
        log[name] = True
    else:
        log[name] = False

log = dict(sorted(log.items(), reverse=True))

for name in log:
    if log[name]:
        print(name)
