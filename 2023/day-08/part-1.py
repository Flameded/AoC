with open("input.txt", "r") as f:
    inp = f.readlines()

inp = [l.strip("\n") for l in inp]
instructions = inp[0]

adj_list = {}
for l in inp[2:]:
    a, b = l.split(" = ")
    b = b.replace("(", "('").replace(")", "')").replace(", ", "', '")
    adj_list[a] = eval(b)

node = "AAA"

t = 0
while True:
    if instructions[t % len(instructions)] == "R":
        node = adj_list[node][1]
    else:
        node = adj_list[node][0]

    t += 1
    if node[-1] == "Z":
        break

print(f"Part 1: {t}")
