# Roy and Profile Picture

l = int(input())
if l < 1 or l > 10000:
    sys.exit()
n = int(input())
for i in range(0, n):
    a = [int(x) for x in input().split()]
    if a[0] < l or a[1] < l:
        print("UPLOAD ANOTHER")
    elif a[0] == a[1]:
        print("ACCEPTED")
    else:
        print("CROP IT")
