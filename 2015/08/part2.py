print(sum(l.count('"')+l.count("\\")+2 for l in map(str.strip,open("input.txt"))))