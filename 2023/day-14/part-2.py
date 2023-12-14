with open("input.txt", "r") as f:
    inp = f.readlines()

grid = [list(l.strip("\n")) for l in inp]
h, w = len(grid), len(grid[0])


def tilt(direction):
    dr, dc = direction

    row_range = (h - 1, -1, -1) if dr == 1 else (0, h, 1)
    col_range = (w - 1, -1, -1) if dc == 1 else (0, w, 1)

    for r in range(*row_range):
        for c in range(*col_range):
            if grid[r][c] != "O":
                continue

            i = r if dr else c
            while (dr == -1 and i > 0) or (dc == -1 and i > 0) or (dr == 1 and i < h-1) or (dc == 1 and i < w-1):

                cr, cc = i if dr else r, i if dc else c
                adj = grid[cr+dr][cc+dc]
                if adj == ".":
                    grid[cr][cc] = "."
                    grid[cr+dr][cc+dc] = "O"
                else:
                    break

                i += dr if dr else dc


def spin_cycle():
    tilt((-1, 0))
    tilt((0, -1))
    tilt((1, 0))
    tilt((0, 1))


seen_grids = {}
cycle = 0
while True:
    spin_cycle()

    t = sum(["".join(row).count("O") * r for r, row in enumerate(grid[::-1], 1)])
    grid_tuple = tuple(tuple(row) for row in grid)

    if grid_tuple in seen_grids:
        i1, i2 = seen_grids[grid_tuple], cycle

        seq_len = i2 - i1
        left = (1_000_000_000 - i1 - 1) % seq_len

        for _ in range(left):
            spin_cycle()

        t = sum(["".join(row).count("O") * r for r, row in enumerate(grid[::-1], 1)])
        break

    seen_grids[grid_tuple] = cycle
    cycle += 1

print(t)
