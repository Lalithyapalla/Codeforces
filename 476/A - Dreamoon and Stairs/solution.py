def solve():
    n, m = [int(x) for x in input().split()]
    if n < m:
        print(-1)
        return
    min_moves = (n + 1) // 2
    ans = ((min_moves + m - 1) // m) * m
    print(ans)
solve()