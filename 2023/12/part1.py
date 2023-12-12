import itertools, re
s = 0
for data, counts in map(str.split, open("input.txt")):
    counts = [int(x) for x in counts.split(",")]
    unknowns = [i for i in range(len(data)) if data[i] == "?"]
    for test in itertools.product((True, False), repeat=len(unknowns)):
        newsprings = [unknowns[i] for i in range(len(unknowns)) if test[i]]
        newdata = "".join(["#" if (i in newsprings) else data[i] for i in range(len(data))])
        if [len(m) for m in re.findall(r"(#+)", newdata.replace("?", "."))] == counts:
            s += 1
print(s)