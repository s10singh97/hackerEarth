# Seating Arrangement Problem

t = int(input())
ll = []
n = 9
dd = ['WS', 'MS', 'AS', 'AS', 'MS', 'WS']
if t < 1 and t > 1e5:
    sys.exit()
else:
    for i in range(0, t):
        s = int(input())
        if s < 1 and s > 108:
            sys.exit()
        else:
            for i in range(1, n + 1):
                an = 13 + (i - 1)*24
                ll.append(an)
            d = int(s / 12)
            if s % 12 == 0:
                seat = ll[d - 1] - s
            else:
                seat = ll[d] - s
            print(seat, end = ' ')
            e = s % 6
            if e == 0:
                print(dd[0])
            else:
                print(dd[e - 1])