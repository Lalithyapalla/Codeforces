def solve():
    n = int(input())
    data = [int(x) for x in input().split()]
    for val in data:
        if val == 1:
            return 'HARD'
    return 'EASY'
print(solve())
            