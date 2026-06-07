n = int(input())
count = 0
for dig in str(n):
    if dig == '4' or dig == '7':
        count += 1
        continue
else:
    print('YES' if (count == 4 or count == 7) else 'NO')