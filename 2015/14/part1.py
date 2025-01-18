print(max(
    s*d*int(2503/(d+p))+s*min(d,2503%(d+p))
    for s,d,p in [[int(l[z]) for z in (3,6,13)] for l in map(str.split,open("input.txt"))]
))