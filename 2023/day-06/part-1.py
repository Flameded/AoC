with open("input.txt") as f:
    inp = f.readlines()

inp = [l.strip("\n").split(":")[1] for l in inp]

times, dists = [[int(x) for x in l.split()] for l in inp]

x = 1
for time, dist in zip(times, dists):
    total = 0
    for t in range(time):
        s = (time-t)*t
        total += s > dist

    x *= total

print(x)
