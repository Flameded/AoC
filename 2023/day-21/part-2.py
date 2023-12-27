with open("input.txt", "r") as f:
    inp = f.readlines()

grid = [list(l.strip()) for l in inp]
size = len(grid)

start = (size // 2, size // 2)
grid[start[0]][start[1]] = "."

curr = {start}
seen = [set(), set()]
totals = [1]
for i in range(65 + 131 * 2):

    curr = {(nr, nc) for r, c in list(curr) for nr, nc in [(r-1, c), (r, c+1), (r+1, c), (r, c-1)]
            if grid[nr % size][nc % size] == "." and (nr, nc) not in seen[i % 2]}

    seen[i % 2] |= curr
    totals.append(len(seen[i % 2]))

x0, x1, x2 = [totals[65 + 131*i] for i in range(3)]
diff_2nd = (x2 - x1) - (x1 - x0)
nth_term = lambda n: x0 + n*(n+1)//2 * diff_2nd

print(nth_term(26501365 // 131))
