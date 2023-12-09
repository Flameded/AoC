with open("input.txt", "r") as f:
    inp = f.readlines()

inp = [[int(x) for x in l.split()] for l in inp]

t = 0
for seq in inp:

    sequences = [seq]
    while any(seq):
        seq = [seq[i + 1] - seq[i] for i in range(len(seq) - 1)]
        sequences.append(seq)

    t += sum(s[-1] for s in sequences[:-1])

print(f"Part 1: {t}")
