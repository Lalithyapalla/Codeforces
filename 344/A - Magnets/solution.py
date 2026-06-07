n = int(input())
magnets = []
for _ in range(n):
    magnets.append(input())
count = 1 
for i in range(0, n - 1):
    char = magnets[i]
    first = char         
    char2 = magnets[i + 1]
    prev = char2          
    
    if first != prev:
        count += 1
 
print(count)
    