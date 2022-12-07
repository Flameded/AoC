with open("input.txt", "r") as f:
  inp = [line.split() for line in f.readlines() if line.split()[1] != "ls"]

dir_sums = {(i, cmd[2]): 0 for i, cmd in enumerate(inp) if cmd[1] == "cd" and cmd[-1] != ".."}
s = []
for i, cmd in enumerate(inp):
  if cmd[1] == "cd":
    if cmd[2] == "..":  # Leaving
      dir_sums[s[-2]] += dir_sums[s.pop()]
    else:  # Entering
      s.append((i, cmd[2]))
  elif cmd[0] != "dir":  # Size of file
    dir_sums[s[-1]] += int(cmd[0])

while len(s) > 1:
  dir_sums[s[-2]] += dir_sums[s.pop()]

print(sum([v for v in dir_sums.values() if v <= 100_000]))
print(min([v for v in dir_sums.values() if v >= max(dir_sums.values()) - 40_000_000]))
