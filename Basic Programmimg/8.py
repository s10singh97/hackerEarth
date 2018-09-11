# Toggle String

s = input()
if len(s) > 100 or len(s) < 1:
    sys.exit()
for i in range(0, len(s)):
    if ord(s[i]) >= 65 or ord(s[i]) <= 90:
        s[i] = int(ord(s[i]) + 32)
        s[i] += chr(s[i])
    if ord(s[i]) >= 97 or ord(s[i]) <= 122:
        s[i] = int(ord(s[i]) - 32)
        s[i] += chr(s[i])
print(s)