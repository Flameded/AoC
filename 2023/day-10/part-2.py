with open("input.txt", "r") as f:
    inp = f.readlines()

grid = [[c for c in l.strip("\n")] for l in inp]
h = len(grid)
w = len(grid[0])

start = (-1, -1)
start_type = ""
for r, l in enumerate(grid):
    for c, ch in enumerate(l):
        if ch == "S":
            start = (r, c)

            dirs = set("|-JL7F")
            if r > 0 and grid[r - 1][c] in "|7F":
                dirs &= set("|7F")
            if r < h and grid[r + 1][c] in "|LJ":
                dirs &= set("|LJ")
            if c > 0 and grid[r][c - 1] in "-LF":
                dirs &= set("-LF")
            if c < w and grid[r][c + 1] in "-J7":
                dirs &= set("-J7")

            start_type = list(dirs)[0]

grid[start[0]][start[1]] = start_type

pipe_to_dirs = {
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
    "|": [(1, 0), (-1, 0)],
    "-": [(0, 1), (0, -1)]
}

seen = set()
q = [start]

while q:
    curr = q.pop()

    if curr in seen:
        continue
    seen.add(curr)

    r, c = curr
    pipe = grid[r][c]
    for dr, dc in pipe_to_dirs[pipe]:
        adj = (r + dr, c + dc)

        if 0 <= adj[0] < h and 0 <= adj[1] < w:
            q.append(adj)


grid = [[grid[r][c] if (r, c) in seen else "." for c in range(w)] for r in range(h)]

# Check horizontals left --> right
t = 0
for r in range(h):

    valid = False
    for c in range(w):
        curr = grid[r][c]

        if curr in "|JL":
            valid = not valid

        if curr == ".":
            t += valid

print(f"Part 2: {t}")
