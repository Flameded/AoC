with open("input.txt", "r") as f:
    inp = f.readlines()

inp = [l.strip("\n") for l in inp]

five = []
four = []
full = []
three = []
twopair = []
onepair = []
high = []
lists = [high, onepair, twopair, three, full, four, five]

for l in inp:
    hand, bid = l.split()

    idx = 0
    unique = len(set(hand))
    letter_counts = [hand.count(c) for c in set(hand)]

    if unique == 1:
        idx = 6
    if unique == 2:
        if letter_counts.count(4) == 1:
            idx = 5
        if letter_counts.count(3) == 1:
            idx = 4
    if unique == 3:
        if letter_counts.count(3) == 1:
            idx = 3
        if letter_counts.count(2) == 2:
            idx = 2
    if unique == 4:
        idx = 1
    if unique == 5:
        idx = 0

    lists[idx].append((hand, bid))


def sort_func(x):
    n = ""
    for d in x:
        n += str("23456789TJQKA".index(d)).zfill(2)

    return int(n)


total = []
for l in lists:
    total += sorted(l, key=lambda x: sort_func(x[0]))

t = sum(int(l[1]) * i for i, l in enumerate(total, 1))

print(f"Part 1: {t}")
