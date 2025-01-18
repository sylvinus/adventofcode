import itertools
G,N={},set()
for f,_,t,_,d in map(str.split,open("input.txt")):
    G[(f,t)]=G[(t,f)]=int(d)
    N.update({f,t})
print(min(sum(G[v] for v in itertools.pairwise(p)) for p in itertools.permutations(N, len(N))))