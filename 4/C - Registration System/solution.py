n = int(input())
entries = [input() for _ in range(n)]
d = {}
for name in entries:
    if name not in d:
        print('OK')
        d[name] = 1
    else:
        print(name + str(d[name]))
        d[name] += 1