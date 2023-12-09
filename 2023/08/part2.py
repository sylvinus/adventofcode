import math
instructions, graph = open("input.txt").read().split('\n\n')
mapping = {line[0:3]: (line[7:10], line[12:15]) for line in graph.strip().split("\n")}
positions = [k for k in mapping.keys() if k.endswith("A")]
steps = [0] * len(positions)
for i, pos in enumerate(positions):
    while not pos.endswith("Z"):
        pos = mapping[pos][0 if instructions[steps[i]%len(instructions)]=="L" else 1]
        steps[i] += 1
print(math.lcm(*steps))