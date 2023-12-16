with open("input.txt", "r") as f:
    inp = f.readlines()

grid = [list(l.strip("\n")) for l in inp]
h = len(grid)
w = len(grid[0])

start = (0, -1)
direction = (0, 1)
s = [(start, direction)]
seen = set()

while s:
    (r, c), (dr, dc) = s.pop()

    if ((r, c), (dr, dc)) in seen:
        continue
    seen.add(((r, c), (dr, dc)))

    adj = r + dr, c + dc
    if not (0 <= adj[0] < h and 0 <= adj[1] < w):
        continue

    adj_item = grid[adj[0]][adj[1]]

    if adj_item == "." or adj_item == "-" and dc or adj_item == "|" and dr:
        s.append((adj, (dr, dc)))
    elif adj_item == "-":
        s.append((adj, (0, -1)))
        s.append((adj, (0, 1)))
    elif adj_item == "|":
        s.append((adj, (-1, 0)))
        s.append((adj, (1, 0)))
    elif adj_item == "/":
        s.append((adj, (-dc, -dr)))
    elif adj_item == "\\":
        s.append((adj, (dc, dr)))

print(len(set([coord for coord, _ in list(seen)])) - 1)
