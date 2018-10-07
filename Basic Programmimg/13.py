# Minimize Cost

a = [int(x) for x in input().split()]
if a[0] < 1 or a[1] < 1 or a[0] > 10e5 or a[1] > 10e5:
    sys.exit()
b = [int(x) for x in input().split()]
for i in range(0, len(b)):
    if b[i] > 10e9 or b[i] < -10e9:
        sys.exit()
    