grid = [line.strip() for line in open("input.txt")]
N, S, E, W = ((0, -1), (0, 1), (1, 0), (-1, 0))
invs = {N: S, S: N, E: W, W: E}
connects = {"|": (N, S), "-": (E, W), "L": (N, E), "J": (N, W), "7": (S, W), "F": (S, E), ".": tuple()}
connects_inv = {v: k for k, v in connects.items()}
for y, row in enumerate(grid):
    for x, char in enumerate(row):
        if char == "S":
            start_pos = (x, y)
            assert x+y > 0
            incoming_connections = tuple(d for d in (N, S, E, W) if d in [invs[c] for c in connects[grid[y+d[1]][x+d[0]]]])
            grid[y] = grid[y].replace("S", connects_inv[incoming_connections])
            break
pos, i = start_pos, 0
nextdir = connects[grid[pos[1]][pos[0]]][0]
while i == 0 or pos != start_pos:
    i += 1
    pos = (pos[0]+nextdir[0], pos[1]+nextdir[1])
    cons = connects[grid[pos[1]][pos[0]]]
    nextdir = cons[(cons.index(invs[nextdir])+1)%2]
print(i//2)