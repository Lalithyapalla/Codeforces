n = int(input())
d = {}
for _ in range(n):
    name = input()
    if name not in d:
        d[name] = 0
        print('OK')
    else:
        d[name] += 1
        print(f'{name}{d[name]}')