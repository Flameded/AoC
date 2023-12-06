with open("input.txt", "r") as f:
    inp = f.readlines()

inp = [l.strip("\n").split(":")[1] for l in inp]

t = 0
for idx, card in enumerate(inp, 1):
    winning = card.split("|")[0].split()
    have = card.split("|")[1].split()

    x = len(set(have) & set(winning))
    t += int(2**(x-1))

print(f"Part 1: {t}")
