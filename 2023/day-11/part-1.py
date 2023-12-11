with open("input.txt", "r") as f:
    inp = f.readlines()

grid = [list(l.strip("\n")) for l in inp]

# Duplicate empty rows
w = len(grid[0])
new_grid = []

for r in range(w):
    if grid[r].count("#") == 0:
        new_grid.append(grid[r])
    new_grid.append(grid[r])
grid = new_grid

# Duplicate empty columns
h, w = len(grid), len(grid[0])
new_grid = [[] for _ in range(h)]

for c in range(w):
    if [grid[r][c] for r in range(h)].count("#") == 0:
        for r in range(h):
            new_grid[r].append(grid[r][c])
    for r in range(h):
        new_grid[r].append(grid[r][c])
grid = new_grid

# Distance calculation
h, w = len(grid), len(grid[0])
vertices = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == "#"]

t = 0
for i, (r1, c1) in enumerate(vertices[:-1]):
    for r2, c2 in vertices[i+1:]:
        t += abs(r1 - r2) + abs(c1 - c2)

print(t)
