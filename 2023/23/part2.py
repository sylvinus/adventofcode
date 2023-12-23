grid = open("input.txt").read().splitlines()
start, end = (1, 0), (len(grid[0])-2, len(grid)-1)
addv = lambda a, b: (a[0]+b[0], a[1]+b[1])
edges = {}
opens = [(start, start, 0, {start})]
while len(opens):
    pos, startpos, cost, path = opens.pop()
    edgecost = 0
    nexts = {None}
    while len(nexts) >= 1:
        if pos == end:
            edges[tuple(sorted((startpos, pos)))] = edgecost
            break
        tile = grid[pos[1]][pos[0]]
        nexts = {addv(pos, d) for d in ((1, 0), (-1, 0), (0, -1), (0, 1))}
        nexts = [p for p in nexts if p not in path and grid[p[1]][p[0]] != "#"]
        if len(nexts) > 0:
            cost += 1
            edgecost += 1
            if len(nexts) > 1:
                key = tuple(sorted((startpos, pos)))
                if key not in edges:
                    edges[key] = edgecost
                    for p in nexts:
                        opens.append((p, pos, cost, path.union({p})))
                break
            else:
                pos = nexts[0]
                path.add(pos)
# Runs in ~3m. There is probably a better algorithm but it's xmas time!
opens = [(0, start, set())]
maxcost = 0
while len(opens) > 0:
    cost, pos, path = opens.pop()
    if pos == end and cost > maxcost:
        maxcost = cost
    for edge, edgecost in edges.items():
        if edge[1] == pos:
            edge = (edge[1], edge[0])
        if edge[0] == pos and edge[1] not in path:
            opens.append((cost+edgecost, edge[1], path.union({edge[1]})))
print(maxcost)