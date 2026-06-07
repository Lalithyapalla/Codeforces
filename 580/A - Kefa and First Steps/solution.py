n = int(input())
a = list(map(int, input().split()))
 
curr = 1
ans = 1
 
for i in range(1, n):
    if a[i] >= a[i - 1]:
        curr += 1
    else:
        curr = 1
 
    ans = max(ans, curr)
 
print(ans)