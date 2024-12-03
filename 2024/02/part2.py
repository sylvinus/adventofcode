tests=lambda r:[r]+[r[:i]+r[i+1:] for i in range(len(r))]
safe=lambda d:0 not in d and max(map(abs,d)) <= 3 and (all(x<=0 for x in d) or all(x>=0 for x in d))
print(sum(any(safe([int(j)-int(i) for i,j in zip(t,t[1:])]) for t in tests(r.split())) for r in open("input.txt")))