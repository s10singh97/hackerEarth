# Finding Teammate

t = int(input())
if t < 1 or t > 1000:
    sys.exit()
for i in range(0, t):
    n = int(input())
    if n < 2 or n > 100000:
        sys.exit()
    s = [int(x) for x in input().split()]
    for i in s:
        if i < 1 or i > int(1e6):
            sys.exit()
    s.sort()
    count = 0
    