with open("input.txt", "r") as f:
    inp = [[(int(x.split('-')[0]), int(x.split('-')[1])) for x in l.strip().split(',')] for l in f.readlines()]

print(len([400 for (a, b), (x, y) in inp if a <= x <= y <= b or x <= a <= b <= y]))
print(len([400 for (a, b), (x, y) in inp if a <= x <= b or x <= a <= y]))
