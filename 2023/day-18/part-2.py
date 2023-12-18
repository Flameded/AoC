with open("input.txt", "r") as f:
    inp = f.readlines()

inp = [l.strip("\n") for l in inp]
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

vertex_count = 0
curr = (0, 0)
vertices = [curr]
for l in inp:
    n = l.split()[-1][2:-1]
    n, d = int(n[:5], 16), int(n[-1], 16)
    dr, dc = dirs[d]

    vertex_count += n
    curr = curr[0] + dr * n, curr[1] + dc * n
    vertices.append(curr)

area = 0
for i in range(len(vertices)):
    x1, y1 = vertices[i]
    x2, y2 = vertices[(i + 1) % len(vertices)]
    area += (x1 * y2) - (y1 * x2)

area = abs(area) + vertex_count
print(area // 2 + 1)
