n = int(input())
s = input()
d = {}
ans = 0
for i in range(0, len(s), 2):
    key = s[i]
    door = s[i+1].lower()
    d[key] = d.get(key, 0) + 1
    if d.get(door, 0) > 0:
        d[door] -= 1
    else:
        ans += 1
print(ans)