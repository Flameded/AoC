with open("input.txt", "r") as f:
    inp = [l.strip() for l in f.readlines()]

r = [1]
[r.extend([r[-1], r[-1] + int(cmd.split()[1])]) if cmd != "noop" else r.append(r[-1]) for cmd in inp]
crt = ["#" if v - 1 <= pos % 40 <= v + 1 else " " for pos, v in enumerate(r)]

print(sum((cycle + 1) * val for cycle, val in enumerate(r) if cycle % 40 == 19))
[print("".join(crt[40*(i-1):40*i - 1])) for i in range(1, 7)]
