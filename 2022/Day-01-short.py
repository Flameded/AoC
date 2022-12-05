with open("input.txt", "r") as f:
    inp = sorted([sum([int(i) for i in l.split()]) for l in f.read().split("\n\n")], reverse=True)

print(inp[0])
print(sum(inp[:3]))
