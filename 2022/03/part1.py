import string
ords = string.ascii_lowercase + string.ascii_uppercase
print(sum(ords.index(list(set(l[:len(l)//2]).intersection(set(l[len(l)//2:])))[0])+1 for l in open("input.txt")))