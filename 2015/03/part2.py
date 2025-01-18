M,D={(0,0)},{"v":(0,1),"^":(0,-1),">":(1,0),"<":(-1,0)}
for i in 0,1:
    P=(0,0)
    for x in open("input.txt").read()[i::2]:
        M.add(P:=tuple(map(sum,zip(D[x],P))))
print(len(M))