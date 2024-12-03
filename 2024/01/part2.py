v=list(map(int,open("input.txt","r").read().split()))
print(sum([x*v[1::2].count(x) for x in v[::2]]))