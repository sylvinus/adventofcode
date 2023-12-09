seqs = [[[int(x) for x in line.strip().split()]] for line in open("input.txt").readlines()]
for seq in seqs:
    while any(d!=0 for d in seq[-1]):
        seq.append([seq[-1][i+1] - seq[-1][i] for i in range(len(seq[-1]) - 1)])
print(sum(sum(s[0]*((-1)**i) for i, s in enumerate(seq)) for seq in seqs))