n = int(input())
x_input = list(map(int, input().split()))
xlevels = x_input[1:]
y_input = list(map(int, input().split()))
ylevels = y_input[1:]
combined = set(xlevels + ylevels)
if len(combined) == n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')