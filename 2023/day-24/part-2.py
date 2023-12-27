import z3

with open("input.txt", "r") as f:
    inp = f.readlines()

stones = [eval(l.strip("\n").replace(" @", ",")) for l in inp]

# 3 Hailstones required:   a1 + d1*t1,   a2 + d2*t2,   a3 + d3*t3
# Intersects with the line:  a + d  , at:  t1, t2, t3  respectively
# This leads to 3 equations, each having 3 equations (for x, y, z):
# a1 + d1*t1 = a + d*t1
# a2 + d2*t2 = a + d*t2
# a3 + d3*t3 = a + d*t3

# Had to quickly learn z3
x, y, z, dx, dy, dz = [z3.Real(var) for var in "x y z dx dy dz".split()]
t = [z3.Real(var) for var in "t1 t2 t3".split()]

solver = z3.Solver()
for i in range(3):
    xi, yi, zi, dxi, dyi, dzi = stones[i]
    solver.add(xi + dxi * t[i] == x + dx * t[i])
    solver.add(yi + dyi * t[i] == y + dy * t[i])
    solver.add(zi + dzi * t[i] == z + dz * t[i])

solver.check()
m = solver.model()
print(m.eval(m[x] + m[y] + m[z]))
