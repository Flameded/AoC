with open("input.txt", "r") as f:
    inp = [line.strip().split(',') for line in f.readlines()]

p1, p2 = 0, 0
for id_ranges in inp:
    a, b = [int(i) for i in id_ranges[0].split('-')]  # range1 start, end
    x, y = [int(i) for i in id_ranges[1].split('-')]  # range2 start, end

    if a <= x <= y <= b or x <= a <= b <= y:
        p1 += 1
    if a <= x <= b or x <= a <= y:
        p2 += 1

print(p1)
print(p2)
