with open("input.txt", "r") as f:
    seeds = [int(x) for x in f.readline()[7:].split()]
    blocks = f.read().strip().split("\n\n")
    maps = [[[int(x) for x in line.split()] for line in block.split(":")[1].strip().split("\n")] for block in blocks]

locations = []
for seed in seeds:
    for block in maps:
        for line in block:
            if seed >= line[1] and seed < line[1] + line[2]:
                seed += line[0] - line[1]
                break
    locations.append(seed)
print(min(locations))