with open("input.txt") as f:
    inp = f.readlines()

inp = [l.strip("\n").split(":")[1] for l in inp]

time, dist = [int("".join([c for c in l if c.isdigit()])) for l in inp]

total = 0
for t in range(time):
    s = (time-t)*t
    total += s > dist

print(total)
