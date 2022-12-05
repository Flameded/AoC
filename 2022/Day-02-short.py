with open("input.txt", "r") as f:  # p = player, q = qomputer
    inp = [[ord(q), ord(p)] for (q, p) in [line.split() for line in f.readlines()]]

print(sum([p - 81 - 3 * (((2 - p) % 5 + q - 2) % 3) for (q, p) in inp]))
print(sum([p * 3 + (p + q - 1) % 3 - 263 for (q, p) in inp]))
