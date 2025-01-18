choices = {"X": (1, "B", "A", "C"), "Y": (2, "C", "B", "A"), "Z": (3, "A", "C", "B")}
print(sum([choices[m[1]][0] + (choices[m[1]].index(m[0])-1)*3 for m in map(str.split, open("input.txt"))]))