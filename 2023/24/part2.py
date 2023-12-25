from decimal import Decimal as D
hails = [(tuple(tuple(D(c) for c in p.split(",")) for p in x)) for x in (line.split("@") for line in open("input.txt"))]
def inter(a, b, adjvx, adjvy, full=False):
    ((ax, ay, az), (avx, avy, avz)), ((bx, by, bz), (bvx, bvy, bvz)) = a, b
    avx, avy, bvx, bvy = avx-adjvx,avy-adjvy,bvx-adjvx,bvy-adjvy
    if avx*bvx == 0 or avy/avx == bvy/bvx:
        return None
    x = (ax*avy/avx-bx*bvy/bvx+by-ay)/(avy/avx - bvy/bvx)
    y = ay+avy*(x-ax)/avx
    if full:
        z = bz+bvz*(x-bx)/bvx
        at, bt = (x-ax)/avx, (x-bx)/bvx
        if round(at) != round(bt):
            return None
        return x, y, z, at
    else:
        return round(x), round(y)
def search(M):
    # The problem definition strongly implies all speeds and coordinates are integers. Brute force (vx,vy) with inside-out grid search
    for vx, vy in zip(list(range(-M, M+1))*2+[-M]*(M*2-1)+[M]*(M*2-1),[-M]*(M*2+1)+[M]*(M*2+1)+list(range(-M+1, M))*2):
        # If we adjust the frame of reference by (-vx, -vy), all hailstones should cross path in a single point
        inters = {inter(hails[0], h2, vx, vy) for h2 in hails[1:3]}.difference({None})
        if len(set(inters)) == 1:
            x, y = list(inters)[0]
            checks = [check for hail in hails if (check:=inter(((D(x), D(y), 0), (D(vx), D(vy), 0)), hail, 0, 0, full=True)) is not None]
            if len(checks) == len(hails):
                vz = (checks[1][2] - checks[0][2])/(checks[1][3]-checks[0][3])
                z = checks[0][2] - vz*checks[0][3]
                print(round(x+y+z))
                return True
i = 0
while not search(i): i+=1