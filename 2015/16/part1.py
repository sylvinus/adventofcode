for s,l in [r.split(":",1) for r in open("input.txt")]:
    if len(set(map(str.strip,l.split(","))).difference(set(map(str.strip,open("tape.txt")))))==0:
        print(s[4:])