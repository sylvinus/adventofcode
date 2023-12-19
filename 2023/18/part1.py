grid = [[x==y==500 for x in range(1000)] for y in range(1000)]
directions = {"R": (1, 0), "L": (-1, 0), "D": (0, 1), "U": (0, -1)}
pos = (500, 500)
for d, n, _ in map(str.split, open("input.txt")):
    for _ in range(int(n)):
        pos = (pos[0]+directions[d][0], pos[1]+directions[d][1])
        grid[pos[1]][pos[0]] = True
edge = [(x, y) for y in range(len(grid)) for x in range(len(grid[0])) if x*y==0 or x==len(grid[0])-1 or y==len(grid)-1]
while len(edge):
    x, y = edge.pop()
    if 0 <= x < len(grid[0]) and 0 <= y < len(grid) and grid[y][x] is False:
        grid[y][x] = None
        for v in directions.values():
            edge.append((x+v[0], y+v[1]))
print(sum(sum(type(cell) is bool for cell in line) for line in grid))