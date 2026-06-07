n = int(input())
s = input()
anton = 0
for char in s:
    if char == 'A':
        anton += 1
dan = len(s) - anton
if anton > dan:
    print('Anton')
elif anton < dan:
    print('Danik')
else:
    print('Friendship')