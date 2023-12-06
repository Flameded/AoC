from collections import defaultdict

with open("input.txt", "r") as f:
    inp = f.readlines()

grid = [l.strip("\n") for l in inp]

height = len(grid)
width = len(grid[0])

id_to_num = {}
asterisks = defaultdict(set)
valid_num_id = 0
is_valid = False
number = ""
for r, line in enumerate(grid):
    for c, ch in enumerate(line):

        # For every digit of a number, check the surroundings for a symbol to see if valid
        if ch.isdigit():
            number += ch
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
                nr = r + dr
                nc = c + dc
                if not (0 <= nr < height and 0 <= nc < width):
                    continue

                item = grid[nr][nc]
                if item == "*":
                    # Adding the number id to a set so each number is added exactly once
                    asterisks[(nr, nc)].add(valid_num_id)
                    is_valid = True
                    break

        # If the character is not a digit or the end of a line,
        # check if number is valid and if so, map its id to its value
        if not ch.isdigit() or c == width - 1:
            if is_valid and len(number) > 0:
                id_to_num[valid_num_id] = int(number)
                valid_num_id += 1

            number = ""
            is_valid = False


values_to_multiply = [val for val in asterisks.values() if len(val) == 2]
t = sum(id_to_num[a] * id_to_num[b] for a, b in values_to_multiply)

print(f"Part 2: {t}")
