vertices = [[0, 0]]
for _, _, color in map(str.split, open("input.txt")):
    n = int(color[2:7], 16)
    v = ((1, 0), (0, 1), (-1, 0), (0, -1))[int(color[7])]
    vertices.append([vertices[-1][0]+v[0]*n, vertices[-1][1]+v[1]*n])
blocks = [ # Build a grid of macro blocks and do the same as part1
    list(sorted(list(set(sum([[v[0], v[0]+1] for v in vertices], []))))),
    list(sorted(list(set(sum([[v[1], v[1]+1] for v in vertices], [])))))
]
grid = [[False for _ in range(len(blocks[0])-1)] for _ in range(len(blocks[1])-1)]
for i, v in enumerate(vertices):
    v2 = vertices[(i+1)%len(vertices)]
    d = int(v[0]==v2[0])
    idxs = [max([ib for ib, b in enumerate(blocks[0]) if b<=min(v[0], v2[0])]), max([ib for ib, b in enumerate(blocks[1]) if b<=min(v[1], v2[1])])]
    for idx in range(idxs[d], len(blocks[d])):
        idxs[d] = idx
        if blocks[d][idx] <= max(v[d], v2[d]):
            grid[idxs[1]][idxs[0]] = True
edge = [(x, y) for y in range(len(grid)) for x in range(len(grid[0])) if x*y==0 or x==len(grid[0])-1 or y==len(grid)-1]
while len(edge):
    x, y = edge.pop()
    if 0 <= x < len(grid[0]) and 0 <= y < len(grid) and grid[y][x] is False:
        grid[y][x] = None
        for v in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            edge.append((x+v[0], y+v[1]))
print(sum(sum(int(type(cell) is bool)*(blocks[0][x+1]-blocks[0][x])*(blocks[1][y+1]-blocks[1][y]) for x, cell in enumerate(line)) for y, line in enumerate(grid)))