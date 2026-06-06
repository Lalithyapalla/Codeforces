n, k = list(map(int, input().split()))
points = list(map(int, input().split()))
res = 0
for val in range(n):
    if ( points[val] >= points[k-1]) and ( points[val] > 0 ):
        res += 1
print(res)