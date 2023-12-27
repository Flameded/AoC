from collections import defaultdict

with open("input.txt", "r") as f:
    inp = f.readlines()

grid = [list(l.strip()) for l in inp]
h, w = len(grid), len(grid[0])

grid[0][1] = "#"
grid[h-1][w-2] = "#"
start = (1, 1)
end = (h-2, w-2)

adj_list = defaultdict(list)
seen_tiles = set()
q = [(start, 0, start)]
while q:
    curr, dist, parent = q.pop()
    r, c = curr
    adj_coords = [(nr, nc) for nr, nc in [(r-1, c), (r, c+1), (r+1, c), (r, c-1)] if grid[nr][nc] != "#"]

    if len(adj_coords) >= 3 or curr == end:
        if (curr, dist) in adj_list[parent]:
            continue

        adj_list[parent].append((curr, dist))
        adj_list[curr].append((parent, dist))

        q += [(adj, 1, curr) for adj in adj_coords]

    elif curr not in seen_tiles:
        seen_tiles.add(curr)
        q += [(adj, dist+1, parent) for adj in adj_coords]


longest = defaultdict(int)
q = [(start, set(), 0)]
while q:
    curr, path, dist = q.pop()
    longest[curr] = max(longest[curr], dist)

    adj_coords = [(adj, cost) for adj, cost in adj_list[curr]
                  if adj != curr and adj not in path]

    for adj, cost in adj_coords:
        new_path = set(path) | {adj}
        q.append((adj, new_path, dist + cost))

print(longest[end] + 2)
