import functools
F=lambda x:x+"_()" if x.islower() else {"A":"&","O":"|","L":"<<","R":">>","N":"65535^"}.get(x[0],x)
for L in map(str.split,open("input.txt")):
    exec(L[-1]+"_=functools.lru_cache()(lambda:"+"".join(map(F,L[:-2]))+")")
print(a_())