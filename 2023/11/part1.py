import itertools
flip = lambda g: ["".join([g[y][x] for y in range(len(g))]) for x in range(len(g[0]))]
expand = lambda g: sum([[line, line] if "#" not in line else [line] for line in g], [])
grid = flip(expand(flip(expand([line.strip() for line in open("input.txt")]))))
galaxies = [(x, y) for y in range(len(grid)) for x in range(len(grid[0])) if grid[y][x] == "#"]
pairs = tuple(itertools.combinations(galaxies, 2))
print(sum([abs(x1-x2) + abs(y1-y2) for (x1, y1), (x2, y2) in pairs]))