def solve():
    n = int(input())
    d = list(map(int, input().split()))
    
    a = [0] * n
    a[0] = d[0]
    
    for i in range(1, n):
        if d[i] != 0 and a[i-1] - d[i] >= 0:
            print(-1)
            return
        a[i] = a[i-1] + d[i]
        
    print(*a)
 
t = int(input())
for _ in range(t):
    solve()