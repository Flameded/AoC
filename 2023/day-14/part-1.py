with open("input.txt", "r") as f:
    inp = f.readlines()

grid = [list(l.strip("\n")) for l in inp]
h, w = len(grid), len(grid[0])

for r in range(0, h, 1):
    for c in range(0, w, 1):
        if grid[r][c] != "O":
            continue

        i = r
        while i != 0:
            adj = grid[i-1][c]
            if adj == ".":
                grid[i][c] = "."
                grid[i-1][c] = "O"
            else:
                break

            i -= 1

t = sum(["".join(row).count("O") * r for r, row in enumerate(grid[::-1], 1)])
print(t)
