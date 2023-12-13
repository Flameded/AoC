with open("input.txt", "r") as f:
    inp = f.read()

inp = [chunk.splitlines() for chunk in inp.split("\n\n")]

t = 0
for grid in inp:

    c = 0
    for i in range(1, len(grid[0])):
        valid = all(all(c1 == c2 for c1, c2 in zip(row[:i][::-1], row[i:])) for row in grid)
        if valid:
            c = i
            break

    r = 0
    for i in range(1, len(grid)):
        valid = all([r1 == r2 for r1, r2 in zip(grid[:i][::-1], grid[i:])])
        if valid:
            r = i
            break

    t += 100*r + c

print(t)
