# Find Product

n = int(input())
if n < 1 and n > 1000:
    sys.exit()
else:
    a = [int(x) for x in input().split()]
    for i in range(0, len(a)):
        if a[i] < 1 and a[i] > 1000:
            sys.exit()
    ans = 1
    div = int(1e9 + 7)
    for i in range(0, len(a)):
        ans = (ans * a[i]) % (div)
    print(ans)
