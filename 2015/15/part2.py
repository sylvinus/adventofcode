import math
D=[[int(x[i].strip(",")) for i in (2,4,6,8,10)] for x in map(str.split,open("input.txt"))]
G=lambda n,l:[[i]+s for i in range(n+1) for s in G(n-i,l-1)] if l>1 else [[n]]
print(max(
    math.prod(max(0,sum(r)) for r in zip(*[[n*a for a in D[i]][:-1] for i, n in enumerate(q)]))
    for q in G(100,len(D))
    if sum(D[i][-1]*n for i,n in enumerate(q))==500
))