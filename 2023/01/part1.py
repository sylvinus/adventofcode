import re
s = 0
for line in open("input.txt", "r").readlines():
    s += int(re.search("([0-9])", line)[1] + re.search("([0-9])[^0-9]*$", line)[1])
print(s)

