print(max(map(sum,zip(*[
    [int(max(x)==y) for y in x] for x in [[
        s*d*int(n/(d+p))+s*min(d,n%(d+p))
        for s,d,p in [[int(l[z]) for z in (3,6,13)] for l in map(str.split,open("input.txt"))]
    ] for n in range(1,2504)]
]))))