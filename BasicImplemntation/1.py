# count numbers
t = int(input())
if t <= 0 and t >= 200:
    sys.exit()

for i in range(0, t):
    n = int(input())
    if n <= 0 and n >= 10e4:
        sys.exit()
    s = input()
    if len(s) != n:
        sys.exit()
    count = 0
    for i in range(0, len(s)):
        if ord(s[i]) >= 48 and ord(s[i]) <= 57:
            count += 1    
        else:
            s = s.replace(s[i], '\0')
    #print(s)
    s = s.split('\0')
    c = 0
    #print(s)
    for i in s:
        if i != '':
            c += 1
    print(c)