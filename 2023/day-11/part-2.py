with open("input.txt", "r") as f:
    inp = f.readlines()

grid = [list(l.strip("\n")) for l in inp]

h = len(grid)
w = len(grid[0])

for r in range(h):
    if grid[r].count("#") == 0:
        grid[r] = list("x" * w)

for c in range(w):
    if [grid[r][c] for r in range(h)].count("#") == 0:
        for r in range(h):
            grid[r][c] = "x"

vertices = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == "#"]

t = 0
for i, (r1, c1) in enumerate(vertices[:-1]):
    for r2, c2 in vertices[i+1:]:
        t += abs(r1 - r2) + abs(c1 - c2)

        for c in range(*sorted([c1, c2])):
            if grid[0][c] == "x":
                t += 999_999

        for r in range(*sorted([r1, r2])):
            if grid[r][0] == "x":
                t += 999_999

print(t)
