# Spread the word
import sys

def main():
    try:
        t = int(sys.stdin.buffer.readline())
    except:
        sys.exit(1)
    if t < 1 or t > 10000:
        sys.exit(1)
    for  i in range(0, t):
        try:
            n = int(sys.stdin.buffer.readline())
        except:
            sys.exit(1)
        if n < 2 or n > 100000:
            sys.exit(1)
        try:
            a = [int(x) for x in sys.stdin.buffer.readline().split()]
        except:
            sys.exit(1)
        for i in range(1, len(a)):
            if a[i] < 0 or a[i] > n:
                sys.exit(1)
        if a[0] < 1:
            sys.exit(1)
        s = 1
        count = 1
        s += a[0]
        if s >= n:
            print(count)
        else:
            while(s < n):
                for y in range(0, s):
                    s += a[i]
                count += 1
            print(count)   
    sys.exit(0)

main()