arange = lambda b, d: range(b[0][d], b[1][d]+1, 1 if b[0][d] <= b[1][d] else -1)
init = [[[int(c) for c in e.split(",")] for e in b.split("~")] for b in open("input.txt").read().splitlines()]
init = list(sorted([{(z, x, y) for x in arange(b, 0) for y in arange(b, 1) for z in arange(b, 2)} for b in init], key=lambda b: min(b)))
supports = lambda bricks, index, i: set(index[(c[0]-1, c[1], c[2])] for c in bricks[i] if index.get((c[0]-1, c[1], c[2])) not in {None, i})
def fall(bricks):
    index = {c: i for i, b in enumerate(bricks) for c in b}
    moved, ids = True, set()
    while moved:
        moved = False
        for i in range(len(bricks)):
            while all(c[0]>1 for c in bricks[i]) and len(supports(bricks, index, i)) == 0:
                for c in bricks[i]:
                    index.pop(c)
                bricks[i] = {(c[0]-1, c[1], c[2]) for c in bricks[i]}
                for c in bricks[i]:
                    index[c] = i
                moved = True
                ids.add(i)
    return len(ids)
fall(init)
print(sum(fall(init[:i]+init[i+1:]) for i in range(len(init))))