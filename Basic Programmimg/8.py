# Toggle String

s = input()
if len(s) > 100 or len(s) < 1:
    sys.exit()
a = []
for i in range(0, len(s)):
    if ord(s[i]) >= 65 and ord(s[i]) <= 90:
        a.append(chr(ord(s[i]) + 32))
    if ord(s[i]) >= 97 and ord(s[i]) <= 122:
        a.append(chr(ord(s[i]) - 32))
sr = ""
for i in a:
    sr = sr + i
print(sr)