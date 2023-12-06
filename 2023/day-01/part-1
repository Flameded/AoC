with open("input.txt", "r") as f:
    inp = f.readlines()

inp = [l.strip("\n") for l in inp]

t = 0
for l in inp:
    digits = [ch for ch in l if ch.isdigit()]
    t += int(digits[0] + digits[-1])

print(f"Part 1: {t}")
