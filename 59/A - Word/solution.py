s = input()
upper = ''
lower = ''
for char in s:
    if 65 <= ord(char) <= 90:
        upper += char
    if 97 <= ord(char) <= 122:
        lower += char
if len(upper) == len(lower):
    print(s.lower())
elif len(lower) > len(upper):
    print(s.lower())
else:
    print(s.upper())