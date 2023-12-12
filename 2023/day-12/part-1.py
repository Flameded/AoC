with open("input.txt", "r") as f:
    inp = f.readlines()

inp = [l.strip("\n") for l in inp]


def f(s, current_count, chunk_sizes):

    if len(chunk_sizes) == 0:
        return "#" not in s
    if len(s) == 0:
        return current_count == chunk_sizes[0] and len(chunk_sizes) == 1

    if s[0] == ".":
        if current_count == 0:
            return f(s[1:], 0, chunk_sizes)

        if current_count != chunk_sizes[0]:
            return 0
        return f(s[1:], 0, chunk_sizes[1:])

    if s[0] == "#":
        return f(s[1:], current_count + 1, chunk_sizes)

    t = 0
    if s[0] == "?":
        # Acting as '.'
        if current_count == 0:
            t += f(s[1:], 0, chunk_sizes)
        elif current_count == chunk_sizes[0]:
            t += f(s[1:], 0, chunk_sizes[1:])

        # Acting as '#'
        t += f(s[1:], current_count + 1, chunk_sizes)

    return t


total = 0
for l in inp:
    springs, amounts = l.split()
    amounts = [int(x) for x in amounts.split(",")]

    total += f(springs, 0, amounts)

print(total)
