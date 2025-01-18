M,D={(P:=(0,0))},{"v":(0,1),"^":(0,-1),">":(1,0),"<":(-1,0)}
for x in open("input.txt").read():
    M.add(P:=tuple(map(sum,zip(D[x],P))))
print(len(M))