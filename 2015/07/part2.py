import functools
F=lambda x:x+"_()" if x.islower() else {"A":"&","O":"|","L":"<<","R":">>","N":"65535^"}.get(x[0],x)
for i in 0,1:
    for L in map(str.split,open("input.txt")):
        exec(L[-1]+"_=functools.lru_cache()(lambda:"+"".join(map(F,L[:-2]))+")")
    if i==1: b_=lambda:C
    C=a_()
print(C)