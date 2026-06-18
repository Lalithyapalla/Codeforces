def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = input().split()
        left = 0
        right = n - 1
        original = []
        while left <= right:
            if left == right:
                original.append(b[left])
                break
            original.append(b[left])
            original.append(b[right])
            left += 1
            right -= 1
        print(" ".join(original))
solve()