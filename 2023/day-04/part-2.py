with open("input.txt", "r") as f:
    inp = f.readlines()

inp = [l.strip("\n").split(":")[1] for l in inp]

copies = {i: 1 for i, _ in enumerate(inp, 1)}

for idx, card in enumerate(inp, 1):
    winning = card.split("|")[0].split()
    have = card.split("|")[1].split()

    x = len(set(have) & set(winning))

    for i in range(x):
        copies[idx + i + 1] += copies[idx]

print(f"Part 2: {sum(copies.values())}")
