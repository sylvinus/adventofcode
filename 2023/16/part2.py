grid = [line.strip() for line in open("input.txt")]
N, S, E, W = ((0, -1), (0, 1), (1, 0), (-1, 0))
maps = {
    "\\": {W: (N, ), N: (W, ), S: (E, ), E: (S, )}, 
    "/":  {W: (S, ), N: (E, ), S: (W, ), E: (N, )},
    "/":  {W: (S, ), N: (E, ), S: (W, ), E: (N, )},
    "|":  {W: (N, S), E: (N, S)},
    "-":  {S: (E, W), N: (E, W)}
}
def tiles(start):
    beams, seen = [start], {}
    while len(beams) > 0:
        pos, vect = beams.pop()
        if (pos, vect) not in seen and 0 <= pos[0] < len(grid[0]) and 0 <= pos[1] < len(grid):
            seen[(pos, vect)] = True
            tile = grid[pos[1]][pos[0]]
            for newvect in (maps.get(tile, {}).get(vect) or (vect, )):
                beams.append(((pos[0]+newvect[0], pos[1]+newvect[1]), newvect))
    return len(set(b[0] for b in seen))
print(max([tiles(b) for b in (
    [((0, y), E) for y in range(len(grid))] + 
    [((len(grid[0])-1, y), W) for y in range(len(grid))] + 
    [((x, 0), S) for x in range(len(grid[0]))] + 
    [((x, len(grid)-1), N) for x in range(len(grid[0]))]
)]))