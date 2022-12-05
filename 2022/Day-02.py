with open("input.txt", "r") as f:
    inp = [line.split() for line in f.readlines()]

p1 = 0
for line in inp:
    their_shape = line[0]
    my_shape = line[1]

    p1 += ["X", "Y", "Z"].index(my_shape) + 1

    if my_shape == "X":
        if their_shape == "A":
            p1 += 3
        elif their_shape == "B":
            p1 += 0
        elif their_shape == "C":
            p1 += 6

    elif my_shape == "Y":
        if their_shape == "A":
            p1 += 6
        elif their_shape == "B":
            p1 += 3
        elif their_shape == "C":
            p1 += 0

    elif my_shape == "Z":
        if their_shape == "A":
            p1 += 0
        elif their_shape == "B":
            p1 += 6
        elif their_shape == "C":
            p1 += 3

p2 = 0
for line in inp:
    their_shape = line[0]
    my_shape = line[1]

    p2 += ["X", "Y", "Z"].index(my_shape) * 3

    if my_shape == "X":
        if their_shape == "A":
            p2 += 3
        elif their_shape == "B":
            p2 += 1
        elif their_shape == "C":
            p2 += 2

    elif my_shape == "Y":
        if their_shape == "A":
            p2 += 1
        elif their_shape == "B":
            p2 += 2
        elif their_shape == "C":
            p2 += 3

    elif my_shape == "Z":
        if their_shape == "A":
            p2 += 2
        elif their_shape == "B":
            p2 += 3
        elif their_shape == "C":
            p2 += 1

print(p1)
print(p2)
