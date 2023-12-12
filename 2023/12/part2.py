import itertools, re, functools
@functools.cache
def lookup(rest, groups, current_group):
    if len(rest) == 0:
        return int(len(groups) == 0)
    elif len(groups) == 0:
        return int("#" not in rest)
    elif rest[0] == ".":
        if current_group > 0:
            if groups[0] != current_group:
                return 0
            groups = groups[1:]
        return lookup(rest[1:], groups, 0)
    elif rest[0] == "#":
        return lookup(rest[1:], groups, current_group+1)
    elif rest[0] == "?":
        return lookup("#"+rest[1:], groups, current_group) + lookup("."+rest[1:], groups, current_group)
print(sum(
    lookup("?".join([data]*5) + ".", tuple(int(x) for x in counts.split(","))*5, 0)
    for data, counts in map(str.split, open("input.txt"))
))