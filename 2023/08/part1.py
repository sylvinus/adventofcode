instructions, graph = open("input.txt").read().split('\n\n')
mapping = {line[0:3]: (line[7:10], line[12:15]) for line in graph.strip().split("\n")}
pos, step = "AAA", 0
while pos != "ZZZ":
    pos = mapping[pos][0 if instructions[step%len(instructions)]=="L" else 1]
    step += 1
print(step)