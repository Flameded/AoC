from heapq import heappop, heappush

with open("input.txt", "r") as f:
    inp = f.readlines()

grid = [[int(ch) for ch in l.strip()] for l in inp]

# up, right, down, left
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# distance, row, column, amount travelled in that direction, direction index
q = []
heappush(q, (0, 0, 0, 0, 1))
heappush(q, (0, 0, 0, 0, 2))

shortest = {}
h = len(grid)
w = len(grid[0])
end = (h - 1, w - 1)

while q:
    dist, r, c, in_a_row, dir_idx = heappop(q)

    if (r, c) == end and in_a_row >= 4:
        print(dist)
        break

    if ((r, c), in_a_row, dir_idx) in shortest:
        continue
    shortest[((r, c), in_a_row, dir_idx)] = dist

    adj = [(dir_idx - 1) % 4, (dir_idx + 1) % 4] if in_a_row >= 4 else []
    if in_a_row < 10:
        adj.append(dir_idx)

    for new_dir_idx in adj:
        dr, dc = dirs[new_dir_idx]
        nr, nc = r + dr, c + dc

        if 0 <= nr < h and 0 <= nc < w:
            new_in_a_row = in_a_row + 1 if new_dir_idx == dir_idx else 1
            heappush(q, (dist + grid[nr][nc], nr, nc, new_in_a_row, new_dir_idx))
