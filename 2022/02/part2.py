outcomes = ("X", "Y", "Z")
choices = {"A": (1, "C", "A", "B"), "B": (2, "A", "B", "C"), "C": (3, "B", "C", "A")}
print(sum([outcomes.index(m[1])*3 + choices[choices[m[0]][outcomes.index(m[1])+1]][0] for m in map(str.split, open("input.txt"))]))