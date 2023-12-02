import re, math
s = 0
colors = ("red", "green", "blue")
for line in open("input.txt", "r").readlines():
    picks = tuple(tuple(int((re.search("(\d+) "+c, p) or [0, 0])[1]) for c in colors) for p in line.strip().split(";"))
    s += math.prod(max(z) for z in zip(*picks))
print(s)