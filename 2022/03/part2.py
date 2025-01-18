import string
ords = string.ascii_lowercase + string.ascii_uppercase
lines = [set(l.strip()) for l in open("input.txt")]
print(sum(ords.index(list(set.intersection(*lines[i:i+3]))[0])+1 for i in range(0, len(lines), 3)))