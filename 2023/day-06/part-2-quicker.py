with open("input.txt") as f:
    inp = f.readlines()

inp = [l.strip("\n").split(":")[1] for l in inp]

time, dist = [int("".join([c for c in l if c.isdigit()])) for l in inp]

first = -1
lo = 0
hi = time // 2
while lo <= hi:
    t = (lo + hi) // 2
    s = (time-t) * t
    s_prev = (time-t-1) * (t-1)

    if s_prev <= dist < s:
        first = t
    if s_prev < dist:
        lo = t + 1
    elif s_prev > dist:
        hi = t - 1

# We can do this due to the symmetry of the quadratic (time - t) * t   (about x = time/2)
print(time - first * 2 + 1)
