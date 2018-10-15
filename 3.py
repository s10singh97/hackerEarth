# Chefs and Semi-Primes

import sys
from numba import jit

@jit(nopython = True)
def fun(n):
    d = []
    for i in range(2, n+1):
        c = 0
        for j in range(1, int(i/2) + 1):
            if i % j == 0:
                c += 1
        if c == 1:
            d.append(i)
    # print(d)
    f = []
    for i in range(0, int(len(d)/2) + 1):
        for j in range(i+1, int(len(d)/2) + 1):
            e = d[i] * d[j]
            f.append(e)
    f.pop()
    # print(f)
    d.clear()
    for i in f:
        if i < n:
            d.append(i)
    d.sort()
    # print(d)
    flag = 0
    for i in range(0, len(d)):
        for j in range(i, len(d)):
            if d[i] + d[j] == n:
                flag = 1
                break
    if flag == 1:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    t = int(input())
    if t < 1 or t > 200:
        sys.exit(1)
    for i in range(0, t):
        n = int(input())
        if n < 1 or n > 200:
            sys.exit(1)
        fun(n)
    sys.exit(0)