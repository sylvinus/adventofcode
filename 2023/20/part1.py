modules = {k.strip("&%"): [k[0], {}, [d.strip() for d in v.split(", ")]] for k, v in (line.split(" -> ") for line in open("input.txt"))}
modules["rx"] = ["", {}, []]
for k, m in modules.items():
    for d in m[2]:
        modules[d][1][k] = False
count = [0, 0]
for _ in range(1000):
    q = [("broadcaster", False, "button")]
    while len(q) > 0:
        dest, val, src = q.pop(0)
        count[int(val)] += 1
        m = modules[dest]
        if m[0] == "%":
            if not val:
                m[1][None] = not m[1].get(None)
                q += [(d, m[1][None], dest) for d in m[2]]
        elif m[0] == "&":
            m[1][src] = val
            q += [(d, not all(m[1].values()), dest) for d in m[2]]
        else:
            q += [(d, val, dest) for d in m[2]]
print(count[0]*count[1])