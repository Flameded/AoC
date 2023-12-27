with open("input.txt", "r") as f:
    inp = f.readlines()

grid = [list(l.strip()) for l in inp]
size = len(grid)

start = (size // 2, size // 2)
grid[start[0]][start[1]] = "."

curr = {start}
seen = [set(), set()]
totals = [1]
for i in range(64):

    curr = {(nr, nc) for r, c in list(curr) for nr, nc in [(r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)]
            if 0 <= nr < size and 0 <= nc < size and grid[nr][nc] == "." and (nr, nc) not in seen[i % 2]}

    seen[i % 2] |= curr
    totals.append(len(seen[i % 2]))

print(totals[64])
