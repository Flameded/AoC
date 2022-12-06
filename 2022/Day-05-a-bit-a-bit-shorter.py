with open("input.txt", "r") as f:
    inp = [l.strip("\n") if i < 10 else (int(l.split()[1]), int(l.split()[3]) - 1, int(l.split()[5]) - 1)
           for i, l in enumerate(f.readlines())]

stacks_p1 = [list("".join([f'{l:<35}'[4 * i + 1] for l in inp[:8][::-1]]).strip()) for i in range(9)]
stacks_p2 = __import__('copy').deepcopy(stacks_p1)
[(stacks_p1[t].extend(stacks_p1[f][-a:][::-1]), [stacks_p1[f].pop() for i in range(a)]) for a, f, t in inp[10:]]
[(stacks_p2[t].extend(stacks_p2[f][-a:]), [stacks_p2[f].pop() for i in range(a)]) for a, f, t in inp[10:]]

print("".join([stack[-1] for stack in stacks_p1]) + "\n" + "".join([stack[-1] for stack in stacks_p2]))
