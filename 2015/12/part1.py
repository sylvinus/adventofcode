import re
print(sum(map(int,re.findall(r"-?\d+",open("input.txt").read()))))