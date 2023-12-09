with open("input.txt", "r") as f:
    inp = f.readlines()

inp = [l.strip("\n") for l in inp]
instructions = inp[0]

adj_list = {}
for l in inp[2:]:
    a, b = l.split(" = ")
    b = b.replace("(", "('").replace(")", "')").replace(", ", "', '")
    adj_list[a] = eval(b)

nodes = [node for node in adj_list.keys() if node[-1] == "A"]

steps = []
for curr in nodes:

    i = 0
    while True:
        if instructions[i % len(instructions)] == "R":
            curr = adj_list[curr][1]
        else:
            curr = adj_list[curr][0]

        i += 1
        if curr[-1] == "Z":
            steps.append(i)
            break


hcf = 1
for i in range(2, min(steps) // 2 + 1):
    if all(x % i == 0 for x in steps):
        hcf *= i
        steps = [x // i for x in steps]

t = 1
for x in steps:
    t *= x
t *= hcf

print(f"Part 2: {t}")
