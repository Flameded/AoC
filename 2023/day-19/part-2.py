with open("input.txt", "r") as f:
    inp = f.read().split("\n\n")

workflows = {w.split("{")[0]: w[:-1].split("{")[1].split(",") for w in inp[0].splitlines()}


def f(curr, ranges):

    if curr == "A":
        x, m, a, s = ranges
        return (x[1]-x[0]+1) * (m[1]-m[0]+1) * (a[1]-a[0]+1) * (s[1]-s[0]+1)
    if curr == "R":
        return 0

    total = 0
    for rule in workflows[curr]:
        if ":" not in rule:
            total += f(rule, ranges)
            continue

        condition, to_go = rule.split(":")
        (ch, op), n = condition[:2], int(condition[2:])
        idx = "xmas".index(ch)

        lo, hi = ranges[idx]
        if op == ">":
            vlo, vhi = n + 1, hi
            nvlo, nvhi = lo, n
        else:
            vlo, vhi = lo, n - 1
            nvlo, nvhi = n, hi

        if vlo <= vhi:
            new_ranges = list(ranges)
            new_ranges[idx] = (vlo, vhi)
            total += f(to_go, new_ranges)
        if nvlo <= nvhi:
            ranges[idx] = (nvlo, nvhi)

    return total


print(f("in", [(1, 4000) for _ in range(4)]))
