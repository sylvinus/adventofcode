s = 0
for col in ["".join(x) for x in zip(*open("input.txt").read().split())]:
    while ".O" in col:
        col = col.replace(".O", "O.")
    s += sum((len(col)-i)*int(col[i]=="O") for i in range(len(col)))
print(s)