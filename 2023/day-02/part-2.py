with open("input.txt", "r") as f:
    inp = f.readlines()

inp = [l.split(":")[1].split(";") for l in inp]

t = 0
for game in inp:
    max_red = 0
    max_green = 0
    max_blue = 0

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

        max_red = max(max_red, red)
        max_blue = max(max_blue, blue)
        max_green = max(max_green, green)

    t += max_red * max_blue * max_green

print(f"Part 2: {t}")
