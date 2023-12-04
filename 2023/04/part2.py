import re, math, collections
counts = collections.defaultdict(int)
for i, card in enumerate(re.finditer("Card\s+(\d+):\s+(.+?)\s*\|\s*(.+?)\s*$", open("input.txt", "r").read(), flags=re.MULTILINE)):
    counts[i] += 1
    wins = {int(x) for x in card.group(2).split()}
    haves = {int(x) for x in card.group(3).split()}
    for y in range(len(wins.intersection(haves))):
        counts[i+y+1] += counts[i]
print(sum(counts.values()))