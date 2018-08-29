# String Palindrome

s = input()
if len(s) < 1 or len(s) > 100:
    sys.exit()
else:
    c = 0
    for i, j in zip(range(0, len(s)), range(len(s)-1, -1, -1)):
        if s[i] != s[j]:
            c = 1
    if c == 0:
        print("YES")
    else:
        print("NO")
            