with open("input.txt", "r") as f:
    inp = f.readlines()

inp = [l.strip("\n") for l in inp]

t = 0
for l in inp:
    l = l.replace("one", "one1one")
    l = l.replace("two", "two2two")
    l = l.replace("three", "three3three")
    l = l.replace("four", "four4four")
    l = l.replace("five", "five5five")
    l = l.replace("six", "six6six")
    l = l.replace("seven", "seven7seven")
    l = l.replace("eight", "eight8eight")
    l = l.replace("nine", "nine9nine")

    digits = [ch for ch in l if ch.isdigit()]
    t += int(digits[0] + digits[-1])

print(f"Part 2: {t}")
