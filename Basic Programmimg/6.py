# Divisor Count

a = [int(x) for x in input().split()]

if a[0] > 1000 or a[1] < 1:
    sys.exit()
if a[1] > 1000 or a[1] < 1:
    sys.exit()
if a[2] > 1000 or a[2] < 1:
    sys.exit()

c = 0
for i in range(a[0], a[1] + 1):
    if i % a[2] == 0:
        c += 1

print(c)