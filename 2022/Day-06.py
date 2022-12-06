with open("input.txt", "r") as f:
    inp = [line.strip() for line in f.readlines()]


def first_marker(inp_string, check_length):
    for i in range(len(inp_string)):
        if len(set(inp_string[i - check_length:i])) == check_length:
            return i


print(first_marker(inp[0], 4))
print(first_marker(inp[0], 14))
