from collections import deque

with open("input.txt", "r") as f:
    inp = f.readlines()

inp = [l.strip("\n") for l in inp]
dirs = {"R": (0, 1), "U": (-1, 0), "L": (0, -1), "D": (1, 0)}

h, w = 1000, 1000
grid = [["." for _ in range(h)] for _ in range(w)]

curr = (500, 500)
grid[curr[0]][curr[1]] = "#"
for l in inp:
    d, n, colour = l.split()
    dr, dc = dirs[d]
    n = int(n)

    for i in range(n):
        curr = curr[0] + dr, curr[1] + dc
        grid[curr[0]][curr[1]] = "#"

seen = set()
start = (0, 0)
q = deque([start])

# Will not work if any is "#" touching or outside the edges of the grid
while q:
    r, c = q.popleft()

    if (r, c) in seen:
        continue
    seen.add((r, c))

    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:

        nr = r + dr
        nc = c + dc

        if 0 <= nr < h and 0 <= nc < w:
            adj_item = grid[nr][nc]
            if adj_item == ".":
                q.append((nr, nc))

print(h * w - len(seen))
