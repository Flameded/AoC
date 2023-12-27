from collections import defaultdict

with open("input.txt", "r") as f:
    inp = f.readlines()

grid = [list(l.strip()) for l in inp]
h, w = len(grid), len(grid[0])

dirs = {
    "^": [(-1, 0)],
    ">": [(0, 1)],
    "v": [(1, 0)],
    "<": [(0, -1)],
    ".": [(-1, 0), (0, 1), (1, 0), (0, -1)]
}

grid[0][1] = "#"
grid[h-1][w-2] = "#"
start = (1, 1)
end = (h-2, w-2)

q = [(start, set())]
longest = defaultdict(int)

while q:
    curr, path = q.pop()
    r, c = curr
    longest[curr] = max(longest[curr], len(path))

    adj_coords = [(nr, nc) for nr, nc in [(r+dr, c+dc) for dr, dc in dirs[grid[r][c]]]
                  if grid[nr][nc] != "#" and (nr, nc) not in path]

    for adj in adj_coords:
        new_path = set(path) | {adj}
        q.append((adj, new_path))

print(longest[end] + 2)
