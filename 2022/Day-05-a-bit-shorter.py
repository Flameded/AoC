with open("input.txt", "r") as f:
    inp = [l.strip("\n") if i < 10 else (int(l.split()[1]), int(l.split()[3]) - 1, int(l.split()[5]) - 1)
           for i, l in enumerate(f.readlines())]

stacks_p1 = ["".join([f'{l:<35}'[4 * i + 1] for l in inp[:8][::-1]]).strip() for i in range(9)]
stacks_p2 = list(stacks_p1)

for amount, fr, to in inp[10:]:
    stacks_p1[to] += stacks_p1[fr][-amount:][::-1]
    stacks_p1[fr] = stacks_p1[fr][:-amount]
    stacks_p2[to] += stacks_p2[fr][-amount:]
    stacks_p2[fr] = stacks_p2[fr][:-amount]

print("".join(stack[-1] for stack in stacks_p1))
print("".join(stack[-1] for stack in stacks_p2))
