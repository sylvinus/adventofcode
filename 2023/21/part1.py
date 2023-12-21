grid = open("input.txt").read().splitlines()
plots = {(x, y) for y, line in enumerate(grid) for x, cell in enumerate(line) if cell == "S"}
for _ in range(64):
    plots = {(plot[0]+v[0], plot[1]+v[1]) for v in {(1,0),(-1,0),(0,1),(0,-1)} for plot in plots if grid[plot[1]+v[1]][plot[0]+v[0]] in ".S"}
print(len(plots))