# Trailing Zeroes in Factorial
import math

def factorial_cap(num):
    n = 1
    i = 1
    while n < num:
        i += 1   
        n *= i
    return i

def range_prod(lo,hi):
    if lo+1 < hi:
        mid = (hi+lo)//2
        return range_prod(lo,mid) * range_prod(mid+1,hi)
    if lo == hi:
        return lo
    return lo*hi

def treefactorial(n):
    if n < 2:
        return 1
    return range_prod(1,n)

t = int(input())
for i in range(0, t):
    m = int(input())
    if m < 1 or m > 100000:
        sys.exit()
    ar = [];  aa = []
    for i in range(0, 10000):
        ar.append(treefactorial(i))
    for i in range(0, len(ar)):
        count = 0
        n = ar[i]
        while(ar[i]):
            d = ar[i] % 10
            if d == 0:
                count += 1
            else:
                break
            ar[i] = ar[i] // 10
        if count == m:
            aa.append(factorial_cap(n))
    print(len(aa))
    for i in aa:
        print(i, end=" ")
