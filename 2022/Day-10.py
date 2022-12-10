with open("input.txt", "r") as f:
    inp = [l.strip() for l in f.readlines()]

r = [1]
for cmd in inp:
    r.append(r[-1])
    if cmd != "noop":
        r.append(r[-1] + int(cmd.split()[1]))

crt = ["" for _ in range(7)]
for pos, v in enumerate(r):
    if v - 1 <= pos % 40 <= v + 1:
        crt[pos // 40] += "#"
    else:
        crt[pos // 40] += " "

print(sum((cycle + 1) * val for cycle, val in enumerate(r) if cycle % 40 == 19))
[print(row) for row in crt[:-1]]
