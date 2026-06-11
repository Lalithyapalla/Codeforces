import sys
 
def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
    
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        n = int(data[i])
        
        c1 = n // 3
        c2 = n // 3
        remainder = n % 3
        
        if remainder == 1:
            c1 += 1
        elif remainder == 2:
            c2 += 1
            
        results.append(f"{c1} {c2}")
    
    print("
".join(results))
solve()