s = open("input.txt").read()
for i in range(14, len(s)):
    if len(set(s[i-14:i])) == 14:
        break
print(i)