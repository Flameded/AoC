from collections import defaultdict

with open("input.txt", "r") as f:
    inp = f.readlines()

blocks = [tuple(eval(l.strip("\n").replace("~", ","))) for l in inp]
blocks.sort(key=lambda coords: coords[2])

coord_to_block = {}
z_values = defaultdict(list)

fallen_blocks = []
for block in blocks:
    x1, y1, z1, x2, y2, z2 = block
    block_height = z2 - z1 + 1

    h = z1
    while h > 1 and not any(x1 <= x <= x2 and y1 <= y <= y2 for x, y in z_values[h - 1]):
        h -= 1

    new_block = x1, y1, h, x2, y2, h + block_height - 1
    fallen_blocks.append(new_block)

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            for z in range(h, h + block_height):
                z_values[z].append((x, y))
                coord_to_block[(x, y, z)] = new_block


below_blocks = defaultdict(set)
above_blocks = defaultdict(set)
for block in fallen_blocks:
    x1, y1, z1, x2, y2, z2 = block

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):

            below_coord = (x, y, z1 - 1)
            if below_coord in coord_to_block:
                below_blocks[block].add(coord_to_block[below_coord])

            above_coord = (x, y, z2 + 1)
            if above_coord in coord_to_block:
                above_blocks[block].add(coord_to_block[above_coord])

valid = [block for block in fallen_blocks if
         all(len(below_blocks[above]) > 1 for above in list(above_blocks[block]))]

print(len(valid))
