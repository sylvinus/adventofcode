import itertools
n=open("input.txt").read()
for _ in range(50):
    n="".join(str(len(list(g)))+k for k,g in itertools.groupby(n))
print(len(n))