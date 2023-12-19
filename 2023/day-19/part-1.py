with open("input.txt", "r") as f:
    inp = [chunk.splitlines() for chunk in f.read().split("\n\n")]

workflows = {w.split("{")[0]: w[:-1].split("{")[1].split(",") for w in inp[0]}
parts = [[int(chunk.split("=")[1]) for chunk in p[1:-1].split(",")] for p in inp[1]]


def f(curr, x, m, a, s):

    if curr == "A":
        return True
    if curr == "R":
        return False

    for rule in workflows[curr]:
        if ":" not in rule:
            return f(rule, x, m, a, s)

        condition, to_go = rule.split(":")
        if eval(condition):
            return f(to_go, x, m, a, s)


print(sum(sum(part) * f("in", *part) for part in parts))
