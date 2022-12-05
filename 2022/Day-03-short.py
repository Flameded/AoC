with open("input.txt", "r") as f:
    inp = [line.strip() for line in f.readlines()]

print(sum([(ord(list(set(l[:len(l) // 2]) & set(l[len(l) // 2:]))[0]) - 96) % 58 for l in inp]))
print(sum([(ord(list(set(inp[i]) & set(inp[i + 1]) & set(inp[i + 2]))[0]) - 96) % 58 for i in range(0, len(inp), 3)]))
