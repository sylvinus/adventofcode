def n(w):
    for i in range(len(w)):
        if w[i] in {105,108,111}:
            w[i+1:]=[122]*(len(w)-i-1)
    w[-1]+=1
    for i, c in enumerate(reversed(w)):
        if c<123: break
        w[-i-1]=97
        w[-i-2]+=1
    p={i for i in range(len(w)-1) if w[i]==w[i+1]}
    return len(p) and max(p)-min(p)>1 and any(w[i]==w[i+1]-1==w[i+2]-2 for i in range(len(w)-2))
w = list(map(ord,open("input.txt").read()))
while not n(w): pass
print("".join(map(chr,w)))