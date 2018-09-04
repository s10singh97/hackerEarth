n = int(input())

if n < 1 or n > 10:
    sys.exit()

fact = 1
while n != 0:
    fact = fact * n
    n -= 1
print(fact)