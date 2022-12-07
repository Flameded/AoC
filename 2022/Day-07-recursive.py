with open("input.txt", "r") as f:
    commands = [l.split() for l in f.readlines() if l.split()[1] != "ls"]


def get_sum(i, cmds, all_dir_sizes):
    file_sizes, dir_sizes = [], {}
    while i < len(cmds) - 1:
        i += 1
        command = cmds[i]
        if command[1] == "cd":
            if command[2] == "..":  # leaving the directory
                sums = sum(file_sizes) + sum(dir_sizes.values())
                all_dir_sizes.extend(dir_sizes.values())
                return i, sums, all_dir_sizes
            else:  # adding the size of the sub-directory
                i, dir_sum, all_dir_sizes = get_sum(i, cmds, all_dir_sizes)
                dir_sizes[command[2]] += dir_sum
        elif command[0] == "dir":  # creating new sub-directory
            dir_sizes[command[1]] = 0
        else:  # adding each file size to a list
            file_sizes.append(int(command[0]))

    # once all instructions have done --> outermost directory
    sums = sum(file_sizes) + sum(dir_sizes.values())
    all_dir_sizes.extend([val for val in dir_sizes.values() if val not in all_dir_sizes])  # no idea what this does
    all_dir_sizes.append(sums)

    return i, sums, all_dir_sizes


_, _, total = get_sum(0, commands, [])
print(sum([v for v in total if v <= 100_000]))
print(min([v for v in total if v >= max(total) - 40_000_000]))
