# Cipher

s = input()
n = int(input())
a = []
st = ""
if n < 0 or n > 1000:
    sys.exit()
k = n % 26
b = 0
for i in range(0, len(s)):
    if ord(s[i]) >= 65 and ord(s[i]) <= 90:
        if (ord(s[i]) + k) > 90:
            b = ord(s[i]) + k - 26
            a.append(chr(b))
        else:
            a.append(chr(ord(s[i]) + k))
    elif ord(s[i]) >= 97 and ord(s[i]) <= 122:
        if (ord(s[i]) + k) > 122:
            b = ord(s[i]) + k - 26
            a.append(chr(b))
        else:
            a.append(chr(ord(s[i]) + k))
    elif ord(s[i]) >= 48 and ord(s[i]) <= 57:
        c = (ord(s[i]) - 48 + n) % 10
        c += 48
        a.append(chr(c))
    else:
        a.append(s[i])
for i in a:
    st += i
print(st)