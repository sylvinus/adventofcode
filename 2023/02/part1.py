import re
s = 0
colors = ("red", "green", "blue")
maxcounts = (12, 13, 14)
for line in open("input.txt", "r").readlines():
    picks = tuple(tuple(int((re.search("(\d+) "+c, p) or [0, 0])[1]) for c in colors) for p in line.strip().split(";"))
    if all(all(z[0] >= z[1] for z in zip(maxcounts, p)) for p in picks):
        s += int(re.search("Game (\d+)", line)[1])
print(s)