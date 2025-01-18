import re
print(sum(bool(re.search(r"(\S).\1", s))*bool(re.search(r"(\S\S).*\1", s)) for s in open("input.txt")))