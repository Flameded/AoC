with open("input.txt", "r") as f:
   inp = [line.strip() for line in f.readlines()]


def calc_priority(letter):
    if letter >= "a":  # lowercase
        return ord(common_item) - 96
    else:  # uppercase
        return ord(common_item) - 38


p1 = 0
for rucksack in inp:
    compartment1 = rucksack[:len(rucksack)//2]  # first half
    compartment2 = rucksack[len(rucksack)//2:]  # second half

    common_item = list(set(compartment1) & set(compartment2))[0]
    p1 += calc_priority(common_item)

p2 = 0
for i in range(0, len(inp), 3):
    rucksack1, rucksack2, rucksack3 = inp[i], inp[i + 1], inp[i + 2]

    common_item = list(set(rucksack1) & set(rucksack2) & set(rucksack3))[0]
    p2 += calc_priority(common_item)

print(p1)
print(p2)
