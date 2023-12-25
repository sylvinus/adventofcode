import itertools
hails = [(tuple(tuple(int(c) for c in p.split(",")) for p in x)) for x in (line.split("@") for line in open("input.txt"))]
count, smin, smax = 0, 200000000000000, 400000000000000
for comb in itertools.combinations(hails, 2):
    ((ax, ay, az), (avx, avy, avz)), ((bx, by, bz), (bvx, bvy, bvz)) = comb
    assert avx != 0 and bvx != 0
    if avy/avx == bvy/bvx: # parallel
        continue
    x = (ax*avy/avx-bx*bvy/bvx+by-ay)/(avy/avx - bvy/bvx)
    y = ay+avy*(x-ax)/avx
    at, bt = (x-ax)/avx, (x-bx)/bvx
    if at > 0 and bt > 0 and smin <= x <= smax and smin <= y <= smax:
        count += 1
print(count)