import collections
grid = open("input.txt").read().splitlines()
start, end = (1, 0), (len(grid[0])-2, len(grid)-1)
addv = lambda a, b: (a[0]+b[0], a[1]+b[1])
edges = collections.defaultdict(dict)
opens = [(start, start, 0, {start})]
while len(opens):
    pos, startpos, cost, path = opens.pop()
    edgecost = 0
    nexts = {None}
    while len(nexts) >= 1:
        if pos == end:
            edges[min(startpos, pos)][max(startpos, pos)] = edgecost
            edges[max(startpos, pos)][min(startpos, pos)] = edgecost
            break
        tile = grid[pos[1]][pos[0]]
        nexts = {addv(pos, d) for d in ((1, 0), (-1, 0), (0, -1), (0, 1))}
        nexts = [p for p in nexts if p not in path and grid[p[1]][p[0]] != "#"]
        if len(nexts) > 0:
            cost += 1
            edgecost += 1
            if len(nexts) > 1:
                if startpos not in edges[pos]:
                    edges[startpos][pos] = edgecost
                    edges[pos][startpos] = edgecost
                    for p in nexts:
                        opens.append((p, pos, cost, path.union({p})))
                break
            else:
                pos = nexts[0]
                path.add(pos)
opens = [(0, start, set())]
maxcost = 0
while len(opens) > 0:
    cost, pos, path = opens.pop()
    if pos == end and cost > maxcost:
        maxcost = cost
    for dest, edgecost in edges[pos].items():
        if dest not in path:
            opens.append((cost+edgecost, dest, path.union({dest})))
print(maxcost)