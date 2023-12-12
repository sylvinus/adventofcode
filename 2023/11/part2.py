import itertools
grid = [line.strip() for line in open("input.txt")]
empty_rows = {y for y in range(len(grid)) if "#" not in grid[y]}
empty_cols = {x for x in range(len(grid[0])) if "#" not in {grid[y][x] for y in range(len(grid))}}
galaxies = [(
    x + (1000000-1)*len({c for c in empty_cols if c<x}), y + (1000000-1)*len({r for r in empty_rows if r<y}
)) for y in range(len(grid)) for x in range(len(grid[0])) if grid[y][x] == "#"]
pairs = tuple(itertools.combinations(galaxies, 2))
print(sum([abs(x1-x2) + abs(y1-y2) for (x1, y1), (x2, y2) in pairs]))