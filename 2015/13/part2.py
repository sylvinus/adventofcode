import itertools
M={(x[0],x[-1][:-1]):int(x[3] if x[2]=="gain" else "-"+x[3]) for x in map(str.split,open("input.txt").readlines())}
G=set(k[0] for k in M).union({0})
print(max(
    sum(M.get(x,0) for x in set(sum([[x,x[::-1]] for x in itertools.pairwise(o+(o[0],))], [])))
    for o in itertools.permutations(G,len(G))
))