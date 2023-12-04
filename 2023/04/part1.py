import re, math
s = 0
for card in re.finditer("Card\s+(\d+):\s+(.+?)\s*\|\s*(.+?)\s*$", open("input.txt", "r").read(), flags=re.MULTILINE):
    wins = {int(x) for x in card.group(2).split()}
    haves = {int(x) for x in card.group(3).split()}
    s += math.floor(2**(len(wins.intersection(haves))-1))
print(s)