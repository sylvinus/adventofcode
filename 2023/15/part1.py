def h(step, v=0):
    for char in step:
        v = ((v+ord(char))*17)%256
    return v
print(sum(h(step) for step in open("input.txt").read().split(",")))