n = int(input())
problems = 0
for _ in range(n):
    p, v, t = list(map(int, input().split()))
    if ( p + v + t ) >= 2:
        problems += 1
print(problems)