n = int(input())
s = input()
unique = set(s.lower())
if len(unique) == 26:
    print('YES')
else:
    print('NO')