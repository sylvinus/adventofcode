t={k:int(v) for k, v in map(str.split,open("tape.txt"))}
c=lambda k,a,b:a<b if k[:2] in {"po","go"} else a>b if k[:3] in {"cat","tre"} else a==b
for r in map(str.split,open("input.txt")):
    d = {k:int(v.strip(":,")) for k,v in zip(r[2::2],r[3::2])}
    if all(c(k,d[k],t[k]) for k in d):
        print(r[1][:-1])