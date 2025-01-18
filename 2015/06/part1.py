import re
G=[0]*1000000
for l in open("input.txt"):
    f,a,b,c,d=re.search(r"(.) (\d+).(\d+).+?(\d+).(\d+)", l).groups()
    for x in range(int(a),int(c)+1):
        for y in range(int(b),int(d)+1):
            G[x*1000+y]=1 if f=="n" else 0 if f=="f" else 1-G[x*1000+y]
print(sum(G))