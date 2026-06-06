s = input()
l = []
for char in s:
    if char not in l:
        l.append(char)
print('CHAT WITH HER!' if (len(l) % 2 == 0) else 'IGNORE HIM!')