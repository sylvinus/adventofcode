import math
with open("input.txt", "r") as f:
    times = [int(x) for x in f.readline().split(":")[1].strip().split()]
    dists = [int(x) for x in f.readline().split(":")[1].strip().split()]

margins = []
for race in zip(times, dists):
    m = 0
    for hold in range(1, race[0]):
        dist = (race[0] - hold) * hold
        if dist > race[1]:
            m += 1
    margins.append(m)

print(math.prod(margins))