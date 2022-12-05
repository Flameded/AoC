with open("input.txt", "r") as f:
    inp = [line.strip() for line in f.readlines()]

calories_sums = [0]
for line in inp:
    if line == "":
        calories_sums += [0]
    else:
        calories_sums[-1] += int(line)

calories_sums.sort()

print(calories_sums[-1])
print(calories_sums[-1] + calories_sums[-2] + calories_sums[-3])
