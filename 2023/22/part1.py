arange = lambda b, d: range(b[0][d], b[1][d]+1, 1 if b[0][d] <= b[1][d] else -1)
bricks = [[[int(c) for c in e.split(",")] for e in b.split("~")] for b in open("input.txt").read().splitlines()]
bricks = list(sorted([{(z, x, y) for x in arange(b, 0) for y in arange(b, 1) for z in arange(b, 2)} for b in bricks], key=lambda b: min(b)))
index = {c: i for i, b in enumerate(bricks) for c in b}
supports = lambda i: set(index[(c[0]-1, c[1], c[2])] for c in bricks[i] if index.get((c[0]-1, c[1], c[2])) not in {None, i})
moved = True
while moved:
    moved = False
    for i in range(len(bricks)):
        while all(c[0]>1 for c in bricks[i]) and len(supports(i)) == 0:
            for c in bricks[i]:
                index.pop(c)
            bricks[i] = {(c[0]-1, c[1], c[2]) for c in bricks[i]}
            for c in bricks[i]:
                index[c] = i
            moved = True
optional = set(range(len(bricks)))
for i in range(len(bricks)):
    s = supports(i)
    if len(s) == 1:
        optional = optional.difference(s)
print(len(optional))