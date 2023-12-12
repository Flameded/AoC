with open("input.txt", "r") as f:
    inp = f.readlines()

inp = [l.strip("\n") for l in inp]
seen = {}


def f(s, current_count, chunk_sizes):

    info = (s, current_count, chunk_sizes)
    if info in seen:
        return seen[info]

    if len(chunk_sizes) == 0:
        return "#" not in s
    if len(s) == 0:
        return len(chunk_sizes) == 1 and current_count == chunk_sizes[0]

    t = 0
    if s[0] in "?.":
        if current_count == 0:
            t += f(s[1:], 0, chunk_sizes)
        elif current_count == chunk_sizes[0]:
            t += f(s[1:], 0, chunk_sizes[1:])

    if s[0] in "?#":
        if current_count < chunk_sizes[0]:
            t += f(s[1:], current_count + 1, chunk_sizes)

    seen[info] = t
    return t


total = 0
for l in inp:
    springs, amounts = l.split()
    amounts = [int(x) for x in amounts.split(",")]

    springs = "?".join([springs for _ in range(5)])
    amounts = tuple(amounts * 5)

    total += f(springs, 0, amounts)

print(total)
