# Chef and Operations
t = int(input())
if t < 1 or t > int(1e3):
    sys.exit()
for i in range(0, t):
    n = int(input())
    if n < 1 or n > int(1e5):
        sys.exit()
    a = [int(x) for x in input().split()]
    for i in range(0, len(a)):
        if a[i] < 0 or a[i] > int(1e8):
            sys.exit()
    b = [int(x) for x in input().split()]
    for i in range(0, len(a)):
        if b[i] < 0 or b[i] > int(1e8):
            sys.exit()
    index = b.index(max(b))
    if b[index - 1] >= b[index] or b[index - 2] >= b[index] or b[index + 1] >= b[index] or b[index + 2] >= b[index]:
        print("NIE")
    else:
        print("TAK")
    