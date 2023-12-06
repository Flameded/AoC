with open("input.txt", "r") as f:
    inp = f.readlines()

inp = [l.split(":")[1].split(";") for l in inp]

t = 0
for game_id, game in enumerate(inp, 1):
    valid = True

    for group in game:
        red = 0
        green = 0
        blue = 0

        for cube in group.split(","):
            n, colour = cube.strip().split()
            n = int(n)

            if colour == "red":
                red = n
            elif colour == "green":
                green = n
            elif colour == "blue":
                blue = n

        if red > 12 or green > 13 or blue > 14:
            valid = False

    if valid:
        t += game_id

print(f"Part 1: {t}")
