from collections import deque

with open("input.txt", "r") as f:
    inp = f.readlines()

grid = [list(l.strip("\n")) for l in inp]
h = len(grid)
w = len(grid[0])


def f(start, direction):
    q = deque()
    q.append((start, direction))
    seen = set()

    while q:
        (r, c), (dr, dc) = q.popleft()

        if ((r, c), (dr, dc)) in seen:
            continue
        seen.add(((r, c), (dr, dc)))

        adj = r + dr, c + dc
        if not (0 <= adj[0] < h and 0 <= adj[1] < w):
            continue

        adj_item = grid[adj[0]][adj[1]]
        if adj_item == "." or adj_item == "-" and dc or adj_item == "|" and dr:
            q.append((adj, (dr, dc)))
        elif adj_item == "-":
            q.append((adj, (0, -1)))
            q.append((adj, (0, 1)))
        elif adj_item == "|":
            q.append((adj, (-1, 0)))
            q.append((adj, (1, 0)))
        elif adj_item == "/":
            q.append((adj, (-dc, -dr)))
        elif adj_item == "\\":
            q.append((adj, (dc, dr)))

    return len(set([coord for coord, _ in list(seen)])) - 1


m = 0
for i in range(max(h, w)):
    if i < h:
        m = max(m, f((i, -1), (0, 1)))
        m = max(m, f((i, w), (0, -1)))
    if i < w:
        m = max(m, f((-1, i), (1, 0)))
        m = max(m, f((w, i), (-1, 0)))

print(m)
