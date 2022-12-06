with open("input.txt", "r") as f:
    inp = [line.strip() for line in f.readlines()]

print([i for i in range(len(inp[0])) if len(set(inp[0][i - 4:i])) == 4][0])
print([i for i in range(len(inp[0])) if len(set(inp[0][i - 14:i])) == 14][0])
