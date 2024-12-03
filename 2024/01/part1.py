v=list(map(int,open("input.txt","r").read().split()))
print(sum([abs(sorted(v[::2])[i]-sorted(v[1::2])[i]) for i in range(len(v)//2)]))