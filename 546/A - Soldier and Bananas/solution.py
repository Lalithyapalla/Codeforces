k, n, w = list(map(int, input().split()))
sum = 0
for i in range(1, w + 1):
    sum = sum + k * i
print(sum - n if (sum - n) > 0 else 0 )