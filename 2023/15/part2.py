def h(step, v=0):
    for char in step:
        v = ((v+ord(char))*17)%256
    return v
boxes = [{} for _ in range(256)]
for step in open("input.txt").read().split(","):
    label, lens = step.split("=") if "=" in step else (step[:-1], None)
    if lens is not None:
        boxes[h(label)][label] = int(lens)
    else:
        boxes[h(label)].pop(label, None)
print(sum(
    (b+1)*(i+1)*v
    for b in range(len(boxes))
    for i, v in enumerate(boxes[b].values())
))