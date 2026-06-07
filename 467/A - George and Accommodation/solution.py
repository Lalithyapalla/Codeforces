n = int(input())
count = 0
for i in range(n):
    val = list(map(int,input().split()))
    if (val[1] - val[0]) >=2 :
        count += 1
print(count)