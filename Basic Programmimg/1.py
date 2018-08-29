# Primes uptil 'n'

a = int(input())
if a > 1000 and a < 1:
    sys.exit()
else:
    for i in range(2, a+1):
        c = 0
        for j in range(1, int(i/2) + 1):
            if i % j == 0:
                c += 1
        if c == 1:
            print(i, " ", end="")
