import re, collections, math
gears = collections.defaultdict(list)
lines = open("input.txt", "r").read().split("\n")
for x, line in enumerate(lines):
    for m in re.finditer("\d+", line):
        y = m.start()
        l = len(m.group())
        border = ((x, y-1), (x, y+l)) + tuple((x-1, y-1+i) for i in range(l+2)) + tuple((x+1, y-1+i) for i in range(l+2))
        for (xt, yt) in border:
            if 0 <= xt < len(lines) and 0 <= yt < len(line) and lines[xt][yt] == "*":
                gears[(xt, yt)].append(int(m.group()))
print(sum([math.prod(g) for g in gears.values() if len(g) == 2]))