a = [int(x) for x in input().split()]
for i in a:
    if i < 1 or i > 10e6:
        sys.exit()

b = [int(x) for x in input().split()]
for i in range(0, a[1]):
    c = [int(x) for x in input().split()]
    mean = int((b[c[0] - 1] + b[c[1] - 1]) / 2)
    print(mean)