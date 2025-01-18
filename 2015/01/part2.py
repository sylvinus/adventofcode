f = 0
for i, x in enumerate(open("input.txt").read()):
    f += 81-2*ord(x)
    if f < 0:
        print(i+1)
        break