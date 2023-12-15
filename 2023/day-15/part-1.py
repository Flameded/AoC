with open("input.txt", "r") as f:
    inp = f.read().split(",")


total = 0
for s in inp:
    t = 0
    for ch in s:
         t += ord(ch)
         t *= 17
         t = t % 256
    total += t

print(total)
