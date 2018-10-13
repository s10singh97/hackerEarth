# Spread the word

t = int(input())
if t < 1 or t > 10000:
    sys.exit()
for  i in range(0, t):
    n = int(input())
    if n < 2 or n > 100000:
        sys.exit()
    a = [int(x) for x in input().split()]
    for i in range(1, len(a)):
        if a[i] < 0 or a[i] > n:
            sys.exit()
    if a[0] < 1:
        sys.exit()
    s = 1
    count = 1
    s += a[0]
    if s >= n:
        print(count)
    else:
        while(s < n):
            for y in range(0, s):
                s += a[i]
            count += 1
        print(count)    
