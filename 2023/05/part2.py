with open("input.txt", "r") as f:
    seeds = [int(x) for x in f.readline()[7:].split()]
    seedranges = list(zip(*[iter(seeds)] * 2))
    blocks = f.read().strip().split("\n\n")
    maps = [[[int(x) for x in line.split()] for line in block.split(":")[1].strip().split("\n")] for block in blocks]

locations = []
for rng in seedranges:
    i = 0
    while i < rng[1]:
        # See how much we can skip in the range before changing any mapping line
        remaining_ranges = []
        seed = rng[0] + i
        for block in maps:
            for line in block:
                found = False
                if seed >= line[1] and seed < line[1] + line[2]:
                    found = True
                    remaining_ranges.append(line[1] + line[2] - seed)
                    seed += line[0] - line[1]
                    break
            if not found:
                next_ranges = [(line[1] - seed) for line in block if (line[1] - seed > 0)]
                if len(next_ranges) > 0:
                    remaining_ranges.append(min(next_ranges))
        locations.append(seed)
        i += min(remaining_ranges)
print(min(locations))