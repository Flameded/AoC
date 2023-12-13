with open("input.txt", "r") as f:
    inp = f.read()

inp = [chunk.split("\n") for chunk in inp.split("\n\n")]

t = 0
for grid in inp:

    c = 0
    for i in range(1, len(grid[0])):
        not_valid = sum(sum(c1 != c2 for c1, c2 in zip(row[:i][::-1], row[i:])) for row in grid)
        if not_valid == 1:
            c = i
            break

    r = 0
    for i in range(1, len(grid)):
        not_valid = sum([sum(c1 != c2 for c1, c2 in zip(r1, r2)) for r1, r2 in zip(grid[:i][::-1], grid[i:])])
        if not_valid == 1:
            r = i
            break

    t += 100*r + c

print(t)
