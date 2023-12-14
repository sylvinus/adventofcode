def tilt_row(row):
    while ".O" in row:
        row = row.replace(".O", "O.")
    return row
def tilt_w(rows):
    return tuple(map(tilt_row, rows))
def flip(rows):
    return tuple("".join(x) for x in zip(*rows))
def rev(rows):
    return tuple("".join(reversed(col)) for col in rows)
def tilt_n(rows):
    return flip(tilt_w(flip(rows)))
def tilt_e(rows):
    return rev(tilt_w(rev(rows)))
def tilt_s(rows):
    return flip(rev(tilt_w(rev(flip(rows)))))
def cycle(rows):
    return tilt_e(tilt_s(tilt_w(tilt_n(rows))))

rows = tuple(open("input.txt").read().split())

seen, period = {}, None
for n in range(1000000000):
    rows = cycle(rows)
    if rows in seen:
        period = n - seen.get(rows)
        break
    seen[rows] = n

for _ in range((1000000000-n-1)%period):
    rows = cycle(rows)

print(sum(sum((len(col)-i)*int(col[i]=="O") for i in range(len(col))) for col in flip(rows)))