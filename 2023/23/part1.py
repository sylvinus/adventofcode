grid = open("input.txt").read().splitlines()
start, end = (1, 0), (len(grid[0])-2, len(grid)-1)
slopes = {">": (1, 0), "<": (-1, 0), "^": (0, -1), "v": (0, 1)}
addv = lambda a, b: (a[0]+b[0], a[1]+b[1])
opens = [(start, 0, {start})]
maxpath = 0
while len(opens):
    pos, cost, path = opens.pop()
    nexts = {None}
    while len(nexts) >= 1:
        if pos == end:
            if cost > maxpath:
                maxpath = cost
            break
        tile = grid[pos[1]][pos[0]]
        nexts = {addv(pos, d) for d in ([slopes[tile]] if tile in slopes else slopes.values())}
        nexts = [p for p in nexts if p not in path and grid[p[1]][p[0]] != "#"]
        if len(nexts) > 0:
            cost += 1
            for p in nexts[1:]:
                opens.append((p, cost, path.union({p})))
            pos = nexts[0]
            path.add(pos)
print(maxpath)