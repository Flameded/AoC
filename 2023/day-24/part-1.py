
with open("input.txt", "r") as f:
    inp = f.readlines()

stones = [eval(l.strip("\n").replace(" @", ",")) for l in inp]


def solve_simultaneous_equation_2d(a1, b1, c1, a2, b2, c2):
    # In the form ax + by = c
    # ( a1 b1 )( x ) = c1
    # ( a2 b2 )( y ) = c2
    # det = a1*b2 - a2*b1
    # Inverse:  1/det * (  b2 -b1 )
    #                   ( -a2  a1 )
    # ( x ) =  1/det * (  b2 -b1 ) ( c1 )
    # ( y ) =          ( -a2  a1 ) ( c2 )

    det = a1*b2 - a2*b1

    if det == 0:
        return None, None

    x = (b2 * c1 - b1 * c2) / det
    y = (a1 * c2 - a2 * c1) / det

    return x, y


t = 0
LO, HI = 200000000000000, 400000000000000
for i, (x1, y1, z1, dx1, dy1, dz1) in enumerate(stones):
    for (x2, y2, z2, dx2, dy2, dz2) in stones[i + 1:]:

        # (1) x1 + Adx1 = x2 + Bdx2  =>  A(dx1) + B(-dx2) = x2 - x1
        # (2) y1 + Ady1 = y2 + Bdy2  =>  A(dy1) + B(-dy2) = y2 - y1

        A, B = solve_simultaneous_equation_2d(dx1, -dx2, x2 - x1, dy1, -dy2, y2 - y1)
        t += A is not None and A > 0 and B > 0 and LO <= x1 + A*dx1 <= HI and LO <= y1 + A*dy1 <= HI

print(t)
