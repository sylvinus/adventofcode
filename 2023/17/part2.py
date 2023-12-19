import heapq
grid = [line.strip() for line in open("input.txt")]
straightlen = lambda path: max([0]+[i for i in range(1, min(len(path), 10)+1) if len(set(path[-i:])) == 1])
opens = []
heapq.heappush(opens, (0, (0, 0), []))
bests = {}
while len(opens) > 0:
    cost, pos, path = heapq.heappop(opens)
    lastvects = tuple(path[-straightlen(path):])
    if pos == (len(grid[0])-1, len(grid)-1) and len(lastvects) >= 4:
        print(cost)
        break
    for v in {(0, -1), (0, 1), (1, 0), (-1, 0)}:
        if len(lastvects) > 0 and v == ((-lastvects[-1][0], -lastvects[-1][1])): # no u-turns
            continue
        if len(lastvects) == 10 and v == lastvects[-1]: # must turn after 10
            continue
        if 0 < len(lastvects) < 4 and v != lastvects[-1]: # can't turn before 4
            continue
        newpos = (pos[0]+v[0], pos[1]+v[1])
        if 0 <= newpos[0] < len(grid[0]) and 0 <= newpos[1] < len(grid):
            newcost = cost + int(grid[newpos[1]][newpos[0]])
            newpath = path+[v]
            straightvects = tuple(newpath[-straightlen(newpath):])
            best = bests.get((newpos, straightvects))
            if best is None or best > newcost:
                bests[(newpos, straightvects)] = newcost
                heapq.heappush(opens, (newcost, newpos, newpath))