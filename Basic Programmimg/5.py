# Two String

t = int(input())
if t > 100 or t < 1:
    sys.exit()
else:
    for i in range(t):
        a = [str(x) for x in input().split()]
        flag = [0]*len(a[0])
        for i in a[0]:
            if i in a[1]:
                a[0] = a[0].replace(i, "")
                a[1] = a[1].replace(i, "")
        if len(a[0]) == 0 and len(a[1]) == 0:
            print("YES")
        else:
            print("NO")
