with open("input.txt", "r") as f:
    inp = [line.strip("\n") for line in f.readlines()]

stacks = []
for i in range(9):  # once for each stack
    stacks += [""]
    for line in inp[:8][::-1]:  # going up all the stacks
        line = f'{line:<35}'  # making sure the line is 35 characters long
        crate = line[4 * i + 1]  # getting the crate from the right stack
        if crate == " ":
            break
        stacks[i] += crate

stacks_p1 = list(stacks)
stacks_p2 = list(stacks)

for line in inp[10:]:
    amount = int(line.split()[1])
    source = int(line.split()[3]) - 1
    destination = int(line.split()[5]) - 1

    # Part 1
    stacks_p1[destination] += stacks_p1[source][-amount:][::-1]
    stacks_p1[source] = stacks_p1[source][:-amount]

    # Part 2
    stacks_p2[destination] += stacks_p2[source][-amount:]
    stacks_p2[source] = stacks_p2[source][:-amount]

print("".join(stack[-1] for stack in stacks_p1))
print("".join(stack[-1] for stack in stacks_p2))
