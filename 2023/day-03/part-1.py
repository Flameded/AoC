with open("input.txt", "r") as f:
    inp = f.readlines()

grid = [l.strip("\n") for l in inp]

height = len(grid)
width = len(grid[0])

valid_nums = []
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
                if item != "." and not item.isdigit():
                    is_valid = True
                    break

        # If the character is not a digit or the end of a line,
        # check if number is valid and if so add it to a valid number list
        if not ch.isdigit() or c == width - 1:
            if is_valid and len(number) > 0:
                valid_nums.append(int(number))

            number = ""
            is_valid = False

print(f"Part 1: {sum(valid_nums)}")
