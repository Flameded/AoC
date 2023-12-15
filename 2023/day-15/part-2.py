from collections import defaultdict

with open("input.txt", "r") as f:
    inp = f.read().split(",")


def HASH(s):
    t = 0
    for ch in s:
         t += ord(ch)
         t *= 17
         t = t % 256
    return t


boxes = defaultdict(list)
focal_lengths = {}
for x in inp:
    if "=" in x:
        label, val = x.split("=")
        val = int(val)
        box_idx = HASH(label)

        if label not in boxes[box_idx]:
            boxes[box_idx].append(label)

        focal_lengths[(label, box_idx)] = val
    else:
        label = x[:-1]
        box_idx = HASH(label)

        if label in boxes[box_idx]:
            boxes[box_idx].remove(label)

t = 0
for box_idx, box in boxes.items():
    t += sum((box_idx + 1) * i * focal_lengths[(label, box_idx)] for i, label in enumerate(box, 1))

print(t)
