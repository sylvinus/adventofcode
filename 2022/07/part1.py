dirs, mode, cwd = {("/",): {}}, "", []
for line in map(str.strip, open("input.txt")):
    if mode == "ls":
        if line[0] == "$":
            mode = ""
        else:
            size, name = line.split()
            if size == "dir":
                dirs[tuple(cwd)+(name, )] = {}
            else:
                dirs[tuple(cwd)][name] = int(size)
            continue
    if line == "$ ls":
        mode = "ls"
    elif line.startswith("$ cd .."):
        cwd.pop()
    elif line.startswith("$ cd "):
        cwd.append(line[5:])
def totalsize(d):
    return sum([sum(f.values()) for n, f in dirs.items() if n[:len(d)] == d])
print(sum(s for n in dirs.keys() if (s := totalsize(n)) <= 100000))