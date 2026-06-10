n = int(input())
coins = sorted(map(int, input().split()), reverse=True)
total_sum = sum(coins)
sum = 0
for i, coin in enumerate(coins):
    sum += coin
    if sum > total_sum - sum:
        print(i + 1)
        break