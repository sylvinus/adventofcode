stacks, moves = (x.split("\n") for x in open("input.txt").read().split("\n\n"))
COLS, ROWS = (len(stacks[0])+1)//4, len(stacks)-1
crates = ["".join([stacks[r][c*4+1] for r in range(ROWS)]).strip() for c in range(COLS)]
for move in map(str.split, moves):
    cnt, f, t = int(move[1]), int(move[3])-1, int(move[5])-1
    crates[t] = crates[f][:cnt] + crates[t]
    crates[f] = crates[f][cnt:]
print("".join(c[0] for c in crates))