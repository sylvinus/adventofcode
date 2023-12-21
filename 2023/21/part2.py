grid = open("input.txt").read().splitlines()
W, STEPS, SIDES = len(grid), 26501365, {(1,0),(-1,0),(0,1),(0,-1)}
plots = {(x, y) for y, line in enumerate(grid) for x, cell in enumerate(line) if cell == "S"}
for _ in range(STEPS%W+W*2):
    plots = {(plot[0]+v[0], plot[1]+v[1]) for v in SIDES for plot in plots if grid[(plot[1]+v[1])%W][(plot[0]+v[0])%W] in ".S"}
block = lambda x, y: len({p for p in plots if x*W <= p[0] < (x+1)*W and y*W <= p[1] < (y+1)*W})
total = lambda n:(
    n**2*block(0, 1) + (n-1)**2*block(0, 0) +  # even & odd center blocks
    block(-2, 0) + block(2, 0) + block(0, -2) + block(0, 2) +  # angle blocks
    n*(block(-2, 1) + block(-2, -1) + block(2, 1) + block(2, -1)) +  # small edges
    (n-1)*(block(-1, -1) + block(-1, 1) + block(1, 1) + block(1, -1))  # big edges
)
print(total(STEPS//W))